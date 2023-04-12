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
import os

host = "localhost"
user = "Alex"
password = "Alex"
db_name = "Proba"

bot = telebot.TeleBot('6037374947:AAEXNzxXZRH6y8q8cMrZ3gmeEUpOLb7b0WQ')

@bot.message_handler(commands=['getchat'])
def getchat(message:telebot.types.Message):
  getchat1 = str(message.chat.id)
  bot.reply_to(message, getchat1)
  try:
    connection = pymysql.connect(
    host=host, port=3306, user=user, password=password, database=db_name, cursorclass=pymysql.cursors.DictCursor)
    print("Login")
    try:
       with connection.cursor() as cursor:
          insert_query = "INSERT INTO Шашл (pidor) VALUES (%s);"
          cursor.execute(insert_query, (getchat1))
          connection.commit()  
    
    finally:
       connection.close()     

  finally: print('Write')



@bot.message_handler(commands=['getuser'])
def getuser(message:telebot.types.Message):
  getuser1 = str(message.from_user.id)
  bot.reply_to(message, getuser1)
  try:
    connection = pymysql.connect(
    host=host, port=3306, user=user, password=password, database=db_name, cursorclass=pymysql.cursors.DictCursor)
    print("Login")
    try:
       with connection.cursor() as cursor:
          insert_query = "INSERT INTO Шашл (name) VALUES (%s);"
          cursor.execute(insert_query, (getuser1))
          connection.commit()    
    finally:
       connection.close()     

  finally: print('Write')



bot.infinity_polling()