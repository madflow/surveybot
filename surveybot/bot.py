# -*- coding: utf-8 -*-
"""Bot Working Horse"""
import random

from splinter import Browser
from splinter.exceptions import ElementDoesNotExist


class SurveyBot(object):
    """Hit em hard"""
    url = None
    varmap = None
    random_text = [
        42,
        '42@lol.com',
        'Lorem ipsulum',
        '1999',
    ]

    def __init__(self, url=None, varmap=None):
        self.url = url
        self.varmap = varmap

    def run(self):
        """Run the b0t"""
        browser = Browser()
        browser.visit(self.url)

        try:
            while browser.find_by_tag('button').first:
                self.process_elements(browser)
                browser.find_by_tag('button').first.click()
        except ElementDoesNotExist:
            pass

    def process_elements(self, browser):
        for field in browser.find_by_xpath('//input[@type="text"]'):
            self.process_text(field)

        for password_field in browser.find_by_xpath('//input[@type="password"]'):
            self.process_text(password_field)

        for checkbox in browser.find_by_xpath('//input[@type="checkbox"]'):
            self.process_textbox(checkbox)

        for textarea in browser.find_by_tag('textarea'):
            self.process_text(textarea)

        for select in browser.find_by_tag('select'):
            self.process_select(select)

    def process_text(self, el):
        """Process input[type="text"] and textareas"""
        if self.varmap is None:
            self._random_text(el)
        else:
            pass

    def _random_text(self, el):
        """Insert random text"""
        try:
            random.shuffle(self.random_text)
            el.value = self.random_text[0]
        except:
            pass

    def process_select(self, el):
        if self.varmap is None:
            options = el.find_by_tag('option')
            if el['multiple']:
                for i in range(1,len(options)):
                    random.choice(options).click()
            else:
                random.choice(options).click()
        else:
            pass

    def process_textbox(self, el):
        """Process input[type="checkbox"]"""
        if self.varmap is None:
            self._process_random_checkbox(el)
        else:
            pass

    def _process_random_checkbox(self, el):
        try:
            check = bool(random.getrandbits(1))
            if check is True:
                el.check()
            else:
                el.uncheck()
        except:
            pass