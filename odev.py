import discord
from ayarlar import ayarlar
from discord.ext import commands
import random
izinler = discord.Intents.default()
izinler.message_content = True

bot = commands.Bot(command_prefix = "?",intents=izinler)

@bot.event
async def on_ready():
    print(f"{bot.user} çevrimiçi oldu")
iller = ["mersin","adana","sivas","ankara","istanbul"]
@bot.command
async def dene(ctx,tahmin:str):
    il = random.choice(iller)
    if not tahmin in il:
        await ctx.send("o harf burada yok")
    if tahmin in il:
        for i in range(len(il)):
            if il[i] != tahmin:
                il[i] = "#"
        await ctx.send(il)

                    






bot.run(ayarlar["TOKEN"])

