from edamino import Bot, Context
import requests
import json
import sqlite3

bot = Bot('asterixyt@yahoo.com', 'Volcan1000', '!')

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
	mulan = ctx.msg.content[10:21]
	url = "https://youtube-mp3-download1.p.rapidapi.com/dl"
	querystring = {"id":mulan}
	headers = {
		"X-RapidAPI-Host": "youtube-mp3-download1.p.rapidapi.com",
		"X-RapidAPI-Key": "082395124cmsh8f011e89c74584fp1b5c87jsn52b9ca1173b4"
}
	response = requests.request("Get", url, headers=headers, params=querystring)
	datona = response.json()
	rayo = datona["link"]
	await ctx.send(str(rayo))

@bot.command("play")
async def on_video(ctx: Context):
	await ctx.play_video("https://github.com/HakiBl4ck/alissabot2525/blob/main/media/319_Familiar-Wife-Poster.jpg", "https://github.com/HakiBl4ck/alissabot2525/blob/main/media/TWICE.mp4", "Twice", 199.8, "b85f8eed-15dd-099a-12d9-a7d983b54f74", 6872133)

@bot.command("getid")
async def on_getid(ctx: Context):
	delta = ctx.msg.content[8:40]
	alubia = await ctx.client.get_info_link(delta)
	await ctx.send(str(alubia))
	
@bot.command("musica")
async def on_musica(ctx: Context):
	dart = ctx.msg.content[9:16]
	cd = "https://github.com/HakiBl4ck/alissabot2525/blob/main/media/" + dart + ".m4a"
	#flop = await ctx.download_from_link(cd)
	#await ctx.send_audio(flop)
	await ctx.send(cd)

bot.start()
