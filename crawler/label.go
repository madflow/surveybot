package crawler

import (
	"fmt"

	"github.com/go-rod/rod"
)

func FindLabelElement(page *rod.Page, element *rod.Element) (*rod.Element, error) {
	id, errId := element.Attribute("id")
	name, errName := element.Attribute("name")

	if errId == nil && errName == nil {
		return nil, fmt.Errorf("no id or name found")
	}

	if errId != nil {
		return page.Element(fmt.Sprintf("label[id='%s']", *id))
	}

	if errName != nil {
		return page.Element(fmt.Sprintf("label[name='%s']", *name))
	}

	return nil, fmt.Errorf("no label found")
}
