import discord
from discord.ext import commands
from ayarlar import ayarlar
import random
import os
import requests
cat_resimler = os.listdir("images\cat")
dog_resimler = os.listdir("images\dog")
intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')

@bot.command()
async def mem(ctx,a:str):
    if a == "cat":    
        rastgele_resim=random.choice(cat_resimler)
        with open(f"images\{a}\{rastgele_resim}") as f:
            resim = discord.File(f)
        await ctx.send(file=resim)
    if a == "dog":
        rastgele_resim=random.choice(dog_resimler)
        with open(f"images\{a}\{rastgele_resim}") as f:
            resim = discord.File(f)
        await ctx.send(file=resim)

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
