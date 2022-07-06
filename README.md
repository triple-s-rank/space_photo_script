# Скрипты для скачивания изображений Nasa, SpaceX и их загрузки в Telegram.

Набор скриптов для скачивания фотографий космической тематики и дальнейшей загрузки их через бота в канал/чат Telegram.

## Установка

### Окружение
Python3 должен быть предустановлен. Затем используйте pip для установки зависимостей:
```
pip install -r requirements.txt
```
### Переменные окружения

Создайте и заполните переменную окружения `.env` для необходимых настроек.
Пример `.env`:

```
NASA_API_KEY={Nasa api key}
BOT_API_KEY={Bot api key}
TELEGRAM_CHANNEL={Channel id}
TIME_DELAY={Delay in seconds}
```

## Скрипты

### fetch_spacex_launch_image.py
Загружает с сайта [SpaceX](https://api.spacexdata.com) фотографию указанного запуска, если не указывать id запуска - скачает фото последнего запуска. Фотографии запуска сохраняет в директорию `images`. Запуск:
```
python fetch_spacex.py -id {launch_id}
```

### fetch_nasa_picture_of_day.py
Загружает с сайта космического агенства [NASA](https://api.nasa.gov/) несколько фотографий, или последнюю фотографию -если количество не указывать при запуске скрипта  в директорию `images`. Для работы скрипта необходим API Key [NASA](https://api.nasa.gov/#signUp), сохранить в `NASA_API_KEY` файла `.env`. Запуск:
``` 
python fetch_nasa_picture_of_day.py -n {number of images to download}
```

### fetch_nasa_earth_image.py
Загружает с сайта космического агенства [NASA](https://api.nasa.gov/) фотографии Земли за указанную дату в директорию `images`. Для работы скрипта необходим API Key [NASA](https://api.nasa.gov/#signUp), сохранить в `NASA_API_KEY` файла `.env`. Запуск:
``` 
python fetch_nasa_earth_image.py  {date YYYY-MM-DD}
```

### upload_all_images_to_telegram.py
Публикует фотографии из папки 'images' в Telegram канал с определенной периодичностью, id которого следует указать в файле `.env`. API Key вашего бота следуте сохранить в соответствующую переменную в `.env`. Периодичность публикации по умолчанию составляет 4 часа, при запуске скрипта опционально можно задать необходимое значение. Периодичность можно задать в переменной `TIME_DELAY` файла `.env`. Запуск:
``` 
python upload_all_images_to_telegram.py -е {time delay in hours}
```


### upload_single_image_to_telegram.py
Публикует одну фотографию из папки 'images' в Telegram канал, id которого следует указать в файле `.env`. API Key  вашего бота следуте сохранить в соответствующую переменную в `.env`. Указав полное имя фотографии из папки 'images' при запуске скрипта вы загрузите конкретное фото, не передав параметры загрузится случайное фото из папки.Запуск:
``` 
python upload_single_image_to_telegram.py -i {full image name}
```


### Цель проекта

Код написан в образовательных целях на онлайн-курсе для веб-разработчиков [dvmn.org](https://dvmn.org/).
