# -*- coding: utf-8 -*-

"""
Bot Working Horse
"""

import random

from splinter import Browser
from splinter.exceptions import ElementDoesNotExist

from time import sleep

class SurveyBot(object):

    url = None
    varmap = None
    browser = None

    random_text = [
        42,
        '42@lol.com',
        'Lorem ipsulum',
        '1999',
    ]
    next_button_xpath = '//input[@type="submit"] | //button[@type="submit"]'

    def __init__(self, url = None, varmap = None, browser = 'firefox'):
        self.url = url
        self.varmap = varmap
        self.browser = browser

    def run(self):
        """Run the b0t"""
        browser = Browser(self.browser)
        browser.visit(self.url)

        try:
            while browser.find_by_xpath(self.next_button_xpath):
                self.process_elements(browser)
                browser.find_by_xpath(self.next_button_xpath).last.click()
        except ElementDoesNotExist:
            pass

        try:
            window = browser.windows[0]
            window.close()
        except:
            pass


    def process_elements(self, browser):
        for field in browser.find_by_xpath('//input[@type="text"]'):
            self.process_text(field)

        for password_field in browser.find_by_xpath('//input[@type="password"]'):
            self.process_text(password_field)

        for checkbox in browser.find_by_xpath('//input[@type="checkbox"]'):
            self.process_textbox(checkbox)

        for radio in browser.find_by_xpath('//input[@type="radio"]'):
            self.process_radio(radio)

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

    def process_radio(self, el):
        if self.varmap is None:
            self._process_random_radio(el)
            sleep(1)
        else:
            pass

    def _process_random_radio(self, el):
        el.check()

    def _process_random_checkbox(self, el):
        try:
            check = bool(random.getrandbits(1))
            if check is True:
                el.check()
            else:
                el.uncheck()
        except:
            pass
