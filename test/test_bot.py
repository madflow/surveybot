from common import shutdown_server
import sys
import unittest
from surveybot import bot
from web.app import app
from multiprocessing import Process


class BotTest(unittest.TestCase):

    def test_initialize(self):
        server = Process(target=app.run)
        server.start()
        o = bot.SurveyBot('http://localhost:5000')
        b = Process(target=o.run)
        b.start()
        server.terminate()
        b.terminate()
        b.join()
        server.join()
