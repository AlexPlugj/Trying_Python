import telebot
import telegram
from telegram import MessageEntity
from telegram.ext import Updater
import random
import requests
from bs4 import BeautifulSoup
import json
import openai
import pymysql
from config import host, user, password, db_name
import os



bot = telebot.TeleBot('6037374947:AAEXNzxXZRH6y8q8cMrZ3gmeEUpOLb7b0WQ')
openai.api_key = ('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')
client_status = {}




@bot.message_handler(commands=['kurs'])
def kurs(message):
    Dollar_Uah_PB = 'https://api.privatbank.ua/p24api/pubinfo?exchange&json&coursid=11'
    headers = {'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:109.0) Gecko/20100101 Firefox/111.0'}
    infa2 = requests.get(Dollar_Uah_PB, headers=headers).json()
    infa_dol1 = infa2[1]
    kurs_pb_dol = str(infa_dol1['buy'])
    Dollar_Uah_NB = 'https://bank.gov.ua/NBUStatService/v1/statdirectory/exchange?json'
    headers = {'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:109.0) Gecko/20100101 Firefox/111.0'}
    infa1 = requests.get(Dollar_Uah_NB, headers=headers).json()
    infa_dol = infa1[24]
    kurs_nb_dol = str(infa_dol['rate'])
    #print("Національний Банк:" + kurs_nb_dol +"грн")
    Dollar_Uah_G = 'https://www.google.com/search?q=%D0%BA%D1%83%D1%80%D1%81+%D0%B4%D0%BE%D0%BB%D0%BB%D0%B0%D1%80%D0%B0+%D0%BD%D0%B0+%D1%81%D0%B5%D0%B3%D0%BE%D0%B4%D0%BD%D1%8F&sxsrf=APwXEdfSqNUFc2-p36ghGeKWLHGwIbgf-A%3A1681142965961&source=hp&ei=tTQ0ZP26OMOG8gLy55PYBA&iflsig=AOEireoAAAAAZDRCxS3zDRcHkJHULf3nITpR5x2vMy8u&oq=rehc+&gs_lcp=Cgdnd3Mtd2l6EAMYADIMCCMQsQIQJxBGEIICMgcIABCKBRBDMg0IABCABBCxAxCDARAKMgsIABCKBRAKEAEQQzINCAAQgAQQsQMQgwEQCjILCAAQigUQChABEEMyCwgAEIoFEAoQARBDMgkIABCKBRAKEEMyBwgAEIAEEAoyDQgAEIAEELEDEIMBEAo6BAgjECc6DgguEIAEELEDEIMBENQCOgsIABCABBCxAxCDAToUCC4QgAQQsQMQgwEQxwEQ0QMQ1AI6BQgAEIAEOggIABCABBCxAzoNCC4QigUQxwEQ0QMQQzoNCAAQigUQsQMQgwEQQzoRCC4QgAQQsQMQgwEQxwEQ0QM6DgguEIAEELEDEMcBENEDOhMILhCKBRCxAxCDARDHARDRAxBDOgkIABCABBAKEAE6BwgjELECECdQAFixBmCRHGgAcAB4AIABZ4gBxwOSAQM0LjGYAQCgAQE&sclient=gws-wiz'
    headers = {'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:109.0) Gecko/20100101 Firefox/111.0'}
    infa = requests.get(Dollar_Uah_G, headers=headers)
    soup = BeautifulSoup(infa.content, "lxml")
    convert = soup.find_all("span", {"class": "DFlfde SwHCTb", "data-precision": "2"})
    bot.reply_to(message, "Долар на сьогодні:\n" + "Google каже:" + ' ' + convert[0].text + "грн\n" + "НацБанк каже:" + ' ' + kurs_nb_dol +"грн\n" + "Privat каже:" + ' ' + kurs_pb_dol + "грн")

@bot.message_handler(commands=['start'])
def istart(message:telebot.types.Message):
    fam = message.from_user.last_name
    if fam == 'None':
     mess = f'Hi, {message.from_user.first_name}, ti pidor'
    else:
     mess = f'Hi, {message.from_user.first_name} {message.from_user.last_name}, ti pidor'
    bot.reply_to(message, mess, parse_mode='html')
  
@bot.message_handler(commands=['prognoz'])
def prognoz(message):
      list1 = ["Поставиш сьогодні Плужку каву", "Поставиш сьогодні Плужку пиво", "Накормиш сьогодні Плужка", "Підеш нахуй", "Підеш в дупу"]
      ppp = random.randint(0, len(list1) - 1)
      bot.reply_to(message, list1[ppp])

  
@bot.message_handler(commands=['kek'])
def keknut(message):
   kkk = f'Лол, Кек, Чебурек'
   bot.reply_to(message, kkk)

@bot.message_handler(commands=['speak'])
def speak(message):
    client_id = message.from_user.id
    client_status[client_id] = 'wait_for_data'
    bot.reply_to(message, text='Введіть текст: ')

@bot.message_handler(content_types=['text'])
def handler(message):
    client_id = message.from_user.id
    if client_id in client_status and client_status[client_id] == 'wait_for_data':
     response = openai.Completion.create(
     model="text-davinci-003",
     prompt= message.text,
     temperature=0.5,
     max_tokens=2000,
     top_p=1.0,
     frequency_penalty=0.5,
     presence_penalty=0.0,
     )
    bot.reply_to(message, text=response['choices'][0]['text'])
    del client_status[client_id]


   

#@bot.message_handler(func=lambda m: True)
#def vidp(message: telebot.types.Message):
       #if message.text == ("підор"):
        # bot.reply_to(message, "Сам ти підор")
       #elif message.text == ("піздец"):
       #  bot.reply_to(message, "Йди на хуй")
#    response = openai.Completion.create(
#     model="text-davinci-003",
#     prompt= message.text,
#     temperature=0.5,
#     max_tokens=1000,
#     top_p=1.0,
#     frequency_penalty=0.5,
#     presence_penalty=0.0,
#    )
#    bot.reply_to(message, text=response['choices'][0]['text'])   



bot.infinity_polling()
