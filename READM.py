import telebot
from telebot import types
import phonenumbers
from phonenumbers import carrier, geocoder
from phonenumbers import timezone

token = "6067541039:AAHvGGYPAVHGS7H85_KOnBGnhQByVHY67u0"#توكنك
bot = telebot.TeleBot(token)
btn = types.InlineKeyboardButton(text="قناتي",url = "https://t.me/SuPeRx1")

@bot.message_handler(commands=['start'])
def send_welcome(message):
    us = message.from_user.first_name
    b = types.InlineKeyboardMarkup()
    b.add(btn)
    bot.reply_to(message, f"مرحبا {us} ارسل لي رقم هاتف للحصول على معلومات عنه",reply_markup=b)

@bot.message_handler(content_types=['text'])
def info(message):
    	try:
    		number = message.text
    		timezone_number = phonenumbers.parse(number)
    		ti = timezone.time_zones_for_geographical_number(timezone_number)
    		ch_number = phonenumbers.parse(number,'CH')
    		co = geocoder.description_for_number(ch_number, 'en')
    		service_number = phonenumbers.parse(number,'RO')
    		se = carrier.name_for_number(service_number,'en')
    		
    		bot.reply_to(message,f"time zone: {ti}\nPhone number: {number}\nCountry: {co}\nService Provider: {se}")
    	except:bot.reply_to(message,'error, رقم الهاتف غير صحيح')

print('run')
bot.infinity_polling()
