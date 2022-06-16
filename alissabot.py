from edamino import Bot, Context
import requests
import json
import sqlite3
import random
import time

bot = Bot('asterixyt@yahoo.com', 'Volcan1000', '!')

premiums = ["fc83578c-706a-44ef-bc2a-e2c119f2fe92"]
cards = ["JennieFUT.png", "JisooFUT.png", "JinsoulFUT.png", "LisaFUT.png", "HeejinFUT.png", "JypFUT.png", "SmFUT.png", "KarinaFUT.png", "NingningFUT.png", "RoseFUT.png", "YgFUT.png"]

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
	await ctx.play_video("https://github.com/HakiBl4ck/alissabot2525/blob/main/media/319_Familiar-Wife-Poster.jpg", "https://github.com/HakiBl4ck/alissabot2525/blob/main/media/TWICE.mp4", "Twice", 199.8, "b85f8eed-15dd-099a-12d9-a7d983b54f74", 6872133)

@bot.command("getid")
async def on_getid(ctx: Context):
	delta = ctx.msg.content[7:40]
	alubia = await ctx.client.get_info_link(delta)
	await ctx.send(str(alubia))
	
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
	luka = ctx.msg.content[8:50]
	url = "https://tiktok-downloader-download-tiktok-videos-without-watermark.p.rapidapi.com/index"
	querystring = {"url":"https://www.tiktok.com/@nor10122/video/7037155617491913986"}
	headers = {
		"X-RapidAPI-Key": "082395124cmsh8f011e89c74584fp1b5c87jsn52b9ca1173b4",
		"X-RapidAPI-Host": "tiktok-downloader-download-tiktok-videos-without-watermark.p.rapidapi.com"
	}
	response = requests.request("GET", url, headers=headers, params=querystring)
	gloom = response.json()
	tiki = gloom["video"][0]
	if ctx.msg.author.uid in premiums:
		await ctx.reply(str(tiki))
	else:
		await.reply("Para utilizar este comando necesita ser Premium.")
	
@bot.command("caracola")
async def on_caracola(ctx: Context):
	answers = ["Posiblemente mi pequeñ@ elf@", "Uff.. lo veo muy dificil", "Por supuesto", "No", "Nunca", "Si", "Como bichot@ que eres, seguro que si", "Eso preguntaselo a una bruja, yo que se.", "Clarisimo que no", "No se, pregunta eso a tu tercer @", "Pues por supuesto que no", "Yes bitch!"]
	puca = random.choice(answers)
	await.reply(puca)
	
@bot.command("truco")
async def on_tricky(ctx: Context):
	await ctx.send("Ahora estoy..")
	time.sleep(3)
	await ctx.delete_message(ctx.msg.messageId)
	
bot.start()
