
import telebot
from telebot import types
import sys


TOKEN = ''

bot = telebot.TeleBot(TOKEN)

  
  
def listener(messages):
	for m in messages:
		cid = m.chat.id
		uid= m.from_user.id
		usm = m.from_user.username
		if m.content_type == 'text':
			print ("[" + "@" + str(usm) + " " + str(uid) + " in " + str(cid) + "]: " + m.text)
		if m.chat.id == -1001032739882:
			if m.content_type == 'text':
					bot.send_message( "@TeConPastas" ,m.text, parse_mode = "Markdown", disable_web_page_preview=True)
		if m.chat.id == -112387007:
			if m.content_type == 'text':
					bot.send_message( "@TCP_SNK" ,m.text, parse_mode = "Markdown", disable_web_page_preview=True)
		if m.chat.id == 11448177:
			if m.content_type == 'text':
						bot.send_message(1001032739882)
		if m.chat.id == 1896312:
			if m.content_type == 'text':
						bot.send_message( -1001032739882 ,m.text, parse_mode = "Markdown", disable_web_page_preview=True)
		if m.chat.id == 8978818:
			if m.content_type == 'text':
						bot.send_message( -1001032739882 ,m.text, parse_mode = "Markdown", disable_web_page_preview=True)
						
bot.set_update_listener(listener)


#############################################

 
bot.skip_pending = True		
bot.polling(none_stop=True)