import os
from pathlib import Path
from urllib.parse import urlparse, unquote

import argparse
import requests


def download_image(image_url, filename, image_payload=None):
    response = requests.get(image_url, params=image_payload)
    response.raise_for_status()

    with open(f'images/{filename}', 'wb') as file:
        file.write(response.content)


def get_image_name(image_url):
    parsed_url = urlparse(image_url)
    unquoted_path = unquote(parsed_url.path)
    path, downloaded_filename = os.path.split(unquoted_path)
    return downloaded_filename


if __name__ == '__main__':
    Path(f'{Path.cwd()}/images').mkdir(parents=True, exist_ok=True)
    parser = argparse.ArgumentParser(description='Enter image url to download it in "current_folder/images"')
    parser.add_argument('image_url')
    args = parser.parse_args()
    download_image(args.image_url, get_image_name(args.image_url))
