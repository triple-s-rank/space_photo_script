import argparse
import os
import time

import telegram
from dotenv import load_dotenv


def publish_all_images(delay, api_key, chat_id):
    bot = telegram.Bot(token=api_key)
    while True:
        for root, dirs, files in os.walk('images'):
            for photo in files:
                with open(f'images/{photo}', 'rb') as photo_to_publish:
                    bot.send_photo(chat_id=chat_id, photo=photo_to_publish)
                time.sleep(delay)


def main():
    load_dotenv()
    bot_api_key = os.environ.get('BOT_API_KEY')
    telegram_chat = os.environ.get('CHAT_ID')
    parser = argparse.ArgumentParser(description='Publish photo to your telegram channel once in 4 hours by default')
    parser.add_argument('-t', '--time_delay', help='Time delay in hours.', type=int)
    args = parser.parse_args()
    if not args.time_delay:
        publish_all_images(os.environ.get('TIME_DELAY')*3600, bot_api_key, telegram_chat)
    else:
        publish_all_images(args.time_delay*3600, bot_api_key, telegram_chat)


if __name__ == "__main__":
    main()

