import argparse
import os
import random
import time

import telegram
from dotenv import load_dotenv


def publish_all_images(image_name):
    bot = telegram.Bot(token=os.environ.get('BOT_API_KEY'))
    if not image_name:
        for root, dirs, files in os.walk('images'):
            bot.send_photo(chat_id=os.environ.get('CHAT_ID'), photo=open(f'images/{random.choice(files)}', 'rb'))
    else:
        bot.send_photo(chat_id=os.environ.get('CHAT_ID'), photo=open(f'images/{image_name}', 'rb'))


if __name__ == "__main__":
    load_dotenv()
    parser = argparse.ArgumentParser(description='Publish chosen or random photo to your telegram channel')
    parser.add_argument('-i', '--image_name', help='Full mage name to upload.')
    args = parser.parse_args()
    publish_all_images(args.image_name)

