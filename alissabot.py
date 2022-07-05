from edamino import Bot, Context
from edamino.objects import *
import requests
import json
import sqlite3
import random
import time

bot = Bot('asterixyt@yahoo.com', 'Volcan1000', '!')

premiums = ["fc83578c-706a-44ef-bc2a-e2c119f2fe92"]
cards = ["YoongiFUT.png", "JennieFUT.png", "JisooFUT.png", "JinsoulFUT.png", "LisaFUT.png", "HeejinFUT.png", "JypFUT.png", "SmFUT.png", "KarinaFUT.png", "NingningFUT.png", "RoseFUT.png", "YgFUT.png", "XiaotingFUT.png", "ClFUT.png", "BahiyyihFUT.png", "JuyeonFUT.png", "PsyFUT.png"]

@bot.command("ping")
async def on_ping(ctx: Context):
	await ctx.reply('Pong!')

@bot.command("hola")
async def on_hola(ctx: Context):
	await ctx.reply("Hola que tal estas?, yo muy bien ^^")

#@bot.event([api.MessageType.GROUP_MEMBER_JOIN])
#async def on_miembro_unido(ctx: Context):
#	await ctx.send(ctx.msg.author.nickname + ", bienvenido a nuestro chat uwu, mi nombre es Alissa y estoy para servirte.")

@bot.command("sh")
async def on_superheroe(ctx: Context):
	manteca = ctx.msg.content[5:30]
	res = requests.get("https://www.superheroapi.com/api.php/1282131145540058/search/" + manteca)
	data = res.json()
	img = data["results"][0]["image"]["url"]
	imagen = await ctx.download_from_link(img)
	await ctx.send_image(imagen)
	print(ctx.msg.author.nickname + " invoco a un super heroe." + ctx.msg.author.uid)

@bot.command("registrarme")
async def on_registro(ctx: Context):
	nombre = ctx.msg.author.nickname
	contrasena = ctx.msg.author.uid
	conexion = sqlite3.connect("aminodb.db")
	cursor = conexion.cursor()
	cursor.execute("INSERT INTO usuarios VALUES (?,?)",(nombre, contrasena))
	conexion.commit()
	conexion.close()
	await ctx.reply("Registrad@ correctamente :)")

@bot.command("miembros")
async def on_miembros(ctx: Context):
	if ctx.msg.author.uid == "fc83578c-706a-44ef-bc2a-e2c119f2fe92":
		conex = sqlite3.connect("aminodb.db")
		curzor = conex.cursor()
		curzor.execute("SELECT * FROM usuarios")
		user = curzor.fetchall()
		member = " ".join(map(str, user))
		await ctx.send(member)
		conex.close()
	else:
		await ctx.reply("No tiene el permiso necesario.")

@bot.command("pokedex")
async def on_pokedex(ctx: Context):
	olaf = ctx.msg.content[9:20]
	poke = requests.get("https://pokeapi.co/api/v2/pokemon/" + olaf)
	dex = poke.json()
	sprite = dex["sprites"]["front_default"]
	pokemon = await ctx.download_from_link(sprite)
	await ctx.send_image(pokemon)

@bot.command("abrazar")
async def on_abrazo(ctx: Context):
	pana = ctx.msg.content[10:30]
	await ctx.send("[I]" + ctx.msg.author.nickname + " le dio un abrazo rompe costillas a " + pana + " uwu")
	print("Abrazo de " + ctx.msg.author.nickname + " a " + pana)


@bot.command("descargar")
async def on_song(ctx: Context):
	mulan = str(ctx.msg.content[28:40])
	url = "https://youtube-mp36.p.rapidapi.com/dl"
	querystring = {"id":mulan}
	headers = {
		"X-RapidAPI-Key": "082395124cmsh8f011e89c74584fp1b5c87jsn52b9ca1173b4",
		"X-RapidAPI-Host": "youtube-mp36.p.rapidapi.com"
	}
	response = requests.request("GET", url, headers=headers, params=querystring)
	bromin = response.json()
	daka = bromin["link"]
	if str(ctx.msg.author.uid) in premiums:
		await ctx.send(str(daka))
	else:
		await ctx.send("Para utilizar este comando necesita ser Premium.")

@bot.command("video")
async def on_video(ctx: Context):
	await ctx.create_channel(str(ctx.msg.threadId), ctx.msg.ndcId)
	mp = "https://github.com/HakiBl4ck/alissabot2525/blob/main/media/319_Familiar-Wife-Poster.jpg?raw=true"
	kik = "https://github.com/HakiBl4ck/alissabot2525/blob/main/media/TWICE.mp4?raw=true"
	await ctx.play_video(mp, kik, "Twice", 199.8, str(ctx.msg.threadId), ctx.msg.ndcId)

@bot.command("getid")
async def on_getid(ctx: Context):
	delta = ctx.msg.content[7:40]
	alubia = await ctx.get_info_link(delta)
	oid = alubia.linkInfo.objectId
	tuba = await ctx.client.get_link_identify(oid)
	await ctx.send(str(tuba))
	
@bot.command("play")
async def on_musica(ctx: Context):
	dart = ctx.msg.content[6:30]
	flix = await ctx.download_from_link("https://github.com/HakiBl4ck/alissabot2525/blob/main/media/" + dart + ".mp3?raw=true")
	await ctx.send_audio(flix)

@bot.command("patear")
async def on_patada(ctx: Context):
	habas = ctx.msg.content[8:30]
	await ctx.send(ctx.msg.author.nickname + " le dio una patada de la surte a " + habas)
	
@bot.command("carta")
async def on_carta(ctx: Context):
	magia = random.choice(cards)
	tarjeta = await ctx.download_from_link("https://github.com/HakiBl4ck/eskelerbot007/raw/main/" + magia)
	await ctx.send_image(tarjeta)
	await ctx.send("Carta sacada de: " + ctx.msg.author.nickname)
	
@bot.command("dm")
async def on_dm(ctx: Context):
	kula = ctx.msg.author.uid
	await ctx.send("Que onda papu", chat_id=kula)
	
@bot.command("tiktok")
async def on_tistos(ctx: Context):
	luka = ctx.msg.content[8:60]
	url = "https://tiktok-downloader-download-tiktok-videos-without-watermark.p.rapidapi.com/index"
	querystring = {"url":str(luka)}
	headers = {
		"X-RapidAPI-Key": "082395124cmsh8f011e89c74584fp1b5c87jsn52b9ca1173b4",
		"X-RapidAPI-Host": "tiktok-downloader-download-tiktok-videos-without-watermark.p.rapidapi.com"
	}
	response = requests.request("GET", url, headers=headers, params=querystring)
	gloom = response.json()
	tiki = gloom["video"]
	if ctx.msg.author.uid in premiums:
		await ctx.reply(str(tiki))
	else:
		await ctx.reply("Para utilizar este comando necesita ser Premium.")
	
@bot.command("caracola")
async def on_caracola(ctx: Context):
	answers = ["Posiblemente mi pequeñ@ elf@", "Uff.. lo veo muy dificil", "Por supuesto", "No", "Nunca", "Si", "Como bichot@ que eres, seguro que si", "Eso preguntaselo a una bruja, yo que se.", "Clarisimo que no", "No se, pregunta eso a tu tercer @", "Pues por supuesto que no", "Yes bitch!"]
	puca = random.choice(answers)
	await ctx.reply(str(puca))
	
@bot.command("compatibilidad")
async def on_compat(ctx: Context):
	un = ctx.msg.author.nickname
	plux = ctx.msg.content[16:30]
	rango = random.choice(range(1,100))
	await ctx.send("La compatibilidad amorosa entre " + un + " y " + plux + "\nes de " + str(rango) + "%")

@bot.command("marryme")
async def on_casados(ctx: Context):
	novio = ctx.msg.author.nickname
	novia = ctx.msg.content[9:35]
	kunno = sqlite3.connect("matris.db")
	curzor = kunno.cursor()
	curzor.execute("INSERT INTO casados VALUES (null,?,?)", (novio, novia))
	kunno.commit()
	kunno.close()
	await ctx.send("Felicitaciones a " + novio + " y " + novia + "\nPor su matrimonio, hasta que el amante los separe!")

@bot.command("comandos")
async def on_cmds(ctx: Context):
	await ctx.send("[BUI]Lista de Comandos\n!ping: Usalo para saber si el bot esta activo.\n!hola: Comando para saludar al bot.\n!pokedex (nombre del pokemon): Este comando envia la imagen de dicho pokemon.\n!abrazar (@nombre de la persona): Abrazas a esa persona espcial.\n@!descargar (link del video)[PREMIUM]: Permite descargar canciones de youtube.\n!patear (@nombre de la persona): Envias una patada a esa persona especial.\n!carta: Sacas una carta al azar de un idol [Apuesta].\n!caracola (pregunta): Puedes preguntarle algo a la caracola magica.\n!compatibilidad (nombre de la persona): Puedes saber tu compatibilidad con dicha persona.")

@bot.command("checkin")
async def on_checkin(ctx: Context):
	await ctx.client.check_in(tz=360)
	await ctx.reply("Check In Realizado!")

@bot.command("ctm")
async def on_ctm(ctx: Context):
	alma = ctx.msg.content[5:30]
	idi = await ctx.download_from_link("https://github.com/HakiBl4ck/eskelerbot007/raw/main/Concha%20tu%20madre%20Concha%20tu%20madre%20(online-audio-converter.com).mp3")
	await ctx.send_audio(idi)
	await ctx.send("Audio dedicado a " + alma)

@bot.command("clima")
async def on_weather(ctx: Context):
	extasis = ctx.msg.content[7:27]
	url = "https://yahoo-weather5.p.rapidapi.com/weather"
	querystring = {"location":extasis,"format":"json","u":"c"}
	headers = {
		"X-RapidAPI-Key": "082395124cmsh8f011e89c74584fp1b5c87jsn52b9ca1173b4",
		"X-RapidAPI-Host": "yahoo-weather5.p.rapidapi.com"
	}
	response = requests.request("GET", url, headers=headers, params=querystring)
	foca = response.json()
	clima = foca["forecasts"][0]["text"]
	tempMin = foca["forecasts"][0]["low"]
	tempMax = foca["forecasts"][0]["high"]
	ciudad = foca["location"]["city"]
	sunrise = foca["current_observation"]["astronomy"]["sunrise"]
	sunset = foca["current_observation"]["astronomy"]["sunset"]
	await ctx.send("[B]" + ciudad + "\n" + clima + "\nTemperatura Minima: " + str(tempMin) + "°\nTemperatura Maxima: " + str(tempMax) + "°\nAmanecer: " + sunrise + "\nAnochecer: " + sunset)
	
@bot.command("idol")
async def on_avatar(alv: Context):
	aio = alv.msg.content[6:30]
	url = "https://k-pop.p.rapidapi.com/idols"
	querystring = {"q":aio,"by":"Stage Name","limit":"2"}
	headers = {
		"X-RapidAPI-Key": "082395124cmsh8f011e89c74584fp1b5c87jsn52b9ca1173b4",
		"X-RapidAPI-Host": "k-pop.p.rapidapi.com"
	}
	response = requests.request("GET", url, headers=headers, params=querystring)
	bp = response.json()
	fn = bp["data"][0]["Full Name"]
	kn = bp["data"][0]["Korean Name"]
	cum = bp["data"][0]["Date of Birth"]
	bipl = bp["data"][0]["Birthplace"]
	alt = bp["data"][0]["Height"]
	pes = bp["data"][0]["Weight"]
	nombre = bp["data"][0]["Stage Name"]
	await alv.send("[BU]Ficha de " + nombre + "\nNombre Completo: " + fn + "\nNombre Coreano: " + kn + "\nFecha de Nacimiento: " + cum + "\nLugar de Origen: "+ bipl + "\nAltura: " + alt + "\nPeso: " + pes)
	
@bot.command("chisme")
async def on_newchisme(ctx: Context):
	ch = ctx.msg.content[8:200]
	prop = ctx.msg.author.nickname
	lizy = sqlite3.connect("chismografo.db")
	k = lizy.cursor()
	k.execute("INSERT INTO chismes VALUES (?,?)", (ch, prop))
	lizy.commit
	await ctx.send("Chsime agregado con exito!")
	lizy.close

@bot.command("chismografo")
async def on_chismear(ctx: Context):
	monda = sqlite3.connect("chismografo.db")
	kax = monda.cursor()
	kax.execute("SELECT * FROM chismes")
	dado = kax.fetchall()
	gamma = " ".join(map(str, dado))
	await ctx.send(gamma)
	monda.close()
	
@bot.command("msi")
async def on_msi(ctx: Context):
	await ctx.send(ctx.msg.threadId)
	
@bot.command("matrimonios")
async def on_casades(ctx: Context):
	ily = sqlite3.connect("matris.db")
	fanta = ily.cursor()
	fanta.execute("SELECT * FROM casados")
	erga = fanta.fetchall()
	celta = " ".join(map(str, erga))
	await ctx.send(celta)
	ily.close()
	
	
bot.start()
