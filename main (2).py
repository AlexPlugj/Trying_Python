import telebot
import random
import requests
from bs4 import BeautifulSoup
import json


bot = telebot.TeleBot('6037374947:AAEXNzxXZRH6y8q8cMrZ3gmeEUpOLb7b0WQ')

Dollar_Uah_NB = 'https://bank.gov.ua/NBUStatService/v1/statdirectory/exchange?json'
headers = {'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:109.0) Gecko/20100101 Firefox/111.0'}
infa1 = requests.get(Dollar_Uah_NB, headers=headers).json()
#data = json.loads(infa1.text)
print(infa1)



@bot.message_handler(commands=['kurs'])
def kurs(message):
    
    Dollar_Uah_G = 'https://www.google.com/search?q=%D0%BA%D1%83%D1%80%D1%81+%D0%B4%D0%BE%D0%BB%D0%BB%D0%B0%D1%80%D0%B0+%D0%BD%D0%B0+%D1%81%D0%B5%D0%B3%D0%BE%D0%B4%D0%BD%D1%8F&sxsrf=APwXEdfSqNUFc2-p36ghGeKWLHGwIbgf-A%3A1681142965961&source=hp&ei=tTQ0ZP26OMOG8gLy55PYBA&iflsig=AOEireoAAAAAZDRCxS3zDRcHkJHULf3nITpR5x2vMy8u&oq=rehc+&gs_lcp=Cgdnd3Mtd2l6EAMYADIMCCMQsQIQJxBGEIICMgcIABCKBRBDMg0IABCABBCxAxCDARAKMgsIABCKBRAKEAEQQzINCAAQgAQQsQMQgwEQCjILCAAQigUQChABEEMyCwgAEIoFEAoQARBDMgkIABCKBRAKEEMyBwgAEIAEEAoyDQgAEIAEELEDEIMBEAo6BAgjECc6DgguEIAEELEDEIMBENQCOgsIABCABBCxAxCDAToUCC4QgAQQsQMQgwEQxwEQ0QMQ1AI6BQgAEIAEOggIABCABBCxAzoNCC4QigUQxwEQ0QMQQzoNCAAQigUQsQMQgwEQQzoRCC4QgAQQsQMQgwEQxwEQ0QM6DgguEIAEELEDEMcBENEDOhMILhCKBRCxAxCDARDHARDRAxBDOgkIABCABBAKEAE6BwgjELECECdQAFixBmCRHGgAcAB4AIABZ4gBxwOSAQM0LjGYAQCgAQE&sclient=gws-wiz'
    headers = {'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:109.0) Gecko/20100101 Firefox/111.0'}
    infa = requests.get(Dollar_Uah_G, headers=headers)
    soup = BeautifulSoup(infa.content, "lxml")
    convert = soup.find_all("span", {"class": "DFlfde SwHCTb", "data-precision": "2"})
    bot.reply_to(message, "Долар на сьогодні:" + convert[0].text + "грн")

@bot.message_handler(commands=['start'])
def istart(message:telebot.types.Message):
    mess = f'Hi, {message.from_user.first_name} {message.from_user.last_name}, ti pidor'
    bot.reply_to(message, mess, parse_mode='html')

@bot.message_handler(commands=['prognoz'])
def prognoz(message):
      list1 = ["Поставиш сьогодні Плужку каву", "Поставиш сьогодні Плужку пиво", "Накормиш сьогодні Плужка", "Підеш нахуй", "Підеш в дупу"]
      ppp = random.randint(0, len(list1) - 1)
      bot.reply_to(message, list1[ppp])

@bot.message_handler(commands=['kek'])
def keknut(message):
   kkk = f'lol,kek,cheburek'
   bot.reply_to(message, kkk)

 #  @bot.message_handler(commands=['kurs'])


#@bot.message_handler(func=lambda m: True)
#def vidp(message: telebot.types.Message):
#       print(message)
#       if message.text == "pidor":
#         bot.reply_to(message, "Sam ti pidor")
#       elif message.text == "Pizdec":
#         bot.reply_to(message, "Idy na huy")
#       else:
#          bot.reply_to(message, "Blyat")       

bot.infinity_polling()

