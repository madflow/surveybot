import argparse

def process_run(args):
    from surveybot.bot import SurveyBot
    bot = SurveyBot(url = args.url, varmap = args.list, browser =args.browser)
    bot.run()

def main():
    parser = argparse.ArgumentParser(description='Fill out an online survey. Let\'s do this')

    parser.add_argument('url')
    parser.add_argument('-p', dest='participants', help='Number of participants', type=int)
    parser.add_argument('-s', default=1, dest='simultaneous', help='Simultaneous participants', type=int)
    parser.add_argument('-l', dest='list', help='Participants/Variable list')
    parser.add_argument('-b', default='firefox', dest='browser', help='Browser Driver (firefox|chrome|phantomjs)', type=str)
    parser.add_argument('-D', dest='debug', help='Print debug messages')
    parser.set_defaults(func=process_run)
    args = parser.parse_args()
    args.func(args)