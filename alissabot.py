from edamino import Bot, Context
from ezgiphy import GiphyPublicAPI
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
	manteca = ctx.msg.content[12:30]
	res = requests.get("https://www.superheroapi.com/api.php/1282131145540058/search/" + manteca)
	data = res.json()
	img = data["results"][0]["image"]["url"]
	imagen = await ctx.download_from_link(img)
	await ctx.send_image(imagen)
	print(ctx.msg.author.nickname + " invoco a un super heroe.")

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
	conex = sqlite3.connect("aminodb.db")
	curzor = conex.cursor()
	curzor.execute("SELECT * FROM usuarios")
	user = curzor.fetchone()
	member = " ".join(map(str, user))
	await ctx.send(member)
	conex.close()

@bot.command("gif")
async def on_gif(ctx: Context):
	giphy = GiphyPublicAPI('dc6zaTOxFJmzC')
	a = giphy.search(q='madonna',limit=5,rating='g')
	print(a)


bot.start()