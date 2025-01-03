import discord
from discord.ext import commands
from bot_logic import gen_pass
# La variable intents almacena los privilegios del bot
intents = discord.Intents.default()
# Activar el privilegio de lectura de mensajes
intents.message_content = True
# Crear un bot en la variable cliente y transferirle los privilegios
bot = discord.Client(intents=intents)
@bot.event
async def on_ready():
    print(f'Hemos iniciado sesión como {bot.user}')
@bot.event
async def on_message(message):
    if message.author == bot.user:
        return
    if message.content.startswith('hola'):
        await message.channel.send("ola")
    elif message.content.startswith('adios'):
        await message.channel.send("chao :(")
    elif message.content.startswith('gol'):
        await message.add_reaction("⚽")
    elif message.content.startswith('dame una clave'):
         password = gen_pass() 
         await message.channel.send(f"Aquí está tu clave: {password}")
    else:
        await message.channel.send(message.content)

bot.run("MTMxODMwMDU2Mzc0MTYxMDAxNA.GXIml1.HgnXkOxuisnxFqW0N0tGANGAYu2ZBvf0wra1GE")
