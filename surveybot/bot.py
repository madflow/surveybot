from bs4 import BeautifulSoup
import requests
from splinter import Browser

class SurveyBot(object):

    url = None
    varmap = None
    
    def __init__(self, url=None, varmap=None):
        self.url = url
        self.varmap= varmap

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


    def process_textarea(textarea):
        pass


        

  
