import argparse
import requests
from download_image import download_image


def fetch_spacex_launch(flight_id):
    if not flight_id:
        launch_url = 'https://api.spacexdata.com/v3/launches/latest'
    else:
        launch_url = f'https://api.spacexdata.com/v3/launches/{flight_id}'
    response = requests.get(url=launch_url)
    response.raise_for_status()
    launch_images = response.json()['links']['flickr_images']
    for image_number, image_url in enumerate(launch_images, start=0):
        download_image(image_url, f'spacex_{image_number}.jpeg')


def main():
    parser = argparse.ArgumentParser(description='Enter flight id to download its images in "current_folder/images"')
    parser.add_argument('-id', '--flight_id', help='Flight id')
    args = parser.parse_args()
    fetch_spacex_launch(args.flight_id)


if __name__ == '__main__':
    main()
