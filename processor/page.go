package processor

import (
	"time"

	"github.com/go-rod/rod"
	log "github.com/sirupsen/logrus"

	"github.com/madflow/surveybot/crawler"
)

func ProcessPage(page *rod.Page) {
	inputs := crawler.FindAllInputs(page)
	log.Infof("Found %d text inputs", len(inputs))
	for _, input := range inputs {
		label, errLabel := crawler.FindLabelElement(page, input)
		if errLabel == nil {
			log.Infof("Label found: %s", label.MustHTML())
		}
		log.Infof("Input: %s", input.MustHTML())
		err := ProcessInputElement(page, input)
		if err != nil {
			log.Errorf("Error processing input: %s", err)
		}
	}
	time.Sleep(5 * time.Second)
}
