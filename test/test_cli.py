import common
import sys
import unittest
from surveybot import ui


class CliTest(unittest.TestCase):
    def test_simple(self):
        self.assertTrue(1==1)
        