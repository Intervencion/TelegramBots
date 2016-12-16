
from collections import OrderedDict
import telebot
from telebot import types


TOKEN = ''
bot = telebot.TeleBot(TOKEN)

def listener(messages):
	for m in messages:
		cid = m.chat.id
		uid= m.from_user.id
		usm = m.from_user.username
		bienvenida = '.\nWIIIIIIIIIIP!'
		if m.content_type == 'text':
				print ("[@" + str(usm) + " " + str(uid) + " in " + str(cid) + "]: " + m.text)
				bot.send_message (-33694770, "[@" + str(usm) + " " + str(uid) + " in " + str(cid) + "]: " + m.text)
		if m.content_type == 'new_chat_participant':
			musm = m.new_chat_participant.username
			bot.send_message(cid, 'Welcome to One Piece Treasure Cruise,  @' + str(musm) + bienvenida)
	  
	  

@bot.message_handler(commands=['msgall'])
def command_msgall(m): 
  uid= m.from_user.id
  fecha="March. 04 _18:15(CEST)_"
  contenido="Rework of bot. Deleted all characters commands and improvement at guide and drop ones. Use @TreasureCruiseBot to search characters. Works inline too!"
  if uid == 1896312:
    bot.send_message( iditem, "Last update\n"+fecha+"\n\n*UPDATE!*\n"+contenido, parse_mode = "Markdown")




bot.set_update_listener(listener)



@bot.message_handler(commands=['start'])
def command_start(m): 
  cid = m.chat.id
  if m.text.find(" ") != -1:
  	comando = m.text.split(' ', 1)[1]
  else: # Si no, es simplemente '/start' y le enviamos el mensaje normal.
  	bot.send_message( cid, "Use /commands to see what you can do with this bot.", parse_mode = "Markdown")
  	return # Hacemos return para que salga de la función.
  if comando == 'week': # Ahora vamos comprobando los posibles comandos del deeplinking.
    command_week(m)
  if comando == 'sugo':
  	command_sugo(m)
  if comando == 'guia':
  	command_guia(m)
  if comando == 'inicio':
  	command_inicio(m)

		
@bot.message_handler(commands=['guia'])
def command_guia(m):
	cid = m.chat.id

	if cid > 0:
		bot.send_message( cid, "Guia para usar One Piece Treasure Cruise 4.0 en PC (Emulador)\n\n*1.*Primero de todo, necesitamos descargar e instalar *Virtualbox*. Para ello, vamos a [Virtual Box](https://www.virtualbox.org/wiki/Downloads) y seleccionamos nuestra plataforma en *VirtualBox platform packages*.\n\n*2.*Ahora, necesitaremos crearnos una cuenta en [Genymotion](https://goo.gl/URvJrt). (Es gratis, no preocuparse catalanes) y seleccionar *OBLIGATORIAMENTE* la versión que pone *WITHOUT VIRTUALBOX* e instalamos.\n\n*3.*Una vez instalado tanto *VirtualBox* como *Genymotion*, iniciamos Genymotion y le damos a *ADD* (Add a new virtual device).\nPara asegurarnos el tiro, seleccionaremos *Android version 5.0.0* y *Custom Phone* _(Custom Phone - 5.0.0 - API 21 - 768-1280)_.\n\n*4.*Ahora deberías poder iniciar el móvil virtual, pero quizá te pide reiniciar el PC o iniciar Genymotion como Administrador. Iniciamos pues.\n\n*5.*Necesitaremos el *ARM translation layer for Genymotion*, así que lo bajamos.\nUna vez descargado, y con el móvil virtual ejecutado, lo arrastramos a la pantalla del móvil y le damos a 'OK' cuando salga el mensaje de 'Flashear puede romper nosequénosecuantos'. Reiniciamos (móvil).\n[Aquí tenéis el link. Es un mirror muy grande, así que elegís lo que más os guste.](http://www.mirrorcreator.com/files/0ZIO8PME/Genymotion-ARM-Translation_v1.1.zip_links)\n\n*6.*Turno de instalar las 'Google Play App' (también llamadas *Gapps*). Las descargamos de aquí, [para Android 5.0.0](https://drive.google.com/file/d/0B1gsxpQPZadVVGJHampaT2FFQk0/view?usp=sharing).\n\n*7.*Hacemos lo mismo que con el *ARM* e ignoramos los errores.\nAbrimos Google Play, le damos a Update All y reiniciamos.\n\n*8.*Descargamos el [OPTC 3.0](https://drive.google.com/file/d/0B1gsxpQPZadVRE1DQjM3STU3ODQ/view?usp=sharing) y el [Root Explorer](https://drive.google.com/file/d/0B1gsxpQPZadVaHZ5eUg1WEhQYUU/view?usp=sharing)\nY los instalamos.\n\n*9.*Usaremos *Root Explorer* solamente para hacer 'rerolls' hasta conseguir unos buenos personajes iniciales en el juego. Para ello:\n\nAbres el juego y empiezas la partida, cuando acabes el tutorial, y este descargando el juego, tienes que darle rapidamente las 500 veces para conseguir las 5 frutas, en ese momento Y ANTES DE QUE TERMINE LA DESCARGA, minimizas el juego, abres root explorer, buscas el archivo *sakura.db* ```(data/data/com.namcobandaigames.spmoja010/files/documents)``` y lo copias en otra carpeta, yo te recomiendo porque es mas sencillo si le das a la pestaña de la derecha llamada downloads en el root explorer (nosotros estamos en la pestaña de la izquierda llamada documents) y lo copias ahi.\n\nLuego de copiarlo, entramos al juego, se termina la descarga y hacemos el reroll, si salió mierda, cierras el juego por completo, reinicias el root explorer y *borras el archivo sakura.db y el device.db*, *luego copias y pegas el que previamente habias apartado* en la pestaña de al lado (download).\n\nLuego abres de nuevo el juego y empezaras con los 500 toques ya pulsados, y el juego reconocera que ya esta instalado y volveras a donde tenias que entrar al correo a recoger las frutas y demas. *Asi infinitamente hasta que te salga algo decente.*\n\n*¡Y A JUGAR!*", parse_mode = "Markdown")
	else:
		bot.reply_to( m, "Clica en https://telegram.me/OnePieceTC_bot?start=guia para ver la guía para usar One Piece Treasure Cruise 3.0 en PC (Emulador)")


@bot.message_handler(commands=['inicio'])
def command_inicio(m):
	cid = m.chat.id
	if cid > 0:
		bot.send_message( cid, "*Tutorial para empezar en OPTC*\n\n*1. Comienzo*\nComenzaras con 10 gemas. Te dedicaras a hacer rerroll (mira el comando /[guia](https://telegram.me/OnePieceTC_bot?start=guia) para instrucciones detalladas) si te es posible hasta empezar al menos con un ⭐️5 estrellas.\nRecomendados *Rayleigh*, *Whitebeard* (Edward Newgate), *Log Luffy* (Monkey D. Luffy Voyage Log: Straw Hat Pirates), *Sengoku* (estos cuatro solo aparecen durante el Sugo-Fest, que es un evento de 24h mensual) o *Luffy Gear Third* (o Luffy Balloon, que evoluciona a G3).\nEl motivo es que tendras un camino mas “facil” que empezar con cualquier tipo de RR. Los RR son Rare Recruit y se realizan en la taberna.\nEn caso de no tener suerte, podemos empezar con alguno de los ⭐️5 estrellas que destaquen.\nEn PSY:\nShanks + Urouge, Marco o Rakuyo (cualquier combinación entre estos sirve)\nEn INT:\nTowel Nami (Nami Hapiness Punch) + Nico Robin, Vista, Hawkins, X Drake, Moria o Curiel (cualquier combinación entre estos sirve)\nPara STR:\nBlamenco, Arlong, Kid, Fossa o Kuma (cualquier combinación entre estos sirve, pero Arlong renta más llevarlo de capitán junto a otros _Slashers_)\nDEX:\nLaw, Apoo, Izo, Namule (recomendado Law, pero al igual que los anteriores, todos sirven)\nY para QCK:\nAce, Jozu, Killer, Xapone, Thatch o Jimbe (la mejor forma de empezar sería con Killer o Jozu, pero todo sirve)", parse_mode = "Markdown", disable_web_page_preview=True)
		bot.send_message( cid, "*2. Personajes de la historia*\nLuffy. Evoluciona a Gear Second (última evolución). Si no tienes nada mejor de capitán STR, te hará el apaño, y tampoco es malo en stats.\nZoro. De los mejores Slashers. Lo evolucionas a [Roronoa Zoro Three Thousand Worlds](http://i.imgur.com/maCKBfX.jpg) y luego a [Ashura](http://i.imgur.com/ngg8xmD.jpg). No es mal capitán DEX para empezar.\nUsopp. Te salvará la vida en muchísimas ocasiones, pero solo si lo evolucionas a [Golden Pound Usopp](http://i.imgur.com/UebnOX1.jpg) Y NO LO TOCAS DE AHÍ. Recomendado subirlo al MAX (lvl50).\nSanji. Psé. Te hace el apaño si no tienes nada mejor, tanto de Damage Dealer como de Capitán. Se evoluciona al [Sanji de LVL35](http://i.imgur.com/ml7b0vf.jpg) y luego al [Sanji Diable](http://i.imgur.com/RHFmteq.jpg).\nNami. Se evoluciona a [Mirage Tempo](http://i.imgur.com/ANcJ5GW.jpg) y se deja quietecita. Recomendado subirla hasta el max (lvl50).\nChopper. Provocó SIDA a Freddy Mercury. [Se evoluciona al DEX si no tenemos a Smoker y si no al STR o QCK](http://i.imgur.com/qK5SEDU.jpg).", parse_mode = "Markdown", disable_web_page_preview=True)
		bot.send_message( cid, "*3. Personajes dropeables recomendados de la historia*\nAquí recomendamos personajes que deberias ir sacando a lo largo del juego. Sólo intentaremos sacarlo cuando en su isla haya DROPX2 (mayor probabilidad de que salga).\n-*Alvida´s Hideout:* Conseguir (o farmear) a *Alvida*. Su evolución se usa como reductor de daño en muchas fases. Será necesaria para muchas cosas.	\n-*Shell Town:* Farmear a *Morgan*. Slasher rojo con gran daño y bueno para montar el equipo rojo para empezar (si tenemos a Arlong ni os molesteis en sacar a Morgan).\n-*Orange Town:* Farmear a *Buggy*. Slasher INT que evoluciona a bajo nivel y si no tienes nada mejor no es mal capitán INT para empezar.\n-*Syrup Village:* Farmear a *Kuro*. Va de Slashers la cosa. Este es QCK.\n-*Baratie:* Puedes farmear a *Zeff*. Fighter que se puede usar de capitán y hacer un apaño decente.\n-*Arlong park:* Farmear *SI O SI  a ARLONG*. Slasher STR de los que más daño tienen. Es un DD (damage dealer) muy importante. Debes tenerlo. Es buen capitán Slasher. MUST.\n-*Loguetown:* Farmear a *Smoker*. DEX y reductor de daño que con Zoro forman buena composición.\n_Todos estos tienen una isla extra. Así que si no los tienes cuando salga su isla extra deberás sacarlos._\n-*Nanohana/Alubarna:* Farmear *SI O SI a CROCODILE*. Slasher morado con dos evoluciones, striker y slasher. Otros que puedes farmear *MR1* (Slasher rojo), *MR2* (PSY, hace combo con GARP), *MR3* (Slasher INT con buen especial)\n-*Jaya:* Puedes farmear a *Bellamy*. Boost de orbes.\n-*Arc Maxim:* Farmear a *Eneru*. Gran capitán PSY, con bastante daño. Buen PSY. Puedes farmear también a *Wiper* (Capitán Shooter mientras no salga Zephyr).", parse_mode = "Markdown", disable_web_page_preview=True)
		bot.send_message( cid, "*4. Barcos*\nDurante la historia te irán dando todo tipo de barcos. Estos se maxean con colas.\n-*Dinghy* Primer barco que tendrás. Te obligarán a subirlo 1 o 2 veces. NO SUBIR MÁS. Es INUTIL.\n- *Miss Lovey DuckyClear:* Te lo darán después de hacer todas las misiones de Alvida. NO MAXEAR.\n- *Merry Go:* Te lo darán después de pasarte Syrup Village. NECESARIO. Es el primero que tendrás que maxear.\n- *Marine BoatClear Story:* Te lo darán después de pasarte Shells Town. NO MAXEAR. No tenemos capitán shooter actualmente decente. -Baratie. Te lo darán después de pasarte el Baratie. NO MAXEAR.\n- *Coffin Mihawks:* Te lo dan después de pasarte el bosque de mihawk. MAXEAR.\n- *Flying MerryClear Story:* Te lo dan después de pasarte Jaya. NO MAXEAR", parse_mode = "Markdown", disable_web_page_preview=True)
	else:
		bot.reply_to( m, "Clica en https://telegram.me/OnePieceTC_bot?start=inicio para ver el Tutorial para empezar en OPTC")







grupo = -20432512
	
#def command_week(m):
#	cid = m.chat.id
#	bot.send_message( cid, "This week on One Piece Treasure Cruise...\n*~The Feast of Pirates~*\nNov. 24 _00:00 (PST)_ Nov. 24 _09:00 (CEST)_\nDec. 7 _23:59 (PST)_ Dec. 8 _08:59 (CEST)_\n'Tis the season for plenty, and you'll have the chance to get plenty of drops on *Upper Yard ~ Ark Maxim* with double the drop rate! You'll be sure to Recruit plenty of characters for your crew!\n\n*Thak like a Pirate!*\nNov. 24 _00:00 (PST)_ Nov. 24 _09:00 (CEST)_\nNov. 26 _17:59 (PST)_ Nov. 27 _02:59 (CEST)_\nLike the Facebook page during this part of the event, and win fabolous prizes!\nThe more likes we get, the biger the bounty of prizes to go around!\n\n*New island!*\n*New Area: Upperd Yard ~ Ark Maxim*\nStarting Nov. 24 _(19:00 PST)_ // Nov. 25 _(04:00)_\n*Upper Yard - Ark Maxim avaible!*\n\n*Drop x2*\nA cornucopia of drops!\nNov. 24 _00:00 (PST)_ Nov. 24 _09:00 (CEST)_\nNov. 30 _23:59 (PST)_ Dec. 1 _08:59 (CEST)_\n\n*Sugo!*\nSee /sugo for detailed info!\n\n*High up!*\nSee /highup for detailed info!\n\n*Warriors of Shandia! Dreams of a Homeland! Fortnight* appears! And *Franky - Pervert's Aesthetic! Fortnight* is back!\nSee /fortnight for detailed info!\n\n*New ranking!*\nNew ranking for *Franky - Pervert's Aesthetic! Fortnight*\nNov. 24 _19:00 (PST)_ Nov. 25 _04:00 (CEST)_\nDec. 1 _18:59 (PST)_ Dec. 2 _03:59 (CEST)_\n*[Ranking Adventure]*\nPervert Aesthetic - Pervert\n*[Ranking Title]*\nFran-king! *SUPER* Damage!\n*[Ranking Conditions]*\nYour score will be the highest amount of damage dealt to enemies in a single turn during one playthrough of *Pervert Aesthetic - Pervert*.\n\n*Turtles and barrel breaking*\nSee /ids for detailed info!", parse_mode = "Markdown")

@bot.message_handler(commands=['week'])	
def command_week(m):
	cid = m.chat.id
	if cid > 0:
		bot.send_message( cid, "This week on *One Piece Treasure Cruise*...\n*~The Feast of Pirates~*\nNov. 24 _00:00 (PST)_ Nov. 24 _09:00 (CEST)_\nDec. 7 _23:59 (PST)_ Dec. 8 _08:59 (CEST)_\nJoin us at the table!\n\n*High up!*\n*❤️STR fortnight*. See /highup for detailed info!\n\n*Bountiful Turtles!*\n_Dec. 1, Dec. 3, Dec. 5, Dec. 6 (PST)_\nDuring this part of the event, you'll have four certain opportunities to catch almost every color of turtle there is! Choose your moment and get a short chance to catch all the turtles you can manage, for as long as your time and Stamina hold out!\n*[IMPORTANT]*\n·Choose your own start time.\n·Even if you have time remaining, the quest will close at _23:59 (PST)_ // _08:59 (CEST)_\n·The quest may close immediately or shortly after being selected if your device time has been changed. Please confirm your device time is correct before playing.\n\n*Clash of Clashes*\n_Dec. 2 - Dec. 8 (PST)_\nThe Clash of Clashes is back for the holidays, and all during this part of the event, *Rampaging Chopper*, *Garp*, and *Ivankov* will be stopping by to join in the *Feast of Pirates*! Don't miss this chance to Recruit this powerful characters!\n*Chopper:*\nDec. 02 _19:00 (PST)_ Dec. 3 _04:00 (CEST)_\nDec. 3 _18:59 (PST)_ Dec. 4 _03:59 (CEST)_\n*Garp:*\nDec. 04 _19:00 (PST)_ Dec. 5 _04:00 (CEST)_\nDec. 5 _18:59 (PST)_ Dec. 6 _03:59 (CEST)_\n*Ivankov:*\nDec. 07 _19:00 (PST)_ Dec. 8 _04:00 (CEST)_\nDec. 8 _18:59 (PST)_ Dec. 9 _03:59 (CEST)_\n\n*Turtles and barrel breaking*\nSee /ids for detailed info!", parse_mode = "Markdown")
		bot.send_message( cid, "*Next* week on *One Piece Treasure Cruise*...\n*Sugo-Fest!?*\nLeaked the next *Sugo-Fest!*\nDec. 8 _19:00 (PST)_ Dec. 9 _04:00 (CEST)_\nDec. 10 _18:59 (PST)_ Dec. 11 _03:59 (CEST)_\n*48 Hours Only!*\nThe most powerful characters around have gathered together for *Sugo-Fest!*! For 48 hours, you'll have a higher chance of Recruiting them for your crew!\nNot only that, but this time, every rate-boosted *Sugo-Fest* character will join your crew *at level 50*! Anyone you Recruit will be able to hit the ground running!\nSee /sugo for detailed info!\n*Bonds of Friendship*\nDec. 8 _00:00 (PST)_ Dec. 9 _09:00 (CEST)_\nDec. 21 _23:59 (PST)_ Dec. 22 _08:59 (CEST)_\nStrength in Friendship!\n\n*1.* *Rainbow Gem Giveaway!*\nDec. 8 _00:00 (PST)_ Dec. 9 _09:00 (CEST)_\nDec. 21 _23:59 (PST)_ Dec. 22 _08:59 (CEST)_\n\n*2.* *Double Drop Rate*\nDec. 8 _00:00 (PST)_ Dec. 9 _09:00 (CEST)_\nDec. 14 _23:59 (PST)_ Dec. 15 _08:59 (CEST)_\nFriendship enriches, and our *Bonds of Friendship* event will enrich you with twice the drops on *Weekly Quests* all during this part onf the event!\n\n*3.* *Boosters and Evolvers come to Friend Point Recruit!*\nDec. 15 _00:00 (PST)_ Dec. 16 _09:00 (CEST)_\nDec. 21 _23:59 (PST)_ Dec. 22 _08:59 (CEST)_\nFriend Points go farther than ever! During this part of the event, you'll have the chance to get *Boosters* and *Evolvers* every time you use *Friend Point Recruit*!\n\n*4.* *New characters!*\nDec. 8 _00:00 (PST)_ Dec. 9 _09:00 (CEST)_\nDuring this part of the event, you'll be able to Recruit an all new bunch of freidns to help and support your quest to be *King of the Pirates*!\n*Rare Recruit* (⭐️3)\nBellmere\nKaya\nNojiko\nCrocus\nHotori and Kotori\n*Rare Recruit* (⭐️4)\nBellmere Nami and Nojiko's Mother\nKaya A rich young girl from Syrup Village.\nNojiko Nami's Sister\nCrocus Twin Cape Lighthouse Keeper\nHotori and Kotori Skypiea Vice Head Enforcers\n*Friend Point Recruit* (⭐️2)\nHiking Bear\nPurinpurin\n\n*5.* *Restaurant Le Crap, Forest Branch!* *Returns!*\nDec. 15 _00:00 (PST)_ Dec. 16 _09:00 (CEST)_\nDec. 21 _23:59 (PST)_ Dec. 22 _08:59 (CEST)_\nWhat better than to enjoy a meal at a fine restaurant with your friends? Well, luckily for you, in this part of the event, *Restaurant Le Crap* is returning to *Extra Island*, and you and your friends will have the chance to feast on *Cola* and *Cotton Candy* when it does!\nYou never know when *Restaurant Le Crap* will be opening it's doors, so keep your eyes out!\n*·*Wanted posters will NOT drop during this quest.\n*·*The restaurant will appear a few time during this portion of the event, and you'll be able to play each difficulty once whenever it does.\n\n*New Ranking!* Avaible Soon!\nNew ranking for *Deep Sea Kraken Fortnight*\nDec. 8 _19:00 (PST)_ Dec. 9 _04:00 (CEST)_\nDec. 15 _18:59 (PST)_ Dec. 16 _03:59 (CEST)_\nCompete with your friends!\n*[Ranking Adventure]*\nVs Deep-Sea Kraken: Midnight Zone\n*[Ranking Title]*\nChallenge the Creatures of the Deep!\n*[Ranking Conditions]*\nIn the *Extra Island* quest, *VS Deep-Sea Kraken: Midnight Zone*, aim for the *High Score*, which will be based on a combination of crew cost, turns taken, and tap accuracy.\n*·*Details on how the *High Score* is calculated will not be released.\n\n*High up!*\n*❤️STR fortnight*. See /highup for detailed info!\n\n*New Missions Avaible!*\nDec. 8 _19:00 (PST)_ Dec. 9 _04:00 (CEST)_\nNew Missions Avaible!\nMessenger Bats have come to Shells Town bearing Missions!\n*·New Missions:* Stop the Navy's Tyranny! Clearing each mission will net you a different reward, and clearing every mission will unlock an extra story scene!\n\n*Supersonic Duck Squadron Fortnight* appears!\nDec. 8 _19:00 (PST)_ Dec. 9 _04:00 (CEST)_\nDec. 22 _18:59 (PST)_ Dec. 23 _03:59 (CEST)_\nThe *Supersonic Duck Squadron* is conducting their special training exercises on Extra Island! This is your chance to Recruit the Squad's seven members, including their leader, Karoo!\nSee /fortnight and /duck\_fort for more info!\n\n*Deep Sea Kraken Fortnight* is back!\nDec. 8 _19:00 (PST)_ Dec. 9 _04:00 (CEST)_\nDec. 15 _18:59 (PST)_ Dec. 16 _03:59 (CEST)_\nSee /fortnight and /kraken\_fort for more info!", parse_mode = "Markdown")
	else:
		bot.reply_to( m, "Click on https://telegram.me/OnePieceTC_bot?start=week to see what's next this week.")
	
@bot.message_handler(commands=['printids'])
def command_printids(m):
	cid = m.chat.id

	bot.send_message( cid, str(ids).strip('[]'), parse_mode = "Markdown")


@bot.message_handler(commands=['commands'])
def command_commands(m):
	cid = m.chat.id

	bot.send_message( cid,"/24h - Next 24h raid boss in CEST & PST\n/commands - Displays the current active commands\n/crews - Show all crew groups\n/highup - Show the 'higher chance...' schedule for Type, EXP and Skillbook\n/ids - Show turtle and barrel schedule for specific IDs\n/fortlist - Show all Fortnights\n/fortnight - Show all Fortnights schedule (active and next)\n/materials - Extra material's Isle schedule\n/raid - Show all Raids\n/version - Show character bot progress\n/sugo - Show next Sugo-fest!\n/week - This week on One Piece Treasure Cruise... (BEWARE! Walltext is real)")

@bot.message_handler(commands=['24h'])
def command_24h(m): 
	cid = m.chat.id

	bot.send_message( cid, "*Clash!! Rampaging Chopper!*\nWednesday December 2nd at 19:00(PST)\nThursday December 3rd at 04:00(CEST)\n\n*Clash!! Garp!*\nFriday December 4th at 19:00(PST)\nSaturday December 5th at 04:00(CEST)\n\n*Clash!! Invankov!*\nSunday December 6th at 19:00(PST)\nMonday December 7th at 04:00(CEST)", parse_mode = "Markdown")

@bot.message_handler(commands=['materials'])
def command_materials(m): 
	cid = m.chat.id

	bot.send_message( cid, "*Monday:* Turtles\n*Tuesday:* Seahorses\n*Wednesday:* Penguins\n*Thursday:* White Striped Dragons\n*Friday:* Armored Crabs & Hermits (+Lobsters in JP)\n*Weekend:* El Dorado", parse_mode = "Markdown")

@bot.message_handler(commands=['sugo'])
def command_sugo(m): 
	cid = m.chat.id

	if cid > 0:
		bot.send_message( cid, "Last sugo was\n*Sugo-Fest!* New voiced Characters!\n\nThursday *November 26* at _19:00(PST)_\nFriday *November 27* at _04:00(CEST)_\n*24 HOURS ONLY!*\n\n*New character:*\n\n🌟5\nMonkey D. Luffy Voyage Log: Straw Hat Pirates (Log) _(STR)_ *NEW!*\nSengoku _(PSY)_\nBoa Hancock _(QCK)_\nSilvers Rayleigh _(INT)_\nEdward Newgate _(STR)_\n\n*Plus, you'll have a higher chance of Recruiting all the powerful characters listed below!*\n\n\n⭐️5\nNami Voyage Dream: World Map (Log) _(INT)_\nUsopp Voyage Dream: Brave Sea Warrior (Log) _(QCK)_\nBrook Voyage Dream: Promised Meeting (Log) _(DEX)_\nCaptain Kid _(STR)_\nRoar of the Sea Scratchman Apoo _(DEX)_\nCapone 'Gang' Bege _(QCK)_\nBlamenco the Ballet _(STR)_\nFlower Sword Vista _(INT)_\nMarco the Phoenix _(PSY)_\nNico Robin _(INT)_\nRed-Haired Shanks _(PSY)_\nPortgas D. Ace Flame Mirror _(QCK)_\n\n\n⭐️4\nNami Voyage Log: Straw Hat Pirates (Log) _(INT)_\nUsopp Voyage Log: Straw Hat Pirates (Log) _(QCK)_\nBrook Log: Straw Hat Pirates (Log) _(DEX)_\nEustass Kid _(STR)_\nScratchman Apoo _(DEX)_\nCapone Bege _(QCK)_\nBlamenco _(STR)_\nVista _(INT)_\nMarco _(PSY)_\nMiss All Sunday Baroque Works Vice Prese _(INT)_\nShanks _(PSY)_\nPortgas D. Ace _(QCK)_", parse_mode = "Markdown")
		bot.send_message( cid, "Next sugo is\n*Sugo-Fest!* *48 hours!* ~Join my crew!~\n*Sugo-Fest* characters start at *Level 50!*\n\nTuesday *December 8* at _19:00(PST)_\nWednesday *December 9* at _04:00(CEST)_\n*48 HOURS ONLY!*\nThe most powerful characters around have gathered together for *Sugo-Fest!*! For 48 hours, you'll have a higher chance of Recruiting them for your crew!\nNot only that, but this time, every rate-boosted *Sugo-Fest* character will join your crew *at level 50*! Anyone you Recruit will be able to hit the ground running!\n\n*Sugo-Fest Exclusive Characters:*\n\n🌟5\nMonkey D. Luffy Voyage Log: Straw Hat Pirates (Log) _(STR)_\nSengoku _(PSY)_\nBoa Hancock _(QCK)_\nSilvers Rayleigh _(INT)_\nEdward Newgate _(STR)_\n\n*Plus, you'll have a higher chance of Recruiting all the powerful characters listed below!*\n\n\n⭐️5\nJimbe Warlord of the Sea _(QCK)_\nBartholomew Kuma Warlord of the Sea _(STR)_\nGecko Moria Warlord of the Sea _(INT)_\nFlintlock Pistols Izo _(DEX)_\nMorning Star Rakuyo _(PSY)_\nTrafalgar Law ROOM _(DEX)_\nBepo the Martial Artist _(STR)_\nRed Flag X Drake _(INT)_\nMad Monk Urouge _(PSY)_\nMassacre Soldier Killer _(QCK)_\n\n\n⭐️4\nJimbe _(QCK)_\nBartholomew Kuma _(STR)_\nGecko Moria _(INT)_\nIzo _(DEX)_\nRakuyo _(PSY)_\nTrafalgar Law _(DEX)_\nBepo _(STR)_\nX Drake _(INT)_\nUrouge _(PSY)_\nKiller _(QCK)_\n\n*·**Sugo-Fest Exclusive* characters and *Sugo-Fest* rate-boosted characters are guaranteed to start at *LV 50!*\n*·**STR*-type characters are guaranteed to start at *LV 20!*", parse_mode = "Markdown")
	else:
		bot.reply_to( m, "Next sugo is\n*Sugo-Fest!* *48 hours!* ~Join my crew!~\n*Sugo-Fest* characters start at *Level 50!*\n\nTuesday *December 8* at _19:00(PST)_\nWednesday *December 9* at _04:00(CEST)_\n\nClick on [https://telegram.me/OnePieceTC_bot?start=sugo](https://telegram.me/OnePieceTC_bot?start=sugo) to see more info!", parse_mode = "Markdown")
		
@bot.message_handler(commands=['highup'])
def command_highup(m): 
	cid = m.chat.id

	bot.send_message( cid, "*Sugo*\n/sugo - Show what's new at the Sugo-Fest and when!\n\n*High chance Rare Recruit*\nHigher Chance of getting *❤️STR* characters\nDec. 1 _19:00(PST)_ Dec. 2 _04:00(CEST)_\nDec. 15 _18:59(PST)_ Dec. 16 _03:95(CEST)_\n\n*Skill UP*\nHigh chance of getting a *SKill up*\nNov. 24 _19:00(PST)_ Nov. 25 _04:00(CEST)_\nDec. 1 _18:59(PST)_ Dec. 2 _18:59(CEST)_", parse_mode = "Markdown")
	
	
@bot.message_handler(commands=['ids'])
def command_ids(m): 
	cid = m.chat.id

	bot.send_message( cid,"/id0_5 - Show next and current schedule for Turtle and Barrel Breaking for ID 0 and 5\n/id1_6 - Show next and current schedule for Turtle and Barrel Breaking for ID 1 and 6\n/id2_7 - Show next and current schedule for Turtle and Barrel Breaking for ID 2 and 7\n/id3_8 - Show next and current schedule for Turtle and Barrel Breaking for ID 3 and 8\n/id4_9 - Show next and current schedule for Turtle and Barrel Breaking for ID 4 and 9\n\nSince this command is still in development, check http://cyung.github.io/optc/index.html for your timezone schedule.")
	


@bot.message_handler(commands=['id0_5'])
def command_id0_5(m): 
	cid = m.chat.id 

	bot.send_message( cid,"*Turtles*\n\n*First batch*\nMonday *November 30* at _14:00(CEST)_\n\n*Second batch*\nTuesday *December 01* at _00:00(CEST)_\n\n\n*Barrel Breaking*\nNov. 30 _13:00(CEST) - Nov. 31 12:59(CEST)_", parse_mode = "Markdown")
	
@bot.message_handler(commands=['id1_6'])
def command_id1_6(m): 
	cid = m.chat.id

	bot.send_message( cid,"*Turtles*\n\n*First batch*\nMonday *November 30* at _16:00(CEST)_\n\n*Second batch*\nTuesday *December 01* at _02:00(CEST)_\n\n\n*Barrel Breaking*\nNov. 29 _13:00(CEST) - Nov. 30 12:59(CEST)_", parse_mode = "Markdown")
	
@bot.message_handler(commands=['id2_7'])
def command_id2_7(m): 
	cid = m.chat.id 

	bot.send_message( cid,"*Turtles*\n\n*First batch*\nMonday *November 30* at _18:00(CEST)_\n\n*Second batch*\nTuesday *December 01* at _04:00(CEST)_\n\n\n*Barrel Breaking*\nDec. 03 _13:00(CEST) - Dec. 04 12:59(CEST)_", parse_mode = "Markdown")
	
@bot.message_handler(commands=['id3_8'])
def command_id3_8(m): 
	cid = m.chat.id 

	bot.send_message( cid,"*Turtles*\n\n*First batch*\nMonday *November 30* at _20:00(CEST)_\n\n*Second batch*\nTuesday *December 01* at _06:00(CEST)_\n\n\n*Barrel Breaking*\nDec. 02 _13:00(CEST) - Dec. 03 12:59(CEST)_", parse_mode = "Markdown")
	
@bot.message_handler(commands=['id4_9'])
def command_id4_9(m): 
	cid = m.chat.id 

	bot.send_message( cid,"*Turtles*\n\n*First batch*\nMonday *November 30* at _22:00(CEST)_\n\n*Second batch*\nTuesday *December 01* at _08:00(CEST)_\n\n\n*Barrel Breaking*\nDec. 01 _13:00(CEST) - Dec. 02 12:59(CEST)_", parse_mode = "Markdown")
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
#CREWS COMMANDS CREWS COMMANDS#
@bot.message_handler(commands=['crews'])
def command_crews(m): 
	cid = m.chat.id 

	bot.send_message( cid,"/mugiwara_crew - show all Mugiwara's crew commands\n/navy - Show all Navy's crew commands\n/buggy_crew - Show all Buggy's crew commands\n/cp9 - Show all CP9's members\n/blackbeard_crew - Show all Blackbeard's crew\n/baratie_crew - Show all Baratie's crew\n/donkrieg_crew - Show all Don Kriegs's crew")  

@bot.message_handler(commands=['mugiwara_crew'])
def command_mugiwara_crew(m): 
	cid = m.chat.id 

	bot.send_message( cid,"/optcluffy - Show all Luffy commands \n/optczoro - Show all Zoro commands \n/optcnami - Show all Nami commands\n/optcusopp - Show all Usopp commands\n/optcsanji - Show all Sanji commands\n/optcchopper - show all Chopper commands\n/optcbrook - Show all Brook commands")  

@bot.message_handler(commands=['buggy_crew'])
def command_buggy_crew(m): 
	cid = m.chat.id 

	bot.send_message( cid,"/mohji - Mohji & Richie\n/cabaji - Cabaji the Acrobat\n/optcbuggy - Show all Buggy commands\n/optcalvida - Show all Avida commands")

@bot.message_handler(commands=['kuro_crew'])
def command_kuro_crew(m): 
	cid = m.chat.id 

	bot.send_message( cid,"/siam - Siam\n/butchie - Butchie\n/optcdjango - Show all Django commands\n/optckuro - Show all Kuro commands")

@bot.message_handler(commands=['baratie_crew'])
def command_baratie_crew(m): 
	cid = m.chat.id
	bot.send_message( cid,"/patty - Patty\n/carne - Carne\n/zeff - Chef Zeff")	

@bot.message_handler(commands=['donkrieg_crew'])
def command_donkrieg_crew(m):
	cid = m.chat.id 
	bot.send_message( cid,"/optcgin - Show all Gin commands\n/optcpearl - Show all Pearl commands\n/optckrieg - Show all Don Krieg commands")	

@bot.message_handler(commands=['arlong_crew'])
def command_arlong_crew(m):
	cid = m.chat.id 
	bot.send_message( cid,"/momoo - Momoo\n/choo - Choo\n/kuroobi - Kuroobi\n/optchatchan - Show all Hatchan commands\n/optcarlong - Show all Arlong commands")	

@bot.message_handler(commands=['navy'])
def command_navy(m): 
	cid = m.chat.id 

	bot.send_message( cid,"/optccoby - Show all Coby commands\n/opctmeppo - Show all Helmeppo commands\n/optcmorgan - Show all Morgan commands\n/nezumi - Nezumi\n/optctashigi - Show all Tashigi commands\n/optcsmoker - Show all Smoker commands")  

@bot.message_handler(commands=['cp9'])
def command_cp9(m): 
	cid = m.chat.id

	bot.send_message( cid,"/lulu - Lulu\n/optckaku - Show all Kaku commands\n/optclucci - Show all Lucci commands")

@bot.message_handler(commands=['blackbeard_crew'])
def command_blackbeard_crew(m): 
	cid = m.chat.id 
	bot.send_message( cid,"/optcblackbeard - Show all Blackbeard commands")
	
@bot.message_handler(commands=['whitebeard_crew'])
def command_evobeard_crew(m): 
	cid = m.chat.id 
	bot.send_message( cid,"/optcthatch - Show all Thatch commands")


	
	
	
	
	
	
	
	
#OPTCPJs COMMANDS LOG OPTCPJs COMMANDS#
@bot.message_handler(commands=['optclog'])
def command_optclog(m): 
	cid = m.chat.id

	bot.send_message( cid,"/luffy_log - Monkey D. Luffy Voyage Log: Straw Hat Pirates (Log)\n/luffy_log2 - Monkey D. Luffy Voyage Dream: Pirate King (Log)\n/zoro_log - Roronoa Zoro Voyage Log: Straw Hat Pirates (Log)\n/zoro_log2 - Roronoa Zoro Voyage Dream: Strongest Swordsman (Log)\n/chopper_log - Tony Tony Chopper Voyage Log: Straw Hat Pirates (Log)\n/chopper_log2 - Tony Tony Chopper Voyage Dream: Great Doctor (Log)\n/sanji_log - Sanji Voyage Log: Straw Hat Pirates (Log)\n/sanji_log2 - Sanji Voyage Dream: All Blue (Log)\n/brook_log - Brook Voyage Log: Straw Hat Pirates (Log)\n/brook_log2 - Brook Voyage Dream: Promised Meeting (Log)\n/nami_log - Nami Voyage Log: Straw Hat Pirates (Log)\n/nami_log2 - Nami Voyage Dream: World Map (Log)\n/usopp_log - Usopp Voyage Log: Straw Hat Pirates (Log)\n/usopp_log2 - Usopp Voyage Dream: Brave Sea Warrior (Log)\n/nico_log - Nico Robin Voyage Log: Straw Hat Pirates (Log)\n/nico_log2 - Nico Robin Voyage Dream: 100-Year Void (Log)\n/franky_log - Franky Voyage Log: Straw Hat Pirates (Log)\n/franky_log2 - Franky Voyage Dream: A Ship to Sail Around the World (Log)") 
	
	

	
	
	
	
	

#OPTCPJs COMMANDS MUGIWARA OPTCPJs COMMANDS#
@bot.message_handler(commands=['optcluffy'])
def command_optcluffy(m): 
	cid = m.chat.id 
	bot.send_message( cid,"/luffy - Monkey D. Luffy\n/luffy_pistol - Monkey D. Luffy Gum-Gum Pistol\n/luffy_bazooka - Monkey D. Luffy Gum-Gum Bazooka\n/luffy_g2 - Monkey D. Luffy Gear 2\n/luffyv2 - Monkey D. Luffy Gum-Gum Balloon\n/luffy\_g3 - Monkey D. Luffy Gear Third\n/luffy_log - Monkey D. Luffy Voyage Log: Straw Hat Pirates (Log)\n/luffy_log2 - Monkey D. Luffy Voyage Dream: Pirate King (Log)") 	

@bot.message_handler(commands=['optczoro'])
def command_optczoro(m): 
	cid = m.chat.id 
	bot.send_message( cid,"/zoro - Roronoa Zoro\n/zoro_3000worlds - Roronoa Zoro Three Thousand Worlds\n/zoro_pound - Roronoa Zoro Pound Phoenix\n/zoro_ashura - Roronoa Zoro Ashura Ichibugin\n/zorov2 - Roronoa Zoro Streaming Wolf Swords\n/zorov2_evo - Roronoa Zoro Lion's Song\n/zoro_log - Roronoa Zoro Voyage Log: Straw Hat Pirates (Log)\n/zoro_log2 - Roronoa Zoro Voyage Dream: Strongest Swordsman (Log)")  

@bot.message_handler(commands=['optcnami'])
def command_optcnami(m): 
	cid = m.chat.id 
	bot.send_message( cid,"/nami - Nami\n/nami_tornado - Nami Tornado Tempo\n/nami_mirage -  Nami Mirage Tempo\n/nami_thunderbolt - Nami Thunderbolt Tempo\n/namiv2 - Nami Fine Tempo\n/tnami - Nami Happiness Punch\n/nami_log - Nami Voyage Log: Straw Hat Pirates (Log)\n/nami_log2 - Nami Voyage Dream: World Map (Log)")  

@bot.message_handler(commands=['optcusopp'])
def command_optcusopp(m): 
	cid = m.chat.id 
	bot.send_message( cid,"/usopp - Usopp\n/usopp_tabasco - Usopp Tabasco Star\n/usopp_golden - Usopp Golden Pound (GPU)\n/sogeking - Sogeking\n/usopp_log - Usopp Voyage Log: Straw Hat Pirates (Log)\n/usopp_log2 - Usopp Voyage Dream: Brave Sea Warrior (Log)")

@bot.message_handler(commands=['optcsanji'])
def command_optcsanji(m): 
	cid = m.chat.id 
	bot.send_message( cid,"/sanji - Sanji\n/sanji_surgery - Sanji Plastic Surgery Shot\n/sanji_chef - Chef Sanji Hot Rock Stew\n/sanji_diable - Sanji Diable Jambe Flambe\n/sanji_log - Sanji Voyage Log: Straw Hat Pirates (Log)\n/sanji_log2 - Sanji Voyage Dream: All Blue (Log)")  

@bot.message_handler(commands=['optcchopper'])
def command_optcchopper(m): 
	cid = m.chat.id 
	bot.send_message( cid,"/chopper - Tony Tony Chopper\n/chopper_heavy - Tony Tony Chopper Heavy Point\n/chopper_brain - Tony Tony Chopper Brain Point\n/chopper_arm - Tony Tony Chopper Arm Point\n/chopper_horn - Tony Tony Chopper Horn Point\n/chopper_guard - Tony Tony Chopper Guard Point\n/chopper_log - Tony Tony Chopper Voyage Log: Straw Hat Pirates (Log)\n/chopper_log2 - Tony Tony Chopper Voyage Dream: Great Doctor (Log)")  

#@bot.message_handler(commands=['optcrobin'])
#def command_optcusopp(m): 
#	cid = m.chat.id 
#	bot.send_message( cid,"/usopp - Usopp\n/usopp_tabasco - Usopp Tabasco Star\n/usopp_golden - Usopp Golden Pound (GPU)\n/sogeking - Sogeking\n/nico_log - Nico Robin Voyage Log: Straw Hat Pirates (Log)\n/nico_log2 - Nico Robin Voyage Dream: 100-Year Void (Log)")

#@bot.message_handler(commands=['optcfranky'])
#def command_optcusopp(m): 
#	cid = m.chat.id 
#	bot.send_message( cid,"/usopp - Usopp\n/usopp_tabasco - Usopp Tabasco Star\n/usopp_golden - Usopp Golden Pound (GPU)\n/sogeking - Sogeking\n/franky_log - Franky Voyage Log: Straw Hat Pirates (Log)\n/franky_log2 - Franky Voyage Dream: A Ship to Sail Around the World (Log)")	

@bot.message_handler(commands=['optcbrook'])
def command_optcbrook(m): 
	cid = m.chat.id 
	bot.send_message( cid,"/brook - Brook\n/brook_evo - Humming Swordsman Brook\n/brook_log - Brook Voyage Log: Straw Hat Pirates (Log)\n/brook_log2 - Brook Voyage Dream: Promised Meeting (Log)")

	
	
	
	
	
	
	
	
	
	
	

#OPTCPJs COMMANDS BUGGY OPTCPJs COMMANDS#
@bot.message_handler(commands=['optcbuggy'])
def command_optcbuggy(m): 
	cid = m.chat.id 
	bot.send_message( cid,"/buggy - Buggy\n/buggy_evo - Buggy the Clown")
@bot.message_handler(commands=['optcalvida'])
def command_optcalvida(m): 
	cid = m.chat.id 
	bot.send_message( cid,"/alvida - Iron-Mace Alvida\n/alvida_evo- Iron-Mace Alvida Smooth-Smooth Fruit")
#OPTCPJs COMMANDS KURO OPTCPJs COMMANDS#
@bot.message_handler(commands=['optcdjango'])
def command_optcdjango(m): 
	cid = m.chat.id 
	bot.send_message( cid,"/django - One-Two Django\n/django_evo - Dancing Django\n/django_double - Double Crosser Django")
@bot.message_handler(commands=['optckuro'])
def command_optckuro(m): 
	cid = m.chat.id 
	bot.send_message( cid,"/kuro - Captain Kuro\n/kuro_evo - Kuro of a Hundred Plans")
	
	
	
	
	
	
#OPTCPJs COMMANDS DON KRIEG OPTCPJs COMMANDS#
@bot.message_handler(commands=['optcgin'])
def command_optcgin(m): 
	cid = m.chat.id 
	bot.send_message( cid,"/gin - Gin\n/gin_evo - Gin the Man-Demon")
@bot.message_handler(commands=['optcpearl'])
def command_optcpearl(m): 
	cid = m.chat.id 
	bot.send_message( cid,"/pearl - Pearl\n/pearl_evo - Fire Pearl")
@bot.message_handler(commands=['optckrieg'])
def command_optckrieg(m): 
	cid = m.chat.id 
	bot.send_message( cid,"/krieg - Don Krieg\n/krieg_evo - Don Krieg Poison Gas Bomb MH5")

#OPTCPJs COMMANDS ARLONG OPTCPJs COMMANDS#
@bot.message_handler(commands=['optchatchan'])
def command_optchatchan(m):
	cid = m.chat.id 
	bot.send_message( cid,"/hatchan - Hatchan\n/hatchan_evo - Six-Sword Hachi")	
@bot.message_handler(commands=['optcarlong'])
def command_optcarlong(m):
	cid = m.chat.id 
	bot.send_message( cid,"/arlong - Arlong\n/arlong_evo - Enraged Arlong Shark On Tooth")	


	
	
	
	
	
	

#OPTCPJs COMMANDS BAROQUEWORKS OPTCPJs COMMANDS#
@bot.message_handler(commands=['optcmr9'])
def command_optcmr9(m):
	cid = m.chat.id 
	bot.send_message( cid,"/mr9 - Mr. 9\n/mr9_evo - Mr. 9 Hot Blooded Bat")	
	
@bot.message_handler(commands=['optcmr8'])
def command_optcmr8(m):
	cid = m.chat.id 
	bot.send_message( cid,"/mr8 - Mr. 8\n/mr8_iga - Mr. 8 Igarappapa")	
	
@bot.message_handler(commands=['optcmr5'])
def command_optcmr5(m):
	cid = m.chat.id 
	bot.send_message( cid,"/mr5 - Mr. 5 Nez-Palm Cannon\n/mr5_evo - Mr. 5 Breeze Breath Bomb")	
	
@bot.message_handler(commands=['optcmr4'])
def command_optcmr4(m):
	cid = m.chat.id 
	bot.send_message( cid,"/mr4 - Mr. 4\n/mr4_dog - Mr. 4 and Lassoo the Dog-Gun")		
	
@bot.message_handler(commands=['optcmr3'])
def command_optcmr3(m):
	cid = m.chat.id 
	bot.send_message( cid,"/mr3 - Mr. 3\n/mr3_evo - Mr. 3 Extra Special Candelabra\n/mr3_criminal - Criminal Galdino Mr. 3")

#-------------------------# 
	
@bot.message_handler(commands=['optcmissvalentine'])
def command_optcmissvalentine(m):
	cid = m.chat.id 
	bot.send_message( cid,"/missvalentine - Miss Valentine\n/missvalentine_evo - Miss Valentine 10,000 Kilo Guillotine")	
	
@bot.message_handler(commands=['optcmissgoldenweek'])
def command_optcmissgoldenweek(m):
	cid = m.chat.id 
	bot.send_message( cid,"/missgoldenweek - Miss Goldenweek\n/missgoldenweek_evo - Miss Goldenweek Colors Trap: Calming Green")	
	
@bot.message_handler(commands=['optcmisssunday'])
def command_optcmisssunday(m):
	cid = m.chat.id 
	bot.send_message( cid,"/misssunday - Miss All Sunday Baroque Works VP\n/nico_robin - Nico Robin")	
	
@bot.message_handler(commands=['optcmissmonday'])
def command_optcmissmonday(m):
	cid = m.chat.id 
	bot.send_message( cid,"/missmonday - Miss Monday\n/missmonday_superhuman - Miss Monday Superhuman Brass Knuckles")		
	
@bot.message_handler(commands=['optcmisschristmas'])
def command_optcmisschristmas(m):
	cid = m.chat.id 
	bot.send_message( cid,"/misschristmas - Miss Merry Christmas\n/misschristmas_mole - Miss Merry Christmas Human Mole")
	
@bot.message_handler(commands=['optcmissdoublefinger'])
def command_optcmissdoublefinger(m):
	cid = m.chat.id 
	bot.send_message( cid,"/missdoublefinger - Miss Doublefinger\n/missdoublefinger_spike - Miss Doublefinger Human Spike")






@bot.message_handler(commands=['optcmr2'])
def command_optcmr2(m):
	cid = m.chat.id 
	bot.send_message( cid,"/mr2 - Mr. 2 Bon Clay\n/mr2_evo - Mr. 2 Bon Clay Bombardier Arabesque\n/mr2_fugitive - Fugitive Bentham Mr. 2 Bon Clay\n/mr2_prison - Prison Break Expert Mr. 2 Bon Clay\n/mr2_log - Mr. 2 Bon Clay Voyage Log: B.W. (Log)\n/mr2_log_2 - Mr. 2 Bon Clay Voyage Dream: Okama Way (Log)")

@bot.message_handler(commands=['optcmr1'])
def command_optcmr1(m):
	cid = m.chat.id 
	bot.send_message( cid,"/mr1 - Mr. 1\n/mr1_sword - Mr. 1 Human Sword\n/mr1_prisoner - Prisoner Daz Bonez Mr. 1")

@bot.message_handler(commands=['optccrocodile'])
def command_optccrocodile(m):
	cid = m.chat.id 
	bot.send_message( cid,"/mr0 - Mr. 0 Baroque Works CEO (Crocodile)\n/crocodile - Sir Crocodile\n/crocodile_evo - Sir Crocodile Warlord of the Sea\n/crocodile_prisoner - The Strongest Prisoner, Sir Crocodile Mr. 0, Former CEO of Baroque Works\n/crocodile_prisoner_evo - The Strongest Prisoner, Sir Crocodile Warlord of the Sea\n/crocodile_logia - Sir Crocodile Logia Warlord of the Sea\n/crocodile_logia_2 - Sir Crocodile Logia Former Warlord of the Sea")	
	
	
	
	
	
	
	
	
	
	
	
#OPTCPJs COMMANDS ARABASTA OPTCPJs COMMANDS#
@bot.message_handler(commands=['arabasta_crew'])
def command_arabasta_crew(m):
	cid = m.chat.id

	bot.send_message( cid,"/test - test\n/test - test")	

	
	
	
	
	
	
	
#OPTCPJs COMMANDS SHANKS OPTCPJs COMMANDS#
@bot.message_handler(commands=['optcshanks'])
def command_optcshanks(m):
	cid = m.chat.id 
	bot.send_message( cid,"/shanks - Shanks\n/shanks_evo - Red-Haired Shanks\n/shanks_sw - Shanks, Black Clothes and Red Hair (SW)\n/shanks_sw2 - Shanks, The Black-Clothed Yonkou (SW)\n/shanks_pirates - Shanks the Pirate Apprentice\n/shanks_pirates2 - Shanks of the Roger Pirates")	

	
	
	
	
	
#OPTCPJs COMMANDS NAVY OPTCPJs COMMANDS#
@bot.message_handler(commands=['optccoby'])
def command_optccoby(m): 
	cid = m.chat.id 
	bot.send_message( cid,"/coby - Coby\n/coby_cabin - Cabin Boy Coby")
@bot.message_handler(commands=['optchelmeppo'])
def command_optchelmeppo(m): 
	cid = m.chat.id 
	bot.send_message( cid,"/helmeppo - Helmeppo\n/helmeppo_cabin - Cabin Boy Helmeppo")
@bot.message_handler(commands=['optcmorgan'])
def command_optcmorgan(m): 
	cid = m.chat.id 
	bot.send_message( cid,"/morgan - Axe-Hand Morgan\n/morgan_evo - Escapee Morgan")
@bot.message_handler(commands=['optctashigi'])
def command_optctashigi(m): 
	cid = m.chat.id 
	bot.send_message( cid,"/tashigi - Tashigi\n/tashigi_evo - Tashigi Navy HQ Ensign")
@bot.message_handler(commands=['optcsmoker'])
def command_optcsmoker(m): 
	cid = m.chat.id 
	bot.send_message( cid,"/smoker - Smoker\n/smoker_evo - Smoker the White Hunter/smoker_bike - White Chase Smoker")

	

	





#OPTCPJs COMMANDS CP9 OPTCPJs COMMANDS#
@bot.message_handler(commands=['optckaku'])
def command_optckaku(m): 
	cid = m.chat.id 
	bot.send_message( cid,"/kaku - Kaku\n/kaku_evo - Kaku Dock One Carpentry Specialist")
@bot.message_handler(commands=['optclucci'])
def command_optclucci(m): 
	cid = m.chat.id 
	bot.send_message( cid,"/lucci - Rob Lucci\n/lucci_evo - Rob Lucci Dock One Sawyer, Treenail Specialist")








#OPTCPJs COMMANDS KUROHIGE OPTCPJs COMMANDS#
@bot.message_handler(commands=['optcblackbeard'])
def command_optcblackbeard(m): 
	cid = m.chat.id 
	bot.send_message( cid,"/teach - Marshall D. Teach\n/blackbeard - Blackbeard")

	
	
#OPTCPJs COMMANDS WHITEBEARD OPTCPJs COMMANDS#
@bot.message_handler(commands=['optcthatch'])
def command_optcthatch(m): 
	cid = m.chat.id 
	bot.send_message( cid,"/thatch - Thatch\n/thatch_evo - Twin-Blade Thatch")	



#OPTCPJs COMMANDS BEASTS OPTCPJs COMMANDS#
@bot.message_handler(commands=['beasts'])
def command_beasts(m): 
	cid = m.chat.id

	bot.send_message( cid,"/master_near - Master of the Near Sea\n/momoo - Momoo")

	

	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	


#FORTNIGHT COMMANDS - FORTNIGHT COMMANDS#
@bot.message_handler(commands=['fortnight'])
def command_fortnight(m): 
	cid = m.chat.id

	bot.send_message( cid,"/shandia\_fort\n*Warriors of Shandia! Dreams of a Homeland! Fortnight*\nNov. 24 _19:00 (PST)_ Nov. 25 _04:00 (CEST)_\nDec. 8 _18:59 (PST)_ Dec. 9 _03:59 (CEST)_\n\n/tsuru\_fort\n*Tsuru's Morning Stroll Fortnight*\nDec. 1 _18:00 (PST)_ Dec. 2 _04:00 (CEST)_\nDec. 8 _18:59 (PST)_ Dec. 9 _03:59 (CEST)_", parse_mode = "Markdown")
 
@bot.message_handler(commands=['fortlist'])
def command_fort(m): 
	cid = m.chat.id

	bot.send_message( cid,"/tsuru\_fort - List of dropeable characters at *Tsuru's Morning Stroll Fortnight*\n/smoker\_fort - List of dropeable characters at *Smoker's Great Pursuit Fortnight*\n/lucci\_fort - List of dropeable characters at *Lucci's Artisan Spirit Fortnight*\n/brook\_fort - List of dropeable characters at *Adrift!? Humming Brook Fortnight*\n/shandia\_fort - List of dropeable characters at *Warriors of Shandia! Dreams of a Homeland! Fortnight*\n/franky\_fort - List of dropeable characters at *Franky - Pervert's Aesthetic! Fortnight*", parse_mode = "Markdown")
 
@bot.message_handler(commands=['smoker_fort'])
def command_smoker_fort(m): 
	cid = m.chat.id
	
	bot.send_message( cid,"/smoker - Smoker\n/tashigi - Tashigi")

@bot.message_handler(commands=['tsuru_fort'])
def command_tsuru_fort(m): 
	cid = m.chat.id
	
	bot.send_message( cid,"*Characters Drop*\n/tsuru - Tsuru\n/momonga - Momonga\n/onigumo - Onigumo\n\n*Manual Drop*\n/mr5 - [Mr. 5 Nez-Palm Cannon](http://optc.github.io/characters/#/view/199) - *Nez-Palm Cannon* _(11 turns maxed)_\n/mr5\_evo [Mr. 5 Breeze Breath Bomb](http://optc.github.io/characters/#/view/200) - *Breeze Breath Bomb* _(14 turns maxed)_\n/missvalentine\_evo - [Miss Valentine 10,000 Kilo Guillotine](http://optc.github.io/characters/#/view/202) - *10,000 Kill-O-Guillotine* _(6 turns maxed)_\n/luffy\_g3 - [Monkey D. Luffy Gear Third](http://optc.github.io/characters/#/view/217) - *Gum-Gum Giant Rifle* _(20 turns maxed)_\n/usoppv2\_evo - [Usopp Impact](http://optc.github.io/characters/#/view/223) - *Impact* _(12 turns maxed)_\n/mr8\_evo - [Mr. 8 Igarappapa](http://optc.github.io/characters/#/view/234) - *Igarappapa* _(8 turns maxed)_\n/missmonday\_evo - [Miss Monday Superhuman Brass Knuckles](http://optc.github.io/characters/#/view/236) - *Superhuman Brass Knuckles* _(11 turns maxed)_\n\n*Guides*\n[Spanish guide](http://treasure-cruise.blogspot.com/p/guia-otsuru-paradise.html)\n[English guide](http://op-tc-eng-version.blogspot.com.au/2015/06/fortnight-island-tsurus-morning-stroll.html)", parse_mode = "Markdown", disable_web_page_preview=True)
	


	

@bot.message_handler(commands=['lucci_fort'])
def command_lucci_fort(m): 
	cid = m.chat.id
	
	bot.send_message( cid,"/lucci - Rob Luccin/kaku - Kaku\n/lulu - Lulu")
 
@bot.message_handler(commands=['franky_fort'])
def command_franky_fort(m): 
	cid = m.chat.id
	
	bot.send_message( cid,"*Characters Drop*\n/franky - Franky\n/kiwi - Kiwi\n/mozu - Mozu\n\n*Manual Drop*\n/tashigi\_evo - [Tashigi Navy HQ Ensign](http://optc.github.io/characters/#/view/68) - *Quick Draw* _(18 turns maxed)_\n/shanks\_evo [Red-Haired Shanks](http://optc.github.io/characters/#/view/077) - *Conqueror's Haki* _(20 turns maxed)_\n/usoppv2 - [Usopp Usopp Hammer](http://optc.github.io/characters/#/view/222) - *Usopp Hammer* _(8 turns maxed)_\nvista\_evo - [Flower Sword Vista](http://optc.github.io/characters/#/view/255) - *Rose Rondo* _(10 turns maxed)_\n/kiwi - [Kiwi](http://optc.github.io/characters/#/view/338) - *Wavy Square Hair* _(6 turns maxed)_\n/mozu - [Mozu](http://optc.github.io/characters/#/view/339) - *Straight Square Hair* _(6 turns maxed)_\n\n*Guides*\n[Spanish guide](http://treasure-cruise.blogspot.com/2015/11/cyborg-franky-perverts-aesthetic.html)\n[English guide](http://op-tc-eng-version.blogspot.com.au/2015/07/franky-fortnight-isle.html)", parse_mode = "Markdown", disable_web_page_preview=True)






@bot.message_handler(commands=['kraken_fort'])
def command_kraken_fort(m): 
	cid = m.chat.id

	bot.send_message( cid,"*Characters Drop*\n/master\_near - Master of the Near Sea\n/gaimon - Gaimon\n/momoo - Momoo\n/laboon - Laboon\n/squid - Neptunian Squid\n/kraken - Kraken Surume\n\n*Manual Drop*\n/django\_evo - [Dancing Django](http://optc.github.io/characters/#/view/44) - *Dance Heaven* _(7 turns maxed)_\n/misswednesday - [Miss Wednesday](http://optc.github.io/characters/#/view/71) - *Enchanting Vertigo Dance* _(10 turns maxed)_\n/laboon\_evo - [Laboon (Luffy's drawing)](http://optc.github.io/characters/#/view/214) - *Sorrowful Charge* _(15 turns maxed)_\n/izo\_evo - [Flintlock Pistols Izo](http://optc.github.io/characters/#/view/257) - *Beautiful Dual Flintlocks* _(10 turns maxed)_\n/whitebeard - [Whitebeard](http://optc.github.io/characters/#/view/261) - *Seaquake* _(17 turns maxed)_\n/unluckies - [Mr. 13 & Ms. Friday The Unluckies](http://optc.github.io/characters/#/view/290) - *Judgment Bomb* _(18 turns maxed)_\n/dorry - [Dorry](http://optc.github.io/characters/#/view/291) - *[RCV] Slot Storm* _(8 turns maxed)_\n/broggy - [Broggy](http://optc.github.io/characters/#/view/292) - *[RCV] Slot Storm* _(8 turns maxed)_\n\n*Guides*\n[Spanish guide](http://treasure-cruise.blogspot.com/p/guia-kraken-face-deep-sea.html)\n[English guide](http://optc-guide.com/2015/03/05/return-of-sea-monsters-attack/)", parse_mode = "Markdown", disable_web_page_preview=True)


	
	
	
	
@bot.message_handler(commands=['brook_fort'])
def command_brook_fort(m): 
	cid = m.chat.id

	bot.send_message( cid,"/brook - Brook\n/ryuma - Ryuma")  

	
	
	

	
	
@bot.message_handler(commands=['duck_fort'])
def command_duck_fort(m): 
	cid = m.chat.id

	bot.send_message( cid,"*Characters Drop*	\n/unluckies - Mr. 13 & Ms. Friday The Unluckies	\n/triceratops - Triceratops\n/rex - Rex\n/brontosaurus - Brontosaurus\n/lapin - Lapin\n/dugong - Kung Fu Dugong\n/banana\_gator - Banana Gator\n/sandora\_dragon - Sandora Dragon\n/cowboy\_bourbon - Cowboy & Bourbon Jr. - Super Spot-Billed Duck Squad\n/stomp\_ivan - Stomp & Ivan X. - Super Spot-Billed Duck Squad\n/kentauros\_hikoichi - Kentauros & Hikoichi - Super Spot-Billed Duck Squad\n/carue - Carue\n\n*Manual Drop*\n/usopp\_golden - [Usopp Golden Pound](http://optc.github.io/characters/#/view/15) - *Usopp Golden Pound* _(10 turns maxed)_\n/vivi\_evo - [Princess Vivi](http://optc.github.io/characters/#/view/73) - *Charge! Supersonic Duck Squadron!* _(6 turns maxed)_\n/marco\_evo - [Marco the Phoenix](http://optc.github.io/characters/#/view/251) - *Blue Flame Rebirth* _(20 turns maxed)_\n/bonney\_evo - [Big Eater Jewelry Bonney](http://optc.github.io/characters/#/view/363) - *Big Eater* _(8 turns maxed)_\n[Giant Slasher Red Pirates](http://optc.github.io/characters/#/view/368) - *Crystal Shield DEX* _(12 turns maxed)_\n/sea\_cat - [Sea Cat](http://optc.github.io/characters/#/view/378) - *Quick Healing* _(5 turns maxed)_\n\n*Guides*\n[Spanish guide (not yet)](WIP)\n[English guide](http://optc-guide.com/2015/02/24/special-training-super-duck-squad/)", parse_mode = "Markdown", disable_web_page_preview=True)
	
	
@bot.message_handler(commands=['shandia_fort'])
def command_shandia_fort(m): 
	cid = m.chat.id

	bot.send_message( cid,"*Characters Drop*\n/genbou - Genbou\n/kamakiri - Kamakiri\n/raki - Raki\n/aisa - Aisa\n\n*Manual Drop*\n/dorry - [Dorry](http://optc.github.io/characters/#/view/291) - *[RCV] Slot Storm* _(8 turns maxed)_\n/urouge\_evo - [Mad Monk Urouge](http://optc.github.io/characters/#/view/314) - *Karmic Punishment* _(18 turns maxed)_\n/lapin\_evo - [Lapin Adult](http://optc.github.io/characters/#/view/335) - *Light Healing* _(8 turns maxed)_\n[Giant Fighter Yellow Pirates](http://optc.github.io/characters/#/view/371) - *Crystal Shield INT* _(12 turns maxed)_\n/kuma\_evo - [Bartholomew Kuma Warlord of the Sea](http://optc.github.io/characters/#/view/412) - *Ursa Shock* _(14 turns maxed)_\n/braham - [Braham](http://optc.github.io/characters/#/view/466) - *Double Flash Gun* _(10 turns maxed)_\n/wiper\_evo - [Wiper, Descendant of the Great Calgara](http://optc.github.io/characters/#/view/544) - *Reject Dial* _(20 turns maxed)_\n/aisa - [Aisa](http://optc.github.io/characters/#/view/584) - *Mantra* _(8 turns maxed)_\n\n*Guides*\n[Spanish guide](http://treasure-cruise.blogspot.com/2015/11/guia-warriors-of-shandia-dreams-of.html)\n[English guide](http://optc-guide.com/2015/05/19/encounter-skypeia-warriors/)", parse_mode = "Markdown", disable_web_page_preview=True)
 
	
	
	
@bot.message_handler(commands=['eloy'])
def command_eloy(m): 
	cid = m.chat.id

	bot.send_message( cid,"[￰￰](http://i.imgur.com/PcZmxPr.jpg)\n*Name:* [Eloy](https://telegram.me/E_XIII)\n\n*Details*\n*Class:*               Follastats\n*Type:*               💜INT\n*Stars:*              ⭐️⭐️⭐️⭐️⭐️\n*Cost:*                50\n*Combo:*           4\n*Slots:*               0\n*Max LVL:*        99\n*EXP to MAX:*  3\n\n*Stats*\n*Level            1              99*\n*HP*                42           3.000\n*ATK*              15           1.400\n*RCV*              8             150\n\n*Abilities*\n*Captain:* *Paint Artisan*\n_All the members of the crew get a christmas hat_\n\n*Special:*\n*Pay The RR, First Warning*\n_Cuts 30% of current HP to those who owe a RR_\n*CD:* 288 turns *Maxed:* 17 turns", parse_mode = "Markdown")
	
	
	
	
	
	
	
#RAID COMMANDS - RAID COMMANDS#
@bot.message_handler(commands=['raid'])
def command_raid(m): 
	cid = m.chat.id

	bot.send_message( cid,"/blackbeard\_raid - List of dropeable characters at *Blackbeard Raid*", parse_mode = "Markdown")
 
@bot.message_handler(commands=['blackbeard_raid'])
def command_blackbeard_raid(m): 
	cid = m.chat.id 
	bot.send_message( cid,"*Characters Drop*\n/teach - Marshall D. Teach\n\n*Guides*\n[Spanish guide](http://treasure-cruise.blogspot.com/p/guia-kurohige.html)\n[English guide](http://op-tc-eng-version.blogspot.de/2015/11/clash-blackbeard.html)", parse_mode = "Markdown", disable_web_page_preview=True)
   
	

#############################################






	
bot.skip_pending = True	
bot.polling(none_stop=True)