from bs4 import BeautifulSoup
import requests
from splinter import Browser

class SurveyBot(object):

    url = None
    config = None
    
    def __init__(self, url, config):
        self.url = url
        self.config = config

    def run(self):
        browser = Browser()
        browser.visit(self.url)

        for field in browser.find_by_tag('input'):
            field.value='Hello'

        

  
