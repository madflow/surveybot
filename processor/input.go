package processor

import (
	"fmt"
	"strconv"
	"time"

	"github.com/go-rod/rod"
	"github.com/jaswdr/faker"
	log "github.com/sirupsen/logrus"
)

func ProcessInputElement(page *rod.Page, element *rod.Element) error {
	elementType, elementTypeErr := element.Attribute("type")

	if elementTypeErr != nil {
		return elementTypeErr
	}

	log.Infof("Element type %s found: %s", *elementType, element.MustHTML())

	if element.MustDisabled() {
		log.Infof("Element disabled: %s", element.MustHTML())
		return nil
	}

	min := element.MustProperty("min")
	max := element.MustProperty("max")

	if *elementType == "email" {
		f := faker.New()
		email := f.Internet().Email()

		log.Infof("Input value: %s", email)
		return element.MustSelectAllText().Input(email)
	}

	if *elementType == "number" {
		minInt, _ := strconv.Atoi(min.String())
		maxInt, _ := strconv.Atoi(max.String())
		f := faker.New()
		var numberAsString string
		if minInt != 0 && maxInt != 0 {
			numberAsString = fmt.Sprintf("%d", f.IntBetween(minInt, maxInt))
		} else {
			numberAsString = fmt.Sprintf("%d", f.Int())
		}

		log.Infof("Input value: %s", numberAsString)
		return element.MustSelectAllText().Input(numberAsString)
	}

	if *elementType == "color" {
		f := faker.New()
		color := f.Color().Hex()
		log.Infof("Input value: %s", color)
		element.WaitInteractable()
		_, err := element.Eval(`(color) => this.value = color;`, color)
		return err
	}

	if *elementType == "date" || *elementType == "time" || *elementType == "datetime-local" {
		maxDate := time.Now()
		f := faker.New()
		date := f.Time().Time(maxDate)
		log.Infof("Input value: %s", date)
		return element.InputTime(date)
	}

	if *elementType == "month" {
		maxDate := time.Now()
		f := faker.New()
		date := f.Time().Time(maxDate)
		month := date.Format("2006-01")
		log.Infof("Input value: %s", month)
		element.MustFocus()
		element.MustWaitEnabled()
		element.MustWaitWritable()
		_, err := element.Eval(`(month) => this.value = month;`, month)
		return err
	}

	if *elementType == "week" {
		maxDate := time.Now()
		f := faker.New()
		date := f.Time().Time(maxDate)
		year, week := date.ISOWeek()
		value := fmt.Sprintf("%d-W%d", year, week)
		log.Infof("Input value: %s", value)
		element.MustWaitInteractable()
		_, err := element.Eval(`(value) => this.value = value;`, value)
		return err
	}

	if *elementType == "tel" {
		f := faker.New()
		tel := f.Internet().Faker.Phone().Number()
		log.Infof("Input value: %s", tel)
		return element.Input(tel)
	}

	if *elementType == "url" {
		f := faker.New()
		url := f.Internet().Faker.Internet().URL()
		log.Infof("Input value: %s", url)
		return element.Input(url)
	}

	if *elementType == "text" {
		f := faker.New()
		return element.Input(f.Lorem().Text(25))
	}

	log.Infof("Unsupported input type: %s", *elementType)
	return nil
}
