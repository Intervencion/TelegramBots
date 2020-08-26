import telebot
from telebot import types
import time
from colorclass import Color

print(Color(
    '{autored}[{/red}{autoyellow}+{/yellow}{autored}]{/red} {autocyan} Everyone iniciado.{/cyan}'))

import sqlite3
con = sqlite3.connect('canteros.db',check_same_thread = False)
c = con.cursor()

admins = []

TOKEN = ''
bot = telebot.TeleBot(TOKEN)
hora = time.strftime("%Y-%m-%d %H:%M:%S")

def List2Str(list, separator, lastseparator):
	list_str = ''
	list_length = len(list)
	listcounter = 1

	for x in list:
		if len(list) == 1:
			list_str = str(x)
		else:
			if list_str != '' and listcounter < int(list_length):
				list_str = list_str + separator + str(x)

			if listcounter == int(list_length):
				list_str = list_str + lastseparator + str(x)

			if list_str == '':
				list_str = str(x)

			listcounter = listcounter + 1
	return list_str

def listener(messages):
	for m in messages:
		cid = m.chat.id
		uid = m.from_user.id
		uname = m.from_user.username
		mct = m.chat.title
		ufm = m.from_user.first_name
		ulm = m.from_user.last_name
		if m.text:
			mensaje = f"{{autogreen}}User:{{/green}} {ufm}\n"
			mensaje += f"{{autogreen}}Username:{{/green}} {uname}\n"
			mensaje += f"{{autoyellow}}Chat:{{/yellow}} {mct}\n"
			mensaje += f"{{autored}}Hora:{{/red}}{hora}\n"
			mensaje += f"{{autocyan}}UserID:{{/cyan}}[{uid}]"
			mensaje += f"{{autoblue}} ChatID:{{/blue}}[{cid}]"
			mensaje += "\n"
			mensaje += f"{{automagenta}}Mensaje:{{/magenta}} {m.text}\n"
			mensaje += "-------------------------------\n"
			print (Color(str(mensaje)))
			# if (m.from_user.username is None):
				# if (ulm == None):
					# uname = ufm
				# else:
					# name = f'{ufm} {ulm}'
				# try:
					# nocapital = uname.capitalize()
					# c.execute(f"INSERT INTO cid (uid,uname) VALUES ('{uid}','@{nocapital}')")
				# except:
					# print('except L60')
			# else:
				# uname = m.from_user.username
				# try:
					# c.execute(f"INSERT INTO cid (uname) VALUES ('@{nocapital}')")
				# except:
					# print('except L66')

# @bot.message_handler(commands=['create'])
# def command_create(m):
	# cid = m.chat.id
	# uid = m.from_user.id
	# if uid in admins:
		# c.execute('''CREATE TABLE Usuarios (idUsuario, ALIAS)''')
		# c.execute('''CREATE TABLE Grupo (idGrupo)''')
		# c.execute('''CREATE TABLE UsuGrupo (idUsuarioFK, idGrupoFK)''')
		# c.execute('''CREATE UNIQUE INDEX IF NOT EXISTS IDName ON Usuarios (idUsuario, ALIAS)''')
		# c.execute('''CREATE UNIQUE INDEX IF NOT EXISTS GroupID ON Grupo (idGrupo)''')
		# c.execute('''CREATE UNIQUE INDEX IF NOT EXISTS UIDCID ON UsuGrupo (idUsuarioFK, idGrupoFK)''')
		# con.commit()
		# con.close()

@bot.message_handler(commands=['eg'])
def command_eg(m):
	cid = m.chat.id
	uid = m.from_user.id
	EG = existeGrupo(cid)
	EU = existeUser(uid)
	EUG = existeUserGru(uid,cid)
	if(EG == 1):
		bot.send_message(cid, "El grupo existe en la BD", parse_mode="Markdown")
		if(EU == 1):
			bot.send_message(cid, "El user existe en la BD", parse_mode="Markdown")
			if(EUG == 1):
				bot.send_message(cid, "El user en este grupo existe en la BD", parse_mode="Markdown")
			else:
				bot.send_message(cid, "El user en este grupo NO existe en la BD", parse_mode="Markdown")
		else:
			bot.send_message(cid, "El user NO existe en la BD", parse_mode="Markdown")
	else:
		bot.send_message(cid, "El grupo NO existe en la BD", parse_mode="Markdown")

def existeGrupo(cid):
	c.execute(f"SELECT COUNT(*) FROM Grupo WHERE idGrupo ='{cid}'")
	try:
		for i in c:
			print("Vamos a ver si el select de grupo ha devuelto algún elemento")
			print(f'El resultado del select es: {i[0]}')
			EG =i[0]

	except Exception as e:
		print(e)
		print("Estamos aquí porque el select nos ha devuelto un elemento vacío")
		EG = 0

	return EG

def existeUser(uid):
	c.execute(f"SELECT COUNT(*) FROM Usuarios WHERE idUsuario ='{uid}'")
	try:
		for i in c:
			print("Vamos a ver si el select de Usuarios ha devuelto algún elemento")
			print(f"El resultado del select es: {i[0]}")
			EU =i[0]

	except Exception as e:
		print(e)
		print("Estamos aquí porque el select nos ha devuelto un elemento vacío")
		EU = 0

	return EU

def existeUserGru(uid,cid):
	c.execute(f"SELECT COUNT(*) FROM UsuGrupo WHERE idUsuarioFK ='{uid}' AND idGrupoFK ='{cid}'")
	try:
		for i in c:
			print("Vamos a ver si el select de UsuGrupo ha devuelto algún elemento")
			print(f"El resultado del select es: {i[0]}")
			EUG =i[0]

	except Exception as e:
		print(e)
		print("Estamos aquí porque el select nos ha devuelto un elemento vacío")
		EUG = 0
	print(f"Vamos a devolver el valor de EUG que es {EUG}")
	return EUG

@bot.message_handler(commands=['list'])
def command_id(m):
	cid = m.chat.id
	# uname = m.from_user.username
	# uid = m.from_user.id
	arrayl = []
	try:
		print("entro en el try")
		c.execute(f"SELECT idUsuario, ALIAS FROM Usuarios INNER JOIN UsuGrupo ON Usuarios.idUsuario = UsuGrupo.idUsuarioFK WHERE UsuGrupo.idGrupoFK ='{cid}' ORDER BY idUsuario ASC")
		print("hago el for?")
		for i in c:
			if i[1].startswith("@"):
				print("1")
				idUsuario_resultado = i[0]
				print("2)" + str(idUsuario_resultado))
				ALIAS_resultado = i[1]
				print("3)" + str(ALIAS_resultado))
				p = str(ALIAS_resultado)
				print("4" + str(p))
				arrayl.append(p)
				print("5")
			else:
				print("1")
				idUsuario_resultado = i[0]
				print("2)" + str(idUsuario_resultado))
				ALIAS_resultado = i[1]
				print("3)" + str(ALIAS_resultado))
				p = "[" + str(ALIAS_resultado) + "](tg://user?id=" + str(idUsuario_resultado) + ")"
				print("4" + str(p))
				arrayl.append(p)
				print("5")
		f = List2Str(arrayl, ', ', ' y ')
		if not f:
			f = "The DB is empty. Please add yourself with `/add`"
			print(str(f))
			bot.send_message(cid, f'{f}', parse_mode = "Markdown")
			con.commit()
		else:
			print(str(f))
			bot.send_message(cid, f'{f}', parse_mode = "Markdown")
			con.commit()
	except:
		bot.send_message(cid, "An error ocurred. Report to @Intervencion.")
		
@bot.message_handler(commands=['add'])
def command_addbtag(m):
	cid = m.chat.id
	uid = m.from_user.id
	mct = m.chat.title
	ufm = m.from_user.first_name
	ulm = m.from_user.last_name
	if (m.from_user.username is None):
		if (ulm == None):
			uname = ufm
		else:
			uname = f'{ufm} {ulm}'
	else:
		uname = "@"+m.from_user.username
	if(cid>0):
		bot.send_message(cid,"This only works in groups.")
	elif(cid<0):
		print(str(cid))
		print("VAMOS A LEERLO SIN TRY")
		try:
			print("voy a mirar si el grupo ya existe")
			EG = existeGrupo(cid)
			if (EG == 0):
				print("El Grupo no existe, ergo tengo que crearlo")
				print(m.chat.title)
				print(f"El nombre del chat es: {mct}")
				print("Ahora vamos a hacer el insert en el grupo")
				try:
					c.execute(f"INSERT INTO Grupo (idGrupo) VALUES ('{cid}')")
					print(f"El id del grupo {cid}")
					uname = uname
					nocapital = uname.capitalize()
					EU = existeUser(uid)
					if(EU == 0):
						c.execute(f"INSERT INTO Usuarios (idUsuario, ALIAS) VALUES ('{uid}','{uname}')")
					print("ESTOY DEBAJO DEL IF de ENTRE USUARIO = 0")
					c.execute(f"INSERT INTO UsuGrupo(idUsuarioFK,idGrupoFK) VALUES ('{uid}','{cid}')")
					bot.send_message(cid, f"*{uname}* has been added to the DB with User ID *{uid}*.", parse_mode="Markdown")
					con.commit()
				except sqlite3.Error as e:
					print(e)
					bot.send_message(cid, f"*{uname}* has been added to the DB with User ID *{uid}*.", parse_mode="Markdown")
			elif(EG == 1):
				print("El grupo sí existe")
				uname = uname
				nocapital = uname.capitalize()
				try:
					EU = existeUser(uid)
					if(EU == 0):
						c.execute(f"INSERT INTO Usuarios (idUsuario, ALIAS) VALUES ('{uid}','{uname}')")
					print("ESTOY DEBAJO DEL IF de ENTRE USUARIO = 0 Y AHORA VOY A COMPROBAR EUG")
					EUG = existeUserGru(uid,cid)
					print("Sabemos que EUG vale " + str(EUG))
					if(EUG == 0):
						print("Entro cuando no existe la combinación usuario - grupo")
						c.execute(f"INSERT INTO UsuGrupo(idUsuarioFK, idGrupoFK) VALUES ('{uid}','{cid}')")
						bot.send_message(cid, f"*{uname}* has been added to the DB with User ID *{uid}*.", parse_mode="Markdown")
					if(EUG == 1):
						bot.send_message(cid, "You have already introduced been added in this group.", parse_mode="Markdown")
					con.commit()
				except sqlite3.Error as e:
					print(e)
					bot.send_message(cid, "You have already introduced been added in this group.", parse_mode="Markdown")
			else:
				bot.send_message(cid, "ExceptError: The format of the command is `/add.", parse_mode="Markdown")
		except:
			bot.send_message(cid, "ExceptError: The format of the command is `/add.", parse_mode="Markdown")


bot.set_update_listener(listener)
bot.skip_pending = True
bot.polling(none_stop=True)