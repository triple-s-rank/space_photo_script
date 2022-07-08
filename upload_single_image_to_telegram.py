import argparse
import os
import random

import telegram
from dotenv import load_dotenv


def publish_all_images(image_name, api_key, chat_id):
    bot = telegram.Bot(token=api_key)
    if not image_name:
        for root, dirs, files in os.walk('images'):
            with open(f'images/{random.choice(files)}', 'rb') as photo_to_upload:
                bot.send_photo(chat_id=chat_id, photo=photo_to_upload)
    else:
        with open(f'images/{image_name}', 'rb') as photo_to_upload:
            bot.send_photo(chat_id=chat_id, photo=photo_to_upload)


def main():
    load_dotenv()
    bot_api_key = os.environ.get('BOT_API_KEY')
    telegram_chat = os.environ.get('CHAT_ID')
    parser = argparse.ArgumentParser(description='Publish chosen or random photo to your telegram channel')
    parser.add_argument('-i', '--image_name', help='Full mage name to upload.')
    args = parser.parse_args()
    publish_all_images(args.image_name, bot_api_key, telegram_chat)


if __name__ == "__main__":
    main()


