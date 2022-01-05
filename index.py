import discord
import time
from discord.ext import commands
import json
import datetime
from discord import FFmpegPCMAudio
import random
from urllib import parse, request
import re

ver = "Version 0.1"
bot = commands.Bot(command_prefix='!', description ="Command prefix")

@bot.command()
async def menu(ctx):
    embed = discord.Embed(title="Comandos", timestamp= datetime.datetime.utcnow(), color=discord.Color.red())
    embed.add_field(name =  "Caza", value ="!c")
    embed.add_field(name=   "Pesca", value="!pc")
    embed.add_field(name=   "Dungeon", value="!dng")
    embed.add_field(name =  "Apoyo",  value ="!ap")
    embed.add_field(name =  "Coliseum",  value ="!csm")
    embed.add_field(name =  "Inventario",  value ="!inv")
    embed.add_field(name =  "Perfil",  value ="!p")
    embed.add_field(name =  "Level up",  value ="!lvlup")
    embed.add_field(name =  "Cambio de clase",  value ="!rolupdate")
    embed.add_field(name =  "Ranking",  value ="!king")
    embed.add_field(name =  "Listado de arcos",  value ="!arcos")
   #embed.set_thumbnail(url="https://geekland.eu/wp-content/uploads/2020/04/usar-y-configurar-el-historial-de-comandos-history-1280x720.png")
    await ctx.send(embed=embed)

#Comandos de menú

@bot.command()
async def c(ctx):
    embed = discord.Embed(color=discord.Color.red())
    embed.add_field(name='\u200b', value="Caza No implementado" + "\n\u200b")
    await ctx.send(embed=embed)

@bot.command()
async def pc(ctx):
    embed = discord.Embed(color=discord.Color.red())
    embed.add_field(name='\u200b', value="Pesca No implementado" + "\n\u200b")
    await ctx.send(embed=embed)

@bot.command()
async def dng(ctx):
    embed = discord.Embed(color=discord.Color.red())
    embed.add_field(name='\u200b', value="Dungeon No implementado" + "\n\u200b")
    await ctx.send(embed=embed)

@bot.command()
async def ap(ctx):
    embed = discord.Embed(color=discord.Color.red())
    embed.add_field(name='\u200b', value="Apoyo No implementado" + "\n\u200b")
    await ctx.send(embed=embed)

@bot.command()
async def csm(ctx):
    embed = discord.Embed(color=discord.Color.red())
    embed.add_field(name='\u200b', value="Coliseo No implementado" + "\n\u200b")
    await ctx.send(embed=embed)

@bot.command()
async def inv(ctx):
    embed = discord.Embed(color=discord.Color.red())
    embed.add_field(name='\u200b', value="Inventario No implementado" + "\n\u200b")
    await ctx.send(embed=embed)

@bot.command()
async def p(ctx):
    embed = discord.Embed(title='\u200b')
    author = ctx.message.author
    pfp = author.avatar_url
    embed.set_thumbnail(url = (pfp))
    await ctx.send(embed=embed)

@bot.command()
async def lvlup(ctx):
    embed = discord.Embed(color=discord.Color.red())
    embed.add_field(name='\u200b', value="Subir nivel No implementado" + "\n\u200b")
    await ctx.send(embed=embed)

@bot.command()
async def rolupdate(ctx):
    embed = discord.Embed(color=discord.Color.red())
    embed.add_field(name='\u200b', value="Cambio de clase No implementado" + "\n\u200b")
    await ctx.send(embed=embed)
    
@bot.command()
async def king(ctx):
    embed = discord.Embed(color=discord.Color.red())
    embed.add_field(name='\u200b', value="Ranking No implementado" + "\n\u200b")
    await ctx.send(embed=embed)


#Fin comandos de menú

class Jugador:
    def __init__(self, nombre, lv, exp, rol, lasthunt, lastfish, lastdungeon, lastsupport, inv):
        self.nombre = nombre
        self.lasthunt = lasthunt
        self.lv = lv
        self.exp = exp
        self.rol = rol
        self.lastfish = lastfish
        self.lastdungeon = lastdungeon
        self.lastsupport = lastsupport
        self.inv = inv

colm = Jugador("Colm",99,1000000,"Monk",None,None,None,None,None)


@bot.command()
async def start(ctx):
    member = ctx.author
    with open('pt.gif', 'rb') as f: picture = discord.File(f)
    await ctx.send(file=picture)
    await ctx.send("Clases alpha")
    embed = discord.Embed(color=discord.Color.blue())
    embed.add_field(name='\u200b', value="Mago" + "\n\u200b")
    await ctx.send(embed=embed)
    embed = discord.Embed(color=discord.Color.red())
    embed.add_field(name='\u200b', value="Ladrón" + "\n\u200b")
    await ctx.send(embed=embed)
    embed = discord.Embed(color=discord.Color.blue())
    embed.add_field(name='\u200b', value="Mercenario" + "\n\u200b")
    await ctx.send(embed=embed)
    member = ctx.author
    message = await bot.wait_for('message', check=check_clase(ctx.author,ctx), timeout=30)
    await ctx.send("Has escogido la clase " + message.content)

def check_clase(author,ctx):
    def inner_check(message):
        if message.content == "Ladrón" :
             return message.author == author and message.content == "Ladrón"
        elif message.content == "Mago" :
            return message.author == author and message.content == "Mago"
        elif message.content == "Mercenario" :
            return message.author == author and message.content == "Mercenario"
    return inner_check


@bot.command()
async def arcos(ctx):
    await ctx.send("Lv 3" , file=discord.File('Weapons/Arco1.png'))
    await ctx.send("Lv 6" , file=discord.File('Weapons/Arco2.png'))
    await ctx.send("Lv 9" , file=discord.File('Weapons/Arco3.png'))
    await ctx.send("Lv 12", file=discord.File('Weapons/Arco4.png'))
    await ctx.send("Lv 15", file=discord.File('Weapons/Arco5.png'))


@bot.command()
async def start_assassin(ctx):
    with open('colm.gif', 'rb') as f: picture = discord.File(f)
    await ctx.send(file=picture)

@bot.command()
async def ping(ctx):
    embed = discord.Embed(color=discord.Color.red())
    embed.add_field(name= "Despliegue correcto.", value ="Todos los servicios estan activos.")
    await ctx.send(embed=embed)

@bot.event
async def on_ready():
    await bot.change_presence(activity=discord.Game(name="ZEV", timestamp = datetime.datetime.utcnow()))
    print('Succesfully connected')
bot.run('#######################')
