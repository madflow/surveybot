package crawler

import (
	"fmt"

	"github.com/go-rod/rod"
)

func FindAllButtons(page *rod.Page) (rod.Elements, error) {
	buttons := page.MustElements("button")
	inputTypeButtons, err := page.Elements("input[type='button']")
	if err != nil {
		return nil, err
	}
	// return merged elements
	return append(buttons, inputTypeButtons...), nil
}

func GuessNextButton(page *rod.Page) (*rod.Element, error) {
	buttons, err := FindAllButtons(page)
	if err != nil {
		return nil, err
	}
	if len(buttons) == 0 {
		err := fmt.Errorf("no buttons found")
		return nil, err
	}
	return buttons.Last(), nil
}
