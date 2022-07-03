import requests
from pathlib import Path

Path(f'{Path.cwd()}\images').mkdir(parents=True, exist_ok=True)


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


