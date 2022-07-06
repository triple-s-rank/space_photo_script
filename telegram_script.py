import os

import telegram
from dotenv import load_dotenv

load_dotenv()
bot = telegram.Bot(token=os.environ.get('BOT_API_KEY'))
bot.send_message(chat_id=os.environ.get('CHAT_ID'), text="working")