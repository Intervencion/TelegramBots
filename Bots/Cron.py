import schedule
import time
import telebot
from telebot import types
TOKEN = '400135511:AAHz_-Cu94ooLPRHW9qnzzOGBGSEMVV_61I'
bot = telebot.TeleBot(TOKEN)
admins = [1896312]
try:
	bot.send_message(admins[0], "Cron ha sido encendido")
except Exception as e:
	bot.send_message(admins[0], str(e))
def EXP1():
	bot.send_message(-1001149927976, "@masamune19 @intervencion EXP Quest")
def EXP2():
	bot.send_message(-1001149927976, "@masamune19 @intervencion EXP Quest")
def EXP3():
	bot.send_message(-1001149927976, "@masamune19 @intervencion EXP Quest")
def EXP4():
	bot.send_message(-1001149927976, "@masamune19 @intervencion EXP Quest")
schedule.every().day.at("09:00").do(EXP1)
schedule.every().day.at("14:00").do(EXP2)
schedule.every().day.at("22:00").do(EXP3)
schedule.every().day.at("01:00").do(EXP4)
while True:
	schedule.run_pending()
	time.sleep(1)
