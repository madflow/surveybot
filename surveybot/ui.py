import argparse

def process_run(args):
    print args.participants
    '''
    from surveybot.bot import SurveyBot
    bot = SurveyBot(args.url)
    bot.run()
    '''

def main():
    parser = argparse.ArgumentParser(description='Smack a survey')

    parser.add_argument('url')
    parser.add_argument('--p', dest='participants', help='Number of participants', type=int)
    parser.add_argument('--s', default=1, dest='simultaneous', help='Simultaneous participants', type=int)
    parser.add_argument('--l', dest='list', help='Participants/Variable list')
    parser.add_argument('--D', dest='debug', help='Print debug messages')
    parser.set_defaults(func=process_run)
    args = parser.parse_args()
    args.func(args)