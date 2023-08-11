package crawler

import (
	"github.com/go-rod/rod"
)

func FindAllInputs(page *rod.Page) rod.Elements {
	inputs := page.MustElements("input")
	textareas := page.MustElements("textarea")
	return append(inputs, textareas...)
}

func FindAllTextInputs(page *rod.Page) rod.Elements {
	textInputs := page.MustElements("input[type='text']")
	textareas := page.MustElements("textarea")
	return append(textInputs, textareas...)
}
