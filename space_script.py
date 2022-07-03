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