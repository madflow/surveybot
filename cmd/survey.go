package cmd

import (
	"fmt"

	"github.com/go-rod/rod"
	"github.com/go-rod/rod/lib/launcher"
	"github.com/go-rod/stealth"
	log "github.com/sirupsen/logrus"
	"github.com/spf13/cobra"

	"github.com/madflow/surveybot/processor"
)

type SurveyOpts = struct {
	Url  string
	Show bool
}

var (
	surveyOpts SurveyOpts
	surveyCmd  = &cobra.Command{
		Use:   "survey",
		Short: "Fill out an online survey",
		Run: func(cmd *cobra.Command, args []string) {
			launcher := launcher.New().StartURL(surveyOpts.Url)
			launcher.Headless(!surveyOpts.Show)
			controlURL, err := launcher.Launch()
			if err != nil {
				fmt.Println(err)
			}
			browser := rod.New().ControlURL(controlURL).MustConnect()
			defer browser.MustClose()

			page, err := stealth.Page(browser)
			if err != nil {
				fmt.Println(err)
			}

			errNavigate := page.Navigate(surveyOpts.Url)

			if errNavigate != nil {
				log.Errorf("Failed to navigate: %s", surveyOpts.Url)
				return
			}

			page.MustWaitLoad()
			log.Infof("Survey page loaded: %s", surveyOpts.Url)

			processor.ProcessSurvey(page)
			log.Infof("Survey finishes: %s", surveyOpts.Url)
		},
	}
)

func init() {
	surveyCmd.Flags().StringVarP(&surveyOpts.Url, "url", "u", "", "URL of the survey")
	surveyCmd.Flags().BoolVarP(&surveyOpts.Show, "show", "s", false, "Run in headless mode")
	rootCmd.AddCommand(surveyCmd)
}
