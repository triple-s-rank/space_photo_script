import os.path
from pathlib import Path
from urllib.parse import urlparse, unquote
import requests
from dotenv import load_dotenv


Path(f'{Path.cwd()}\images').mkdir(parents=True, exist_ok=True)
load_dotenv()

def download_image(image_url, filename):
    response = requests.get(image_url)
    response.raise_for_status()

    with open(f'images/{filename}', 'wb') as file:
        file.write(response.content)


filename = "hubble.jpeg"
url = "https://upload.wikimedia.org/wikipedia/commons/3/3f/HST-SM4.jpeg"
download_image(url, filename)


def fetch_spacex_last_launch(launch_id):
    launch_url = f'https://api.spacexdata.com/v3/launches/{launch_id}'
    response = requests.get(url=launch_url)
    response.raise_for_status()
    launch_images = response.json()['links']['flickr_images']
    for image_number, image_url in enumerate(launch_images, start=0):
        download_image(image_url, f'spacex_{image_number}.jpeg')


def fetch_nasa_apod():
    apod_url = "https://api.nasa.gov/planetary/apod"
    params = {'api_key': os.environ.get('API_KEY')}
    response = requests.get(url=apod_url, params=params)
    response.raise_for_status()
    return response.json()['url']


def get_file_type(random_url):
    parsed_url = urlparse(random_url)
    unquoted = unquote(parsed_url.path)
    path, extension = os.path.splitext(unquoted)
    return extension

