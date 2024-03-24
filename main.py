import discord
from discord.ext import commands
from ayarlar import ayarlar
import random
import os
import requests
resimler = os.listdir("images")
intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')

@bot.command
async def mem(ctx):
    rastgele_resim=random.choice(resimler)
    with open(f"images/{rastgele_resim}") as f:
        resim = discord.File(f)
    await ctx.send()

def get_duck_image_url():    
    url = 'https://random-d.uk/api/random'
    res = requests.get(url)
    data = res.json()
    return data['url']


@bot.command('duck')
async def duck(ctx):
    
    image_url = get_duck_image_url()
    await ctx.send(image_url)



bot.run(ayarlar["TOKEN"])