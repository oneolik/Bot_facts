import requests
from deep_translator import GoogleTranslator
import os
import telebot
from dotenv import load_dotenv
import time

EMOJIS = ["🔢", "📊", "🧮", "💡", "🎯", "🌟"]

load_dotenv()
TOKEN = '8381700139:AAHNNOrqvBZRDy61_FQdG83a7hoKBJk6lcI'
bot = telebot.TeleBot(TOKEN)

# Указываем канал
CHANNEL = "@factsssssssssssssssssssssss"  # Канал из ссылки

while True:
    try:
        # Получаем факт
        response = requests.get('https://uselessfacts.jsph.pl/api/v2/facts/random' , timeout=10)
        fact = response.json()['text']
        
        # Переводим на русский
        fact = GoogleTranslator(source='auto', target='ru').translate(fact)
        
        # Отправляем в канал
        bot.send_message(CHANNEL, fact)
        print(f"✅ Отправлено в канал {CHANNEL}")
        
    except Exception as e:
        print(f"❌ Ошибка: {e}")
    
    # Ждем 1 минуту (60 секунд)
    time.sleep(60)