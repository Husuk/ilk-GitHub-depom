import discord
from ayarlar import ayarlar
from discord.ext import commands

izinler = discord.Intents.default()
izinler.message_content = True

bot = commands.Bot(command_prefix = "!",intents=izinler)

