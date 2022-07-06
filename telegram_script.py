import os

import telegram
from dotenv import load_dotenv

load_dotenv()
bot = telegram.Bot(token=os.environ.get('BOT_API_KEY'))
