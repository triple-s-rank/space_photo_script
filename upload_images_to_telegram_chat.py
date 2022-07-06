import argparse
import os
import time

import telegram
from dotenv import load_dotenv


def publish_image(delay=14400):
    bot = telegram.Bot(token=os.environ.get('BOT_API_KEY'))
    while True:
        for root, dirs, files in os.walk('images'):
            for photo in files:
                bot.send_photo(chat_id=os.environ.get('CHAT_ID'), photo=open(f'images/{photo}', 'rb'))
                time.sleep(delay)


if __name__ == "__main__":
    load_dotenv()
    parser = argparse.ArgumentParser(description='Publish photo to your telegram channel once in 4 hours by default')
    parser.add_argument('-t', '--time_delay', help='Time delay in hours.', type=int)
    args = parser.parse_args()
    if not args.time_delay:
        publish_image(os.environ.get('TIME_DELAY'))
    else:
        publish_image(args.time_delay*3600)

