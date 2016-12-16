# -*- coding: utf-8 -*-
from collections import OrderedDict
import telebot
from telebot import types


TOKEN = ''

bot = telebot.TeleBot(TOKEN)

bienvenida = "Paga el RR, hijo de puta moroso"


optc = {
  "angi":"`¿Guardia Civil dígame?`",
  "algoritmo":"Existe un algoritmo trasero y puedo demostrarlo.\n`no afecta a cuentas llevadas por féminas`",
  "eloy":"Renegados sean Foxy, Buggy y Hogback, The INTrinity\nAh, no, que ahora tengo un Sengoku de mierda 🙃",
  "nikito":"Es hora de sacar el Eloy que todos llevamos dentro jaja",
  "#rr":"Se debe yolo de entrada:\n@Jrbryant\n@franwp",
  "adri":"ROBIIIIIIIN SIIIIIIIIIIIU\n*ha abandonado el grupo*",
  "z":"NEVER FORGET",
  "zephyr":"NEVER FORGET",
  "te lo juro":"_Al Señor tu Dios temerás, a él le servirás, por su nombre jurarás_",
  "laboon":"Otro gilipollas con laboon evo al max",
  "angi angi no mi'":"*Solonen*, `[11.01.16 03:36]`\nEs la fruta de la pedofilia?",
  "eloy eloy no mi":'*NikitoNipongo*, `[11.01.16 09:20]`\n"Da los poderes de Luis Piedrahita, sacar fuerza de las cosas pequeñas."',
  "jan jan no mi":'*NikitoNipongo*, `[11.01.16 09:36]`\n"Te convierte en un hombre-mujer, con rabo pero con la capacidad de hablar sin parar puto spammer."',
  "masa":"`Masamune está dormido. No se moverá.`\n\n¡Bien! ¡Me ha salido WB! *lo tira*",
  "masamune":"*Sergi Rusi*, `[22.01.16 13:29]`\nMasamune y los refills perdidos - proximamente en los mejores cines",
  "broquil broquil no mi":"*NikitoNipongo*, `[11.01.16 13:10]`\nEl usuario tiene la capacidad de hacer aparecer magos que salven la situación.",
  "borsalino":"Borsalino puto amo.",
  "telafo?":"Angi detected, ciberpolicía en camino.",
  "primo de masa":"Se viene predicción.",
  "rr":"Fijo que pulleo a tu madre.",
  "®®":"Fijo que pulleo a tu madre.",
  "puto amo":"Adjetivo de Borsalino",
  "blog":"http://optc-esp.blogspot.com.es/",
  "traka":"Gambas al ajillo.",
  "eseneno":"shirorororororo",
  "neno":"shirorororororo",
  "sugo":"Tentación, tentación.",
  "digimon":"*Broquil*, `[30.01.16 21:57]`\nEloy con suerte en RR? ese juego no puede ser bueno",
  "#asperger":'*Mike*, `[18.01.16 22:56]`\nQue coño  es eso de asperge\n*Jan "Intervención" Raven*, `[18.01.16 22:56]`\n_[Respondiendo a Mike]_\nAlgo que tienen los asperger\n*DarkRubius .M 💋*, `[18.01.16 22:57]`\nproblemas con aspersores\n*Marcos*, `[18.01.16 22:57]`\naspergores\n*Masamune*, `[18.01.16 22:57]`\n(aspersand)',
  "mike":"Vaya pacto cutre, solo incluye RR''\n\n\nEl especial de Nami es mejor",
  "dias":"*Masamune*, `[07.02.16 15:23]`\nDía 300 seguimos sin gpu maxeado, día 400 marco sigue sin farmear a doblededo\n*Jan \"Intervención\" Raven*, `[07.02.16 15:24]`\nDia 500: Sigo sin tener levels decentes de box\n*Eloy*, `[07.02.16 15:24]`\nDia 600: Rikirt saca finalmente su segundo croco",
  "días":"*Masamune*, `[07.02.16 15:23]`\nDía 300 seguimos sin gpu maxeado, día 400 marco sigue sin farmear a doblededo\n*Jan \"Intervención\" Raven*, `[07.02.16 15:24]`\nDia 500: Sigo sin tener levels decentes de box\n*Eloy*, `[07.02.16 15:24]`\nDia 600: Rikirt saca finalmente su segundo croco",
  "blasfemia":"Joder!",
  "broquil":"Broquil, no te RAYes",
  "foxy":"Foxy no puede sustituir ni a la niña paralítica",
  "rod rod no mi":"*aDri*, `[24.02.16 19:43]`\nPullea gods en idiomas foraneos",
  "jordan jordan no mi":"*NikitoNipongo*, `[24.02.16 19:43]`\nTras 25 Log Luffy's, adivina, otro Log Luffy.",
  "jan":"Follapíxeles",
  "tenrubyto":"1 tenrubyto = 8 ternubits",
  "manga":"[Únete a este grupo para hablar de One Piece a ritmo de Manga (solo miembros del OPTC).](https://telegram.me/joinchat/ABzveD3IZthqcpthceekqw)",
  "spoiler":"[Únete a este grupo para hablar de One Piece a ritmo de Manga (solo miembros del OPTC).](https://telegram.me/joinchat/ABzveD3IZthqcpthceekqw)",  
  }



def listener(messages):
	for m in messages:
		cid = m.chat.id
		name = m.from_user.first_name
		if m.text:
			@bot.message_handler(func=lambda m: "free spirit" in m.text.lower())
			def freespirit(m):
				uid= m.from_user.id
				bot.reply_to(m, "¿Tu madre te daba polonio de pequeño?",parse_mode="Markdown")
			@bot.message_handler(func=lambda m: "freedom" in m.text.lower())
			def freedom(m):
				uid= m.from_user.id
				bot.reply_to(m, "¿Juegas al Japo?",parse_mode="Markdown")    
			@bot.message_handler(func=lambda m: "pan gratis" in m.text.lower())
			def b(m):
				uid= m.from_user.id
				if uid == 50504:
					bot.reply_to(m, "Más anime en http://telegram.me/TeConPastas. *Té con Pastas*, donde la calidad importa.",parse_mode="Markdown")
			@bot.message_handler(func=lambda m: m.text.lower() == "rod")
			def c(m):
				cid = m.chat.id
				file = open('/home/jan/bots/rod.mp4', 'rb')
				#if cid == -20432512:
				bot.send_video(cid,file)    
			@bot.message_handler(func=lambda m: m.text.lower() == "garp")
			def d(m):
				cid = m.chat.id
				file = open('/home/jan/bots/Garp.mp4', 'rb')
				#if cid == -20432512:
				bot.send_document(cid,file)										
			@bot.message_handler(func=lambda m: "es pan" in m.text.lower())
			def a(m):
				uid= m.from_user.id
				if uid == 50504:
					bot.reply_to(m, "Más anime en http://telegram.me/TeConPastas. *Té con Pastas*, donde la calidad importa.",parse_mode="Markdown")
			if m.text.lower() in optc:
					bot.reply_to(m, optc[m.text.lower()], parse_mode="Markdown")
			if m.content_type == 'new_chat_participant':
				musm = m.new_chat_participant.username
				bot.send_message(cid, "Paga el RR @" + str(musm) + " hijo de puta moroso")




@bot.message_handler(commands=['dict'])
def command_dict(m):
  cid = m.chat.id
  bot.send_message(cid, '<a href="http://hastebin.com/ehogecojem.hs">Lista de trigers</a>', parse_mode="HTML", disable_web_page_preview=True)

  
@bot.message_handler(commands=['buscador'])
def command_buscador(m):
  cid = m.chat.id
  file = open('/home/jan/bots/Buscador.png', 'rb')
  bot.send_photo(cid,file)
   
@bot.message_handler(commands=['sockets'])
def command_sockets(m):
  cid = m.chat.id
  bot.send_message(cid, "https://www.reddit.com/r/OnePieceTC/comments/43b7a9/sockets_a_guide_on_what_to_get_and_look_for/\n\nhttp://op-tc-eng-version.blogspot.com.au/2016/01/version-40-update.html\n\nhttp://treasure-cruise.blogspot.com/2016/02/la-biblia-de-los-sockets_3.html#more")
	
	
bot.set_update_listener(listener)




#@bot.message_handler(commands=['jurar'])
#def command_echo(m): 
#	cid = m.chat.id 
#        bot.reply_to(m,'Me cago en tu puta estampa, @Rodnarok', parse_mode="Markdown")
	



#############################################

 
bot.skip_pending = True	
bot.polling(none_stop=True)