package processor

import (
	"github.com/go-rod/rod"
	log "github.com/sirupsen/logrus"

	"github.com/madflow/surveybot/crawler"
)

func IsSubmittablePage(page *rod.Page) bool {
	nextSubmitButton, err := crawler.GuessNextButton(page)
	return err == nil && nextSubmitButton == nil
}

func ProcessSurvey(page *rod.Page) {
	numberOfSubmits := 0
	for {
		ProcessPage(page)
		nextSubmitButton, err := crawler.GuessNextButton(page)
		if err != nil {
			log.Infof("There is no next submit button")
			break
		}
		log.Infof("Next submit button found: %s", nextSubmitButton.MustHTML())
		nextSubmitButton.MustWaitInteractable().MustClick()
		numberOfSubmits++
		log.Infof("Submit Count is: %d", numberOfSubmits)
	}
}
