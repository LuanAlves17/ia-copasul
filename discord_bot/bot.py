import discord
from discord.ext import commands

from dotenv import load_dotenv

import os

load_dotenv()

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print(f"Bot conectado como {bot.user}")

@bot.command('ping')
async def ping(ctx):
    await ctx.send('Pong!')

@bot.command('aola')
async def ola(ctx):
    await ctx.send(f'Olá {ctx.author.name}!')

bot.run(os.getenv('TOKEN_BOT_DC'))