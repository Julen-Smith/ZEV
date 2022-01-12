from os import read
from Data.gestionxml import checkRootXml
import discord
import time
from discord.ext import commands
import datetime
from urllib import parse, request
import re
import Bot.responseCommands
import Data.gestionxml
import Utils.check
import Obj.Player


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
    await ctx.send(embed=embed)

#Comandos de menú

@bot.command()
async def init_server(ctx):
    serverid = ctx.guild.id  
    if Data.gestionxml.check_for_server_id(serverid):
         await ctx.send("El servidor ya esta registrado.")
    elif Data.gestionxml.register_new_server(serverid):
        await ctx.send("El servidor ha sido registrado.")
    else:
        await ctx.send("Ha ocurrido algún tipo de error con el registro de tú servidor, contacta a Colm#7192.")
    await ctx.send("Tu servidor será procesado con la identificación " + str(serverid) + ".")



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

@bot.command()
async def start(ctx):
    member = ctx.author
    with open('../Assets/pt.gif', 'rb') as f: picture = discord.File(f)
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
    message = await bot.wait_for('message', check= Utils.check_clase(ctx.author,ctx), timeout=30)
    await ctx.send("Has escogido la clase " + message.content)



@bot.command()
async def arcos(ctx):
    await ctx.send("Lv 3" , file=discord.File('../../Weapons/Arco1.png'))
    await ctx.send("Lv 6" , file=discord.File('../../Weapons/Arco2.png'))
    await ctx.send("Lv 9" , file=discord.File('../../Weapons/Arco3.png'))
    await ctx.send("Lv 12", file=discord.File('../../Weapons/Arco4.png'))
    await ctx.send("Lv 15", file=discord.File('../../Weapons/Arco5.png'))

c
@bot.command()
async def start_assassin(ctx):
    with open('../Assets/assa.gif', 'rb') as f: picture = discord.File(f)
    await ctx.send(file=picture)

@bot.command()
async def ping(ctx):
    embed = discord.Embed(color=discord.Color.red())
    embed.add_field(name= "Despliegue correcto.", value ="Todos los servicios estan activos.")
    await ctx.send(embed=embed)


@bot.event
async def on_ready():
    await bot.change_presence(activity=discord.Game(name= "Proximo Wipe : 20-10-2022"))
    #checkRootXml()
    print('Succesfully connected')
bot.run('################################################################')
#Fin comandos de menú