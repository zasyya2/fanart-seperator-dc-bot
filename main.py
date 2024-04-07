import discord
import random
import time
from discord.ext import commands
from bot_token import bottoken
from idk import get_class
import requests

intents = discord.Intents.default()

intents.message_content = True

bot = commands.Bot(command_prefix='/', intents=intents)


@bot.event
async def on_ready():
    print(f'{bot.user} olarak giriş yaptık')

@bot.command()
async def hello(ctx):
    await ctx.send(f'Merhaba {bot.user}! Ben bir botum!')

@bot.command()
async def chat(ctx):
    await ctx.send(f'Merhaba! Ne hakkında konuşalım?')

@bot.command()
async def bored(ctx):
    await ctx.send(f'Ooo. Ne konuşalım?')

@bot.command()
async def nofriends(ctx):
    await ctx.send(f'Ooo. Ne konuşalım?!')
    
@bot.command()
async def anime(ctx):
    await ctx.send(f'ooo')
    time.sleep (1)
    await ctx.send(f'Bende öyle bir bilgi yok x-x')
    time.sleep (1)
    await ctx.send(f'Ama minecraft konuşabiliriz!')

def get_duck_image_url():    
    url = 'https://random-d.uk/api/random'
    res = requests.get(url)
    data = res.json()
    return data['url']


@bot.command('duck')
async def duck(ctx):
    '''duck komutunu çağırdığımızda, program ordek_resmi_urlsi_al fonksiyonunu çağırır.'''
    image_url = get_duck_image_url()
    await ctx.send(image_url)


@bot.command()
async def detect (ctx):
    if ctx.message.attachments:
        for attachment in ctx.message.attachments:
            file_name=attachment.filename
            url = attachment.url
            image_path = "/images" + file_name
 
            await attachment.save(image_path)
            await ctx.send ("Resim Kaydedildi!")
            class_name, score = get_class("keras_model.h5", "labels.txt", image_path)
            await ctx.sen(f'It is a ', class_name, 'fanart!')
    else:
        await ctx.send(f'no file found')

    await ctx.send(f'..')


bot.run(bottoken)