import argparse
import os
from datetime import datetime

import requests
from dotenv import load_dotenv

from download_image import download_image


def fetch_nasa_epic(date, api_key):
    endpoint = f'https://api.nasa.gov/EPIC/api/natural/date/{date}'
    params = {'api_key': api_key}
    response = requests.get(url=endpoint, params=params)
    for photo in response.json():
        photo_date = datetime.strptime(photo['date'], '%Y-%m-%d %H:%M:%S')
        photo_name = photo['image']
        photo_url = f'https://api.nasa.gov/EPIC/archive/natural/' \
                    f'{photo_date.year}/{photo_date.month}/{photo_date.day}/png/{photo_name}.png'
        download_image(photo_url, f'{photo_name}.png', image_payload=params)


def main():
    load_dotenv()
    nasa_api_key = os.environ.get('NASA_API_KEY')
    parser = argparse.ArgumentParser(
        description='Enter the date in format "YYYY-MM-DD" to download earth image to "current_folder/images"'
    )
    parser.add_argument('date', help='Date of images to download')
    args = parser.parse_args()
    fetch_nasa_epic(args.date, nasa_api_key)


if __name__ == '__main__':
    main()

