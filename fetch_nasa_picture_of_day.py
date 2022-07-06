import argparse
import os
import requests
from dotenv import load_dotenv

from download_image import download_image, get_image_name


def fetch_nasa_apod(images_to_download):
    apod_url = "https://api.nasa.gov/planetary/apod"
    params = {'api_key': os.environ.get('API_KEY')}
    if images_to_download:
        params['count'] = images_to_download
    response = requests.get(url=apod_url, params=params)
    response.raise_for_status()
    if images_to_download:
        for apod in response.json():
            download_image(apod['url'], get_image_name(apod['url']))
    else:
        download_image(response.json()['url'], get_image_name(response.json()['url']))


if __name__ == '__main__':
    load_dotenv()
    parser = argparse.ArgumentParser(
        description='Enter number of images you want to download to "current_folder/images"'
    )
    parser.add_argument('-n', '--images_number', help='Number of images to download')
    args = parser.parse_args()
    fetch_nasa_apod(args.images_number)
