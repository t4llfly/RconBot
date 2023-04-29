import discord
from discord.ext import commands
from discord import app_commands
import mcrcon
import os
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('TOKEN')

RCON_IP = input("Введите IP rcon сервера: ")
RCON_PASSWORD = input("Введите пароль rcon сервера: ")

bot = commands.Bot(command_prefix='!', intents=discord.Intents.all())

@bot.event
async def on_ready():
    print(f'Запущен как {bot.user}')
    await bot.tree.sync()


@bot.tree.command(name="whitelistadd", description="Добавить игрока в белый список")
@app_commands.describe(username="Никнейм игрока на сервере Minecraft")
# не работает по какой-то причине @commands.has_role("757460298889429023")
async def whitelistadd(interaction: discord.Interaction, username: str):
    global RCON_IP
    global RCON_PASSWORD

    with mcrcon.MCRcon(RCON_IP, RCON_PASSWORD) as rcon:
        rcon.command('whitelist add ' + username)
    await interaction.response.send_message(f'**{username}** был добавлен в белый список.')


@bot.tree.command(name="whitelistremove", description="Убрать игрока из белого списка")
@app_commands.describe(username="Никнейм игрока на сервере Minecraft")
async def whitelistremove(interaction: discord.Interaction, username: str):
    global RCON_IP
    global RCON_PASSWORD

    with mcrcon.MCRcon(RCON_IP, RCON_PASSWORD) as rcon:
        rcon.command('whitelist add ' + username)
    await interaction.response.send_message(f'**{username}** был убран из белого списка.')


@bot.tree.command(name="banplayer", description="Забанить игрока на сервере")
@app_commands.describe(username="Никнейм игрока на сервере Minecraft", time="Время бана", reason="Причина бана")
async def banplayer(interaction: discord.Interaction, username: str, time: str, reason: str):
    global RCON_IP
    global RCON_PASSWORD

    with mcrcon.MCRcon(RCON_IP, RCON_PASSWORD) as rcon:
        rcon.command('ban ' + username + time + reason)
    await interaction.response.send_message(f'**{username}** был забанен на **{time}**. Причина: **{reason}**')


@bot.tree.command(name="unbanplayer", description="Разбанить игрока на сервере")
@app_commands.describe(username="Никнейм игрока на сервере Minecraft")
async def unbanplayer(interaction: discord.Interaction, username: str):
    global RCON_IP
    global RCON_PASSWORD

    with mcrcon.MCRcon(RCON_IP, RCON_PASSWORD) as rcon:
        rcon.command('pardon ' + username)
    await interaction.response.send_message(f'**{username}** был разбанен на сервере.')

bot.run(TOKEN)
