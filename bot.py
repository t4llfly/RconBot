import discord
from discord.ext import commands
from mcstatus import JavaServer
import mcrcon

SERVER_ADDRESS = input("Введите IP сервера: ")
SERVER_PORT = input("Введите порт сервера: ")

server = JavaServer(SERVER_ADDRESS, SERVER_PORT)
bot = commands.Bot(command_prefix='!', intents=discord.Intents.all())

@bot.event
async def on_ready():
    print(f'Запущен как {bot.user}')
    await bot.tree.sync()
@bot.tree.command(name="addtowl")
async def addtowl(interaction: discord.Interaction, username: str):

    with mcrcon.MCRcon('localhost', 'PASSWORD_FROM_SERVERPROPERTIES') as rcon:
        rcon.command('whitelist add ' + username)

    await interaction.response.send_message(f'**{username}** был добавлен в белый список.')

bot.run('TOKEN')