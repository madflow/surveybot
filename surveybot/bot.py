from bs4 import BeautifulSoup
import requests
import mechanize

class SurveyBot(object):

    url = False
    config = False
    
    def __init__(self, url):
        self.url = url

    def run(self):
        br = mechanize.Browser()
        br.set_handle_refresh(True)
        br.set_debug_redirects(True)
        br.set_debug_responses(True)
        br.set_debug_http(True)
        br.open(self.url)

        for i in range(1, 10):
            br.select_form(nr=0)
            response = br.submit()
            print response.read()
