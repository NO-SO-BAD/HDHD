#imports
import discord
from discord.ext import commands
import json
import os
import time
import asyncio
from keep_alive import keep_alive
from datetime import datetime, timedelta
from discord.utils import get
from __init__ import main, get_lock, config, authorize
#start up
bot = commands.Bot(command_prefix="!",
                   help_command=None,
                   intents=discord.Intents.all())

my_secret = os.environ['discord-key']


@bot.event
async def on_ready():
    activity = discord.Game(name="Buscando fusiones")
    await bot.change_presence(status=discord.Status.online, activity=activity)
    #authorize()
    #config()
    #get_lock()
    #main()
   


#help


class Help(commands.Cog):
    def Bot(self):
        self.Bot = bot

    @commands.command(name="help", aliases=["ayuda", "Help", "Ayuda"])
    async def _help(self, ctx):
      embedVar2 = discord.Embed( 
                  title="Colaboracion",
                  description=
                  "Buscas colaboracion? Contactate con nosotros",
                  color=0x0b0909,
                  timestamp=datetime.utcnow())
     
      embedVar2.set_author(
                  name=f"{ctx.author.name}",
                  icon_url=
                  f"{ctx.author.avatar_url}"
                 )
      embedVar2.set_image(url="")
   
      embedVar2.set_footer(
                  text="© SoftGames Interactive 2022"
                  )  
      await ctx.send(embed=embedVar2)
        

#Colaboracion
class Colaboracion(commands.Cog):
    def Bot(self):
        self.Bot = bot
    
    @commands.command(name="colaboracion", aliases=["Colaboracion"])
    async def _colaboracion(self, ctx):
     embedVar2 = discord.Embed( 
                  title="Colaboracion",
                  description=
                  "Buscas colaboracion? Contactate con nosotros",
                  color=0x0b0909,
                  timestamp=datetime.utcnow())
     embedVar2.add_field(name = "Info", value = """
     ☁️| RP SERVIDORES |☁️

☁️ Este Servidor fue creado para la Comodidad de todos los jugadores en encontrar el mejor Servidor RP ☁️

☁️🎧Contamos com Musica🎧☁️

☁️😂Memes y Diversion😂☁️

☁️📈Encuestas para ver cual es el mejor server📈☁️

☁️🚫Gente Reportada🚫☁️

☁️🛠Soporte🛠☁️

☁️🔥Ayuda en Golpes Gta5🔥☁️

https://discord.gg/BdVHjzswcU
     
     
     
     
     
     
     """)
     embedVar2.set_author(
                  name=f"{ctx.author.name}",
                  icon_url=
                  f"{ctx.author.avatar_url}"
                 )
     embedVar2.set_image(url="https://cdn.discordapp.com/attachments/1003448926784978994/1003854186582114385/3E559A6F-8F16-4FD0-8198-53BD05330389.jpg")
   
     embedVar2.set_footer(
                  text="© SoftGames Interactive 2022"
                  )  
     await ctx.send(embed=embedVar2)




@bot.command()
@commands.has_permissions(administrator = True)
async def crear_wh(ctx):
  await ctx.send("creando...")
  await ctx.channel.create_webhook(name="twitch-Streams")
#cogs
bot.add_cog(Colaboracion(bot))
bot.add_cog(Help(bot))   
#



#run
keep_alive()
bot.run(bot.run(os.environ['']))

