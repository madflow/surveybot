from bs4 import BeautifulSoup
import requests
from splinter import Browser

class SurveyBot(object):

    url = None
    config = None
    
    def __init__(self, url, config=None):
        self.url = url
        self.config = config

    def run(self):
        browser = Browser()
        browser.visit(self.url)

        fields = []
        textareas = []
        for field in browser.find_by_tag('input'):
            fields.append(field)

        for textarea in browser.find_by_tag('textarea'):
            textareas.append(textarea)

        while(browser.find_by_tag('button').first):
            browser.find_by_tag('button').first.click()





        

  
