import telebot
import telegram
from telegram import MessageEntity
from telegram.ext import Updater
#import random
import requests
#from bs4 import BeautifulSoup
#import json
#import openai
import pymysql
import os

host = "localhost"
user = "Alex"
password = "Alex"
db_name = "Proba"

bot = telebot.TeleBot('6037374947:AAEXNzxXZRH6y8q8cMrZ3gmeEUpOLb7b0WQ')


@bot.message_handler(commands=['getinfo'])
def getuser(message:telebot.types.Message):
  getuser1 = str(message.from_user.id)
  getname = str(message.from_user.first_name)
  getsecname = str(message.from_user.last_name)
  getgroup = str(message.chat.id)
  rec = 1
  #bot.reply_to(message, getuser1)
  try:
    connection = pymysql.connect(
    host=host, port=3306, user=user, password=password, database=db_name, cursorclass=pymysql.cursors.DictCursor)
    print("Login")
    try:
       with connection.cursor() as cursor:
          select_name ="SELECT * FROM users "
          cursor.execute(select_name)
          result = cursor.fetchall()
          print(result)
          for i in result:
             get_list = result[1]
             imya = get_list['name']
             grup = get_list['Группа']
             if imya == message.from_user.id :
                print("One")
                if grup == message.chat.id :
                  print("Two")
                  bot.reply_to(message, "Ви вже зареєстровані")
                else:
                  insert_query = "INSERT INTO users (name, firstname, secondname, Группа, Рек) VALUES (%s, %s, %s, %s, %s);"
                  value = ('getuser1')
                  cursor.execute(insert_query, (getuser1, getname, getsecname, getgroup, rec))
                  print('Write')
                  connection.commit()    
    finally:
       connection.close()     

  finally: print('End')



bot.infinity_polling()