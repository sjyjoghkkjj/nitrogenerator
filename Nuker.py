# Made By Deeply
# Invite = https://discordapp.com/oauth2/authorize?client_id=577013437603905538&permissions=8&scope=bot


import discord
from discord.ext.commands import *
from discord.ext import commands
import random
import asyncio
import time
import json
from itertools import cycle
import time
from threading import Thread
from random import randint
import datetime
import os
import aiohttp
import sys
import traceback
import json
from discord.utils import get

 
##PREFIX##

bot = commands.Bot(command_prefix='!')

client = commands.Bot(command_prefix='!')

##OTHER##
bot.remove_command('help')



##BOT IS READY##
@bot.event
async def on_ready():
#BOT STATUS#
    print("Bot Is Online! Getting Ready To Spam.")
    print(f"Bot Status: Online!...")



##BAN COMMAND##
@bot.command(pass_context=True)
async def ban(ctx, member : discord.Member):
    await member.ban()
    await ctx.message.delete()

 
##SPAM COMMAND##
@bot.command(pass_context=True)
async def spam(ctx): #run "!spam" to run the command
    await ctx.message.delete()
    while True:
      await ctx.send("СЕРВЕР КРАШНУТ\nС ЛЮБОВЬЮ АРСЭНЫЙ https://discord.gg/4Vnn6uv @everyone/nСЕРВЕР КРАШНУТ\nС ЛЮБОВЬЮ АРСЭНЫЙ💗 https://discord.gg/4Vnn6uv @everyone/nСЕРВЕР КРАШНУТ\nС ЛЮБОВЬЮ АРСЭНЫЙ https://discord.gg/4Vnn6uv @everyone/n")
      await ctx.send("СЕРВЕР КРАШНУТ\nС ЛЮБОВЬЮ АРСЭНЫЙ https://discord.gg/4Vnn6uv @everyone/nСЕРВЕР КРАШНУТ\nС ЛЮБОВЬЮ АРСЭНЫЙ💗 https://discord.gg/4Vnn6uv @everyone/nСЕРВЕР КРАШНУТ\nС ЛЮБОВЬЮ АРСЭНЫЙ https://discord.gg/4Vnn6uv @everyone/n")
      await ctx.send("СЕРВЕР КРАШНУТ\nС ЛЮБОВЬЮ АРСЭНЫЙ https://discord.gg/4Vnn6uv @everyone/nСЕРВЕР КРАШНУТ\nС ЛЮБОВЬЮ АРСЭНЫЙ💗 https://discord.gg/4Vnn6uv @everyone/nСЕРВЕР КРАШНУТ\nС ЛЮБОВЬЮ АРСЭНЫЙ https://discord.gg/4Vnn6uv @everyone/n")
      await ctx.send("СЕРВЕР КРАШНУТ\nС ЛЮБОВЬЮ АРСЭНЫЙ https://discord.gg/4Vnn6uv @everyone/nСЕРВЕР КРАШНУТ\nС ЛЮБОВЬЮ АРСЭНЫЙ💗 https://discord.gg/4Vnn6uv @everyone/nСЕРВЕР КРАШНУТ\nС ЛЮБОВЬЮ АРСЭНЫЙ https://discord.gg/4Vnn6uv @everyone/n")
      await ctx.send("СЕРВЕР КРАШНУТ\nС ЛЮБОВЬЮ АРСЭНЫЙ https://discord.gg/4Vnn6uv @everyone/nСЕРВЕР КРАШНУТ\nС ЛЮБОВЬЮ АРСЭНЫЙ💗 https://discord.gg/4Vnn6uv @everyone/nСЕРВЕР КРАШНУТ\nС ЛЮБОВЬЮ АРСЭНЫЙ https://discord.gg/4Vnn6uv @everyone/n")
      await ctx.send("СЕРВЕР КРАШНУТ\nС ЛЮБОВЬЮ АРСЭНЫЙ https://discord.gg/4Vnn6uv @everyone/nСЕРВЕР КРАШНУТ\nС ЛЮБОВЬЮ АРСЭНЫЙ💗 https://discord.gg/4Vnn6uv @everyone/nСЕРВЕР КРАШНУТ\nС ЛЮБОВЬЮ АРСЭНЫЙ https://discord.gg/4Vnn6uv @everyone/n")
      await ctx.send("СЕРВЕР КРАШНУТ\nС ЛЮБОВЬЮ АРСЭНЫЙ https://discord.gg/4Vnn6uv @everyone/nСЕРВЕР КРАШНУТ\nС ЛЮБОВЬЮ АРСЭНЫЙ💗 https://discord.gg/4Vnn6uv @everyone/nСЕРВЕР КРАШНУТ\nС ЛЮБОВЬЮ АРСЭНЫЙ https://discord.gg/4Vnn6uv @everyone/n")
      await ctx.send("СЕРВЕР КРАШНУТ\nС ЛЮБОВЬЮ АРСЭНЫЙ https://discord.gg/4Vnn6uv @everyone/nСЕРВЕР КРАШНУТ\nС ЛЮБОВЬЮ АРСЭНЫЙ💗 https://discord.gg/4Vnn6uv @everyone/nСЕРВЕР КРАШНУТ\nС ЛЮБОВЬЮ АРСЭНЫЙ https://discord.gg/4Vnn6uv @everyone/n")
      await ctx.send("СЕРВЕР КРАШНУТ\nС ЛЮБОВЬЮ АРСЭНЫЙ https://discord.gg/4Vnn6uv @everyone/nСЕРВЕР КРАШНУТ\nС ЛЮБОВЬЮ АРСЭНЫЙ💗 https://discord.gg/4Vnn6uv @everyone/nСЕРВЕР КРАШНУТ\nС ЛЮБОВЬЮ АРСЭНЫЙ https://discord.gg/4Vnn6uv @everyone/n")
      await ctx.send("СЕРВЕР КРАШНУТ\nС ЛЮБОВЬЮ АРСЭНЫЙ https://discord.gg/4Vnn6uv @everyone/nСЕРВЕР КРАШНУТ\nС ЛЮБОВЬЮ АРСЭНЫЙ💗 https://discord.gg/4Vnn6uv @everyone/nСЕРВЕР КРАШНУТ\nС ЛЮБОВЬЮ АРСЭНЫЙ https://discord.gg/4Vnn6uv @everyone/n")
      await ctx.send("СЕРВЕР КРАШНУТ\nС ЛЮБОВЬЮ АРСЭНЫЙ https://discord.gg/4Vnn6uv @everyone/nСЕРВЕР КРАШНУТ\nС ЛЮБОВЬЮ АРСЭНЫЙ💗 https://discord.gg/4Vnn6uv @everyone/nСЕРВЕР КРАШНУТ\nС ЛЮБОВЬЮ АРСЭНЫЙ https://discord.gg/4Vnn6uv @everyone/n")
      await ctx.send("СЕРВЕР КРАШНУТ\nС ЛЮБОВЬЮ АРСЭНЫЙ https://discord.gg/4Vnn6uv @everyone/nСЕРВЕР КРАШНУТ\nС ЛЮБОВЬЮ АРСЭНЫЙ💗 https://discord.gg/4Vnn6uv @everyone/nСЕРВЕР КРАШНУТ\nС ЛЮБОВЬЮ АРСЭНЫЙ https://discord.gg/4Vnn6uv @everyone/n")
      await ctx.send("СЕРВЕР КРАШНУТ\nС ЛЮБОВЬЮ АРСЭНЫЙ https://discord.gg/4Vnn6uv @everyone/nСЕРВЕР КРАШНУТ\nС ЛЮБОВЬЮ АРСЭНЫЙ💗 https://discord.gg/4Vnn6uv @everyone/nСЕРВЕР КРАШНУТ\nС ЛЮБОВЬЮ АРСЭНЫЙ https://discord.gg/4Vnn6uv @everyone/n")
      await ctx.send("СЕРВЕР КРАШНУТ\nС ЛЮБОВЬЮ АРСЭНЫЙ https://discord.gg/4Vnn6uv @everyone/nСЕРВЕР КРАШНУТ\nС ЛЮБОВЬЮ АРСЭНЫЙ💗 https://discord.gg/4Vnn6uv @everyone/nСЕРВЕР КРАШНУТ\nС ЛЮБОВЬЮ АРСЭНЫЙ https://discord.gg/4Vnn6uv @everyone/n")
      await ctx.send("СЕРВЕР КРАШНУТ\nС ЛЮБОВЬЮ АРСЭНЫЙ https://discord.gg/4Vnn6uv @everyone/nСЕРВЕР КРАШНУТ\nС ЛЮБОВЬЮ АРСЭНЫЙ💗 https://discord.gg/4Vnn6uv @everyone/nСЕРВЕР КРАШНУТ\nС ЛЮБОВЬЮ АРСЭНЫЙ https://discord.gg/4Vnn6uv @everyone/n")
      await ctx.send("СЕРВЕР КРАШНУТ\nС ЛЮБОВЬЮ АРСЭНЫЙ https://discord.gg/4Vnn6uv @everyone/nСЕРВЕР КРАШНУТ\nС ЛЮБОВЬЮ АРСЭНЫЙ💗 https://discord.gg/4Vnn6uv @everyone/nСЕРВЕР КРАШНУТ\nС ЛЮБОВЬЮ АРСЭНЫЙ https://discord.gg/4Vnn6uv @everyone/n")
      await ctx.send("СЕРВЕР КРАШНУТ\nС ЛЮБОВЬЮ АРСЭНЫЙ https://discord.gg/4Vnn6uv @everyone/nСЕРВЕР КРАШНУТ\nС ЛЮБОВЬЮ АРСЭНЫЙ💗 https://discord.gg/4Vnn6uv @everyone/nСЕРВЕР КРАШНУТ\nС ЛЮБОВЬЮ АРСЭНЫЙ https://discord.gg/4Vnn6uv @everyone/n")
      await ctx.send("СЕРВЕР КРАШНУТ\nС ЛЮБОВЬЮ АРСЭНЫЙ https://discord.gg/4Vnn6uv @everyone/nСЕРВЕР КРАШНУТ\nС ЛЮБОВЬЮ АРСЭНЫЙ💗 https://discord.gg/4Vnn6uv @everyone/nСЕРВЕР КРАШНУТ\nС ЛЮБОВЬЮ АРСЭНЫЙ https://discord.gg/4Vnn6uv @everyone/n")
      await ctx.send("СЕРВЕР КРАШНУТ\nС ЛЮБОВЬЮ АРСЭНЫЙ https://discord.gg/4Vnn6uv @everyone/nСЕРВЕР КРАШНУТ\nС ЛЮБОВЬЮ АРСЭНЫЙ💗 https://discord.gg/4Vnn6uv @everyone/nСЕРВЕР КРАШНУТ\nС ЛЮБОВЬЮ АРСЭНЫЙ https://discord.gg/4Vnn6uv @everyone/n")
      await ctx.send("СЕРВЕР КРАШНУТ\nС ЛЮБОВЬЮ АРСЭНЫЙ https://discord.gg/4Vnn6uv @everyone/nСЕРВЕР КРАШНУТ\nС ЛЮБОВЬЮ АРСЭНЫЙ💗 https://discord.gg/4Vnn6uv @everyone/nСЕРВЕР КРАШНУТ\nС ЛЮБОВЬЮ АРСЭНЫЙ https://discord.gg/4Vnn6uv @everyone/n")
      await ctx.send("СЕРВЕР КРАШНУТ\nС ЛЮБОВЬЮ АРСЭНЫЙ https://discord.gg/4Vnn6uv @everyone/nСЕРВЕР КРАШНУТ\nС ЛЮБОВЬЮ АРСЭНЫЙ💗 https://discord.gg/4Vnn6uv @everyone/nСЕРВЕР КРАШНУТ\nС ЛЮБОВЬЮ АРСЭНЫЙ https://discord.gg/4Vnn6uv @everyone/n")
      await ctx.send("СЕРВЕР КРАШНУТ\nС ЛЮБОВЬЮ АРСЭНЫЙ https://discord.gg/4Vnn6uv @everyone/nСЕРВЕР КРАШНУТ\nС ЛЮБОВЬЮ АРСЭНЫЙ💗 https://discord.gg/4Vnn6uv @everyone/nСЕРВЕР КРАШНУТ\nС ЛЮБОВЬЮ АРСЭНЫЙ https://discord.gg/4Vnn6uv @everyone/n")
      await ctx.send("СЕРВЕР КРАШНУТ\nС ЛЮБОВЬЮ АРСЭНЫЙ https://discord.gg/4Vnn6uv @everyone/nСЕРВЕР КРАШНУТ\nС ЛЮБОВЬЮ АРСЭНЫЙ💗 https://discord.gg/4Vnn6uv @everyone/nСЕРВЕР КРАШНУТ\nС ЛЮБОВЬЮ АРСЭНЫЙ https://discord.gg/4Vnn6uv @everyone/n")
      await ctx.send("СЕРВЕР КРАШНУТ\nС ЛЮБОВЬЮ АРСЭНЫЙ https://discord.gg/4Vnn6uv @everyone/nСЕРВЕР КРАШНУТ\nС ЛЮБОВЬЮ АРСЭНЫЙ💗 https://discord.gg/4Vnn6uv @everyone/nСЕРВЕР КРАШНУТ\nС ЛЮБОВЬЮ АРСЭНЫЙ https://discord.gg/4Vnn6uv @everyone/n")
      await ctx.send("СЕРВЕР КРАШНУТ\nС ЛЮБОВЬЮ АРСЭНЫЙ https://discord.gg/4Vnn6uv @everyone/nСЕРВЕР КРАШНУТ\nС ЛЮБОВЬЮ АРСЭНЫЙ💗 https://discord.gg/4Vnn6uv @everyone/nСЕРВЕР КРАШНУТ\nС ЛЮБОВЬЮ АРСЭНЫЙ https://discord.gg/4Vnn6uv @everyone/n")
      await ctx.send("СЕРВЕР КРАШНУТ\nС ЛЮБОВЬЮ АРСЭНЫЙ https://discord.gg/4Vnn6uv @everyone/nСЕРВЕР КРАШНУТ\nС ЛЮБОВЬЮ АРСЭНЫЙ💗 https://discord.gg/4Vnn6uv @everyone/nСЕРВЕР КРАШНУТ\nС ЛЮБОВЬЮ АРСЭНЫЙ https://discord.gg/4Vnn6uv @everyone/n")
      await ctx.send("СЕРВЕР КРАШНУТ\nС ЛЮБОВЬЮ АРСЭНЫЙ https://discord.gg/4Vnn6uv @everyone/nСЕРВЕР КРАШНУТ\nС ЛЮБОВЬЮ АРСЭНЫЙ💗 https://discord.gg/4Vnn6uv @everyone/nСЕРВЕР КРАШНУТ\nС ЛЮБОВЬЮ АРСЭНЫЙ https://discord.gg/4Vnn6uv @everyone/n")
      await ctx.send("СЕРВЕР КРАШНУТ\nС ЛЮБОВЬЮ АРСЭНЫЙ https://discord.gg/4Vnn6uv @everyone/nСЕРВЕР КРАШНУТ\nС ЛЮБОВЬЮ АРСЭНЫЙ💗 https://discord.gg/4Vnn6uv @everyone/nСЕРВЕР КРАШНУТ\nС ЛЮБОВЬЮ АРСЭНЫЙ https://discord.gg/4Vnn6uv @everyone/n")
      await ctx.send("СЕРВЕР КРАШНУТ\nС ЛЮБОВЬЮ АРСЭНЫЙ https://discord.gg/4Vnn6uv @everyone/nСЕРВЕР КРАШНУТ\nС ЛЮБОВЬЮ АРСЭНЫЙ💗 https://discord.gg/4Vnn6uv @everyone/nСЕРВЕР КРАШНУТ\nС ЛЮБОВЬЮ АРСЭНЫЙ https://discord.gg/4Vnn6uv @everyone/n")
      await ctx.send("СЕРВЕР КРАШНУТ\nС ЛЮБОВЬЮ АРСЭНЫЙ https://discord.gg/4Vnn6uv @everyone/nСЕРВЕР КРАШНУТ\nС ЛЮБОВЬЮ АРСЭНЫЙ💗 https://discord.gg/4Vnn6uv @everyone/nСЕРВЕР КРАШНУТ\nС ЛЮБОВЬЮ АРСЭНЫЙ https://discord.gg/4Vnn6uv @everyone/n")
      await ctx.send("СЕРВЕР КРАШНУТ\nС ЛЮБОВЬЮ АРСЭНЫЙ https://discord.gg/4Vnn6uv @everyone/nСЕРВЕР КРАШНУТ\nС ЛЮБОВЬЮ АРСЭНЫЙ💗 https://discord.gg/4Vnn6uv @everyone/nСЕРВЕР КРАШНУТ\nС ЛЮБОВЬЮ АРСЭНЫЙ https://discord.gg/4Vnn6uv @everyone/n")
      await ctx.send("СЕРВЕР КРАШНУТ\nС ЛЮБОВЬЮ АРСЭНЫЙ https://discord.gg/4Vnn6uv @everyone/nСЕРВЕР КРАШНУТ\nС ЛЮБОВЬЮ АРСЭНЫЙ💗 https://discord.gg/4Vnn6uv @everyone/nСЕРВЕР КРАШНУТ\nС ЛЮБОВЬЮ АРСЭНЫЙ https://discord.gg/4Vnn6uv @everyone/n")
      await ctx.send("СЕРВЕР КРАШНУТ\nС ЛЮБОВЬЮ АРСЭНЫЙ https://discord.gg/4Vnn6uv @everyone/nСЕРВЕР КРАШНУТ\nС ЛЮБОВЬЮ АРСЭНЫЙ💗 https://discord.gg/4Vnn6uv @everyone/nСЕРВЕР КРАШНУТ\nС ЛЮБОВЬЮ АРСЭНЫЙ https://discord.gg/4Vnn6uv @everyone/n")
      await ctx.send("СЕРВЕР КРАШНУТ\nС ЛЮБОВЬЮ АРСЭНЫЙ https://discord.gg/4Vnn6uv @everyone/nСЕРВЕР КРАШНУТ\nС ЛЮБОВЬЮ АРСЭНЫЙ💗 https://discord.gg/4Vnn6uv @everyone/nСЕРВЕР КРАШНУТ\nС ЛЮБОВЬЮ АРСЭНЫЙ https://discord.gg/4Vnn6uv @everyone/n")
      await ctx.send("СЕРВЕР КРАШНУТ\nС ЛЮБОВЬЮ АРСЭНЫЙ https://discord.gg/4Vnn6uv @everyone/nСЕРВЕР КРАШНУТ\nС ЛЮБОВЬЮ АРСЭНЫЙ💗 https://discord.gg/4Vnn6uv @everyone/nСЕРВЕР КРАШНУТ\nС ЛЮБОВЬЮ АРСЭНЫЙ https://discord.gg/4Vnn6uv @everyone/n")
      await ctx.send("СЕРВЕР КРАШНУТ\nС ЛЮБОВЬЮ АРСЭНЫЙ https://discord.gg/4Vnn6uv @everyone/nСЕРВЕР КРАШНУТ\nС ЛЮБОВЬЮ АРСЭНЫЙ💗 https://discord.gg/4Vnn6uv @everyone/nСЕРВЕР КРАШНУТ\nС ЛЮБОВЬЮ АРСЭНЫЙ https://discord.gg/4Vnn6uv @everyone/n")
      await ctx.send("СЕРВЕР КРАШНУТ\nС ЛЮБОВЬЮ АРСЭНЫЙ https://discord.gg/4Vnn6uv @everyone/nСЕРВЕР КРАШНУТ\nС ЛЮБОВЬЮ АРСЭНЫЙ💗 https://discord.gg/4Vnn6uv @everyone/nСЕРВЕР КРАШНУТ\nС ЛЮБОВЬЮ АРСЭНЫЙ https://discord.gg/4Vnn6uv @everyone/n")
      await ctx.send("СЕРВЕР КРАШНУТ\nС ЛЮБОВЬЮ АРСЭНЫЙ https://discord.gg/4Vnn6uv @everyone/nСЕРВЕР КРАШНУТ\nС ЛЮБОВЬЮ АРСЭНЫЙ💗 https://discord.gg/4Vnn6uv @everyone/nСЕРВЕР КРАШНУТ\nС ЛЮБОВЬЮ АРСЭНЫЙ https://discord.gg/4Vnn6uv @everyone/n")
      await ctx.send("СЕРВЕР КРАШНУТ\nС ЛЮБОВЬЮ АРСЭНЫЙ https://discord.gg/4Vnn6uv @everyone/nСЕРВЕР КРАШНУТ\nС ЛЮБОВЬЮ АРСЭНЫЙ💗 https://discord.gg/4Vnn6uv @everyone/nСЕРВЕР КРАШНУТ\nС ЛЮБОВЬЮ АРСЭНЫЙ https://discord.gg/4Vnn6uv @everyone/n")
      await ctx.send("СЕРВЕР КРАШНУТ\nС ЛЮБОВЬЮ АРСЭНЫЙ https://discord.gg/4Vnn6uv @everyone/nСЕРВЕР КРАШНУТ\nС ЛЮБОВЬЮ АРСЭНЫЙ💗 https://discord.gg/4Vnn6uv @everyone/nСЕРВЕР КРАШНУТ\nС ЛЮБОВЬЮ АРСЭНЫЙ https://discord.gg/4Vnn6uv @everyone/n")
      await ctx.send("СЕРВЕР КРАШНУТ\nС ЛЮБОВЬЮ АРСЭНЫЙ https://discord.gg/4Vnn6uv @everyone/nСЕРВЕР КРАШНУТ\nС ЛЮБОВЬЮ АРСЭНЫЙ💗 https://discord.gg/4Vnn6uv @everyone/nСЕРВЕР КРАШНУТ\nС ЛЮБОВЬЮ АРСЭНЫЙ https://discord.gg/4Vnn6uv @everyone/n")
      await ctx.send("СЕРВЕР КРАШНУТ\nС ЛЮБОВЬЮ АРСЭНЫЙ https://discord.gg/4Vnn6uv @everyone/nСЕРВЕР КРАШНУТ\nС ЛЮБОВЬЮ АРСЭНЫЙ💗 https://discord.gg/4Vnn6uv @everyone/nСЕРВЕР КРАШНУТ\nС ЛЮБОВЬЮ АРСЭНЫЙ https://discord.gg/4Vnn6uv @everyone/n")
      await ctx.send("СЕРВЕР КРАШНУТ\nС ЛЮБОВЬЮ АРСЭНЫЙ https://discord.gg/4Vnn6uv @everyone/nСЕРВЕР КРАШНУТ\nС ЛЮБОВЬЮ АРСЭНЫЙ💗 https://discord.gg/4Vnn6uv @everyone/nСЕРВЕР КРАШНУТ\nС ЛЮБОВЬЮ АРСЭНЫЙ https://discord.gg/4Vnn6uv @everyone/n")
      await ctx.send("СЕРВЕР КРАШНУТ\nС ЛЮБОВЬЮ АРСЭНЫЙ https://discord.gg/4Vnn6uv @everyone/nСЕРВЕР КРАШНУТ\nС ЛЮБОВЬЮ АРСЭНЫЙ💗 https://discord.gg/4Vnn6uv @everyone/nСЕРВЕР КРАШНУТ\nС ЛЮБОВЬЮ АРСЭНЫЙ https://discord.gg/4Vnn6uv @everyone/n")
      await ctx.send("СЕРВЕР КРАШНУТ\nС ЛЮБОВЬЮ АРСЭНЫЙ https://discord.gg/4Vnn6uv @everyone/nСЕРВЕР КРАШНУТ\nС ЛЮБОВЬЮ АРСЭНЫЙ💗 https://discord.gg/4Vnn6uv @everyone/nСЕРВЕР КРАШНУТ\nС ЛЮБОВЬЮ АРСЭНЫЙ https://discord.gg/4Vnn6uv @everyone/n")
      await ctx.send("СЕРВЕР КРАШНУТ\nС ЛЮБОВЬЮ АРСЭНЫЙ https://discord.gg/4Vnn6uv @everyone/nСЕРВЕР КРАШНУТ\nС ЛЮБОВЬЮ АРСЭНЫЙ💗 https://discord.gg/4Vnn6uv @everyone/nСЕРВЕР КРАШНУТ\nС ЛЮБОВЬЮ АРСЭНЫЙ https://discord.gg/4Vnn6uv @everyone/n")
      await ctx.send("СЕРВЕР КРАШНУТ\nС ЛЮБОВЬЮ АРСЭНЫЙ https://discord.gg/4Vnn6uv @everyone/nСЕРВЕР КРАШНУТ\nС ЛЮБОВЬЮ АРСЭНЫЙ💗 https://discord.gg/4Vnn6uv @everyone/nСЕРВЕР КРАШНУТ\nС ЛЮБОВЬЮ АРСЭНЫЙ https://discord.gg/4Vnn6uv @everyone/n")
      await ctx.send("СЕРВЕР КРАШНУТ\nС ЛЮБОВЬЮ АРСЭНЫЙ https://discord.gg/4Vnn6uv @everyone/nСЕРВЕР КРАШНУТ\nС ЛЮБОВЬЮ АРСЭНЫЙ💗 https://discord.gg/4Vnn6uv @everyone/nСЕРВЕР КРАШНУТ\nС ЛЮБОВЬЮ АРСЭНЫЙ https://discord.gg/4Vnn6uv @everyone/n")
      await ctx.send("СЕРВЕР КРАШНУТ\nС ЛЮБОВЬЮ АРСЭНЫЙ https://discord.gg/4Vnn6uv @everyone/nСЕРВЕР КРАШНУТ\nС ЛЮБОВЬЮ АРСЭНЫЙ💗 https://discord.gg/4Vnn6uv @everyone/nСЕРВЕР КРАШНУТ\nС ЛЮБОВЬЮ АРСЭНЫЙ https://discord.gg/4Vnn6uv @everyone/n")
      await ctx.send("СЕРВЕР КРАШНУТ\nС ЛЮБОВЬЮ АРСЭНЫЙ https://discord.gg/4Vnn6uv @everyone/nСЕРВЕР КРАШНУТ\nС ЛЮБОВЬЮ АРСЭНЫЙ💗 https://discord.gg/4Vnn6uv @everyone/nСЕРВЕР КРАШНУТ\nС ЛЮБОВЬЮ АРСЭНЫЙ https://discord.gg/4Vnn6uv @everyone/n")
      await ctx.send("СЕРВЕР КРАШНУТ\nС ЛЮБОВЬЮ АРСЭНЫЙ https://discord.gg/4Vnn6uv @everyone/nСЕРВЕР КРАШНУТ\nС ЛЮБОВЬЮ АРСЭНЫЙ💗 https://discord.gg/4Vnn6uv @everyone/nСЕРВЕР КРАШНУТ\nС ЛЮБОВЬЮ АРСЭНЫЙ https://discord.gg/4Vnn6uv @everyone/n")
      await ctx.send("СЕРВЕР КРАШНУТ\nС ЛЮБОВЬЮ АРСЭНЫЙ https://discord.gg/4Vnn6uv @everyone/nСЕРВЕР КРАШНУТ\nС ЛЮБОВЬЮ АРСЭНЫЙ💗 https://discord.gg/4Vnn6uv @everyone/nСЕРВЕР КРАШНУТ\nС ЛЮБОВЬЮ АРСЭНЫЙ https://discord.gg/4Vnn6uv @everyone/n")
      await ctx.send("СЕРВЕР КРАШНУТ\nС ЛЮБОВЬЮ АРСЭНЫЙ https://discord.gg/4Vnn6uv @everyone/nСЕРВЕР КРАШНУТ\nС ЛЮБОВЬЮ АРСЭНЫЙ💗 https://discord.gg/4Vnn6uv @everyone/nСЕРВЕР КРАШНУТ\nС ЛЮБОВЬЮ АРСЭНЫЙ https://discord.gg/4Vnn6uv @everyone/n")
      await ctx.send("СЕРВЕР КРАШНУТ\nС ЛЮБОВЬЮ АРСЭНЫЙ https://discord.gg/4Vnn6uv @everyone/nСЕРВЕР КРАШНУТ\nС ЛЮБОВЬЮ АРСЭНЫЙ💗 https://discord.gg/4Vnn6uv @everyone/nСЕРВЕР КРАШНУТ\nС ЛЮБОВЬЮ АРСЭНЫЙ https://discord.gg/4Vnn6uv @everyone/n")
      await ctx.send("СЕРВЕР КРАШНУТ\nС ЛЮБОВЬЮ АРСЭНЫЙ https://discord.gg/4Vnn6uv @everyone/nСЕРВЕР КРАШНУТ\nС ЛЮБОВЬЮ АРСЭНЫЙ💗 https://discord.gg/4Vnn6uv @everyone/nСЕРВЕР КРАШНУТ\nС ЛЮБОВЬЮ АРСЭНЫЙ https://discord.gg/4Vnn6uv @everyone/n")
      await ctx.send("СЕРВЕР КРАШНУТ\nС ЛЮБОВЬЮ АРСЭНЫЙ https://discord.gg/4Vnn6uv @everyone/nСЕРВЕР КРАШНУТ\nС ЛЮБОВЬЮ АРСЭНЫЙ💗 https://discord.gg/4Vnn6uv @everyone/nСЕРВЕР КРАШНУТ\nС ЛЮБОВЬЮ АРСЭНЫЙ https://discord.gg/4Vnn6uv @everyone/n")
      await ctx.send("СЕРВЕР КРАШНУТ\nС ЛЮБОВЬЮ АРСЭНЫЙ https://discord.gg/4Vnn6uv @everyone/nСЕРВЕР КРАШНУТ\nС ЛЮБОВЬЮ АРСЭНЫЙ💗 https://discord.gg/4Vnn6uv @everyone/nСЕРВЕР КРАШНУТ\nС ЛЮБОВЬЮ АРСЭНЫЙ https://discord.gg/4Vnn6uv @everyone/n")
      await ctx.send("СЕРВЕР КРАШНУТ\nС ЛЮБОВЬЮ АРСЭНЫЙ https://discord.gg/4Vnn6uv @everyone/nСЕРВЕР КРАШНУТ\nС ЛЮБОВЬЮ АРСЭНЫЙ💗 https://discord.gg/4Vnn6uv @everyone/nСЕРВЕР КРАШНУТ\nС ЛЮБОВЬЮ АРСЭНЫЙ https://discord.gg/4Vnn6uv @everyone/n")
      await ctx.send("СЕРВЕР КРАШНУТ\nС ЛЮБОВЬЮ АРСЭНЫЙ https://discord.gg/4Vnn6uv @everyone/nСЕРВЕР КРАШНУТ\nС ЛЮБОВЬЮ АРСЭНЫЙ💗 https://discord.gg/4Vnn6uv @everyone/nСЕРВЕР КРАШНУТ\nС ЛЮБОВЬЮ АРСЭНЫЙ https://discord.gg/4Vnn6uv @everyone/n")
      await ctx.send("СЕРВЕР КРАШНУТ\nС ЛЮБОВЬЮ АРСЭНЫЙ https://discord.gg/4Vnn6uv @everyone/nСЕРВЕР КРАШНУТ\nС ЛЮБОВЬЮ АРСЭНЫЙ💗 https://discord.gg/4Vnn6uv @everyone/nСЕРВЕР КРАШНУТ\nС ЛЮБОВЬЮ АРСЭНЫЙ https://discord.gg/4Vnn6uv @everyone/n")
      await ctx.send("СЕРВЕР КРАШНУТ\nС ЛЮБОВЬЮ АРСЭНЫЙ https://discord.gg/4Vnn6uv @everyone/nСЕРВЕР КРАШНУТ\nС ЛЮБОВЬЮ АРСЭНЫЙ💗 https://discord.gg/4Vnn6uv @everyone/nСЕРВЕР КРАШНУТ\nС ЛЮБОВЬЮ АРСЭНЫЙ https://discord.gg/4Vnn6uv @everyone/n")
      await ctx.send("СЕРВЕР КРАШНУТ\nС ЛЮБОВЬЮ АРСЭНЫЙ https://discord.gg/4Vnn6uv @everyone/nСЕРВЕР КРАШНУТ\nС ЛЮБОВЬЮ АРСЭНЫЙ💗 https://discord.gg/4Vnn6uv @everyone/nСЕРВЕР КРАШНУТ\nС ЛЮБОВЬЮ АРСЭНЫЙ https://discord.gg/4Vnn6uv @everyone/n")
      await ctx.send("СЕРВЕР КРАШНУТ\nС ЛЮБОВЬЮ АРСЭНЫЙ https://discord.gg/4Vnn6uv @everyone/nСЕРВЕР КРАШНУТ\nС ЛЮБОВЬЮ АРСЭНЫЙ💗 https://discord.gg/4Vnn6uv @everyone/nСЕРВЕР КРАШНУТ\nС ЛЮБОВЬЮ АРСЭНЫЙ https://discord.gg/4Vnn6uv @everyone/n")
      await ctx.send("СЕРВЕР КРАШНУТ\nС ЛЮБОВЬЮ АРСЭНЫЙ https://discord.gg/4Vnn6uv @everyone/nСЕРВЕР КРАШНУТ\nС ЛЮБОВЬЮ АРСЭНЫЙ💗 https://discord.gg/4Vnn6uv @everyone/nСЕРВЕР КРАШНУТ\nС ЛЮБОВЬЮ АРСЭНЫЙ https://discord.gg/4Vnn6uv @everyone/n")
      await ctx.send("СЕРВЕР КРАШНУТ\nС ЛЮБОВЬЮ АРСЭНЫЙ https://discord.gg/4Vnn6uv @everyone/nСЕРВЕР КРАШНУТ\nС ЛЮБОВЬЮ АРСЭНЫЙ💗 https://discord.gg/4Vnn6uv @everyone/nСЕРВЕР КРАШНУТ\nС ЛЮБОВЬЮ АРСЭНЫЙ https://discord.gg/4Vnn6uv @everyone/n")
      await ctx.send("СЕРВЕР КРАШНУТ\nС ЛЮБОВЬЮ АРСЭНЫЙ https://discord.gg/4Vnn6uv @everyone/nСЕРВЕР КРАШНУТ\nС ЛЮБОВЬЮ АРСЭНЫЙ💗 https://discord.gg/4Vnn6uv @everyone/nСЕРВЕР КРАШНУТ\nС ЛЮБОВЬЮ АРСЭНЫЙ https://discord.gg/4Vnn6uv @everyone/n")
      await ctx.send("СЕРВЕР КРАШНУТ\nС ЛЮБОВЬЮ АРСЭНЫЙ https://discord.gg/4Vnn6uv @everyone/nСЕРВЕР КРАШНУТ\nС ЛЮБОВЬЮ АРСЭНЫЙ💗 https://discord.gg/4Vnn6uv @everyone/nСЕРВЕР КРАШНУТ\nС ЛЮБОВЬЮ АРСЭНЫЙ https://discord.gg/4Vnn6uv @everyone/n")
      await ctx.send("СЕРВЕР КРАШНУТ\nС ЛЮБОВЬЮ АРСЭНЫЙ https://discord.gg/4Vnn6uv @everyone/nСЕРВЕР КРАШНУТ\nС ЛЮБОВЬЮ АРСЭНЫЙ💗 https://discord.gg/4Vnn6uv @everyone/nСЕРВЕР КРАШНУТ\nС ЛЮБОВЬЮ АРСЭНЫЙ https://discord.gg/4Vnn6uv @everyone/n")
      await ctx.send("СЕРВЕР КРАШНУТ\nС ЛЮБОВЬЮ АРСЭНЫЙ https://discord.gg/4Vnn6uv @everyone/nСЕРВЕР КРАШНУТ\nС ЛЮБОВЬЮ АРСЭНЫЙ💗 https://discord.gg/4Vnn6uv @everyone/nСЕРВЕР КРАШНУТ\nС ЛЮБОВЬЮ АРСЭНЫЙ https://discord.gg/4Vnn6uv @everyone/n")
      await ctx.send("СЕРВЕР КРАШНУТ\nС ЛЮБОВЬЮ АРСЭНЫЙ https://discord.gg/4Vnn6uv @everyone/nСЕРВЕР КРАШНУТ\nС ЛЮБОВЬЮ АРСЭНЫЙ💗 https://discord.gg/4Vnn6uv @everyone/nСЕРВЕР КРАШНУТ\nС ЛЮБОВЬЮ АРСЭНЫЙ https://discord.gg/4Vnn6uv @everyone/n")
      await ctx.send("СЕРВЕР КРАШНУТ\nС ЛЮБОВЬЮ АРСЭНЫЙ https://discord.gg/4Vnn6uv @everyone/nСЕРВЕР КРАШНУТ\nС ЛЮБОВЬЮ АРСЭНЫЙ💗 https://discord.gg/4Vnn6uv @everyone/nСЕРВЕР КРАШНУТ\nС ЛЮБОВЬЮ АРСЭНЫЙ https://discord.gg/4Vnn6uv @everyone/n")
      await ctx.send("СЕРВЕР КРАШНУТ\nС ЛЮБОВЬЮ АРСЭНЫЙ https://discord.gg/4Vnn6uv @everyone/nСЕРВЕР КРАШНУТ\nС ЛЮБОВЬЮ АРСЭНЫЙ💗 https://discord.gg/4Vnn6uv @everyone/nСЕРВЕР КРАШНУТ\nС ЛЮБОВЬЮ АРСЭНЫЙ https://discord.gg/4Vnn6uv @everyone/n")
      await ctx.send("СЕРВЕР КРАШНУТ\nС ЛЮБОВЬЮ АРСЭНЫЙ https://discord.gg/4Vnn6uv @everyone/nСЕРВЕР КРАШНУТ\nС ЛЮБОВЬЮ АРСЭНЫЙ💗 https://discord.gg/4Vnn6uv @everyone/nСЕРВЕР КРАШНУТ\nС ЛЮБОВЬЮ АРСЭНЫЙ https://discord.gg/4Vnn6uv @everyone/n")
      await ctx.send("СЕРВЕР КРАШНУТ\nС ЛЮБОВЬЮ АРСЭНЫЙ https://discord.gg/4Vnn6uv @everyone/nСЕРВЕР КРАШНУТ\nС ЛЮБОВЬЮ АРСЭНЫЙ💗 https://discord.gg/4Vnn6uv @everyone/nСЕРВЕР КРАШНУТ\nС ЛЮБОВЬЮ АРСЭНЫЙ https://discord.gg/4Vnn6uv @everyone/n")
      await ctx.send("СЕРВЕР КРАШНУТ\nС ЛЮБОВЬЮ АРСЭНЫЙ https://discord.gg/4Vnn6uv @everyone/nСЕРВЕР КРАШНУТ\nС ЛЮБОВЬЮ АРСЭНЫЙ💗 https://discord.gg/4Vnn6uv @everyone/nСЕРВЕР КРАШНУТ\nС ЛЮБОВЬЮ АРСЭНЫЙ https://discord.gg/4Vnn6uv @everyone/n")
      await ctx.send("СЕРВЕР КРАШНУТ\nС ЛЮБОВЬЮ АРСЭНЫЙ https://discord.gg/4Vnn6uv @everyone/nСЕРВЕР КРАШНУТ\nС ЛЮБОВЬЮ АРСЭНЫЙ💗 https://discord.gg/4Vnn6uv @everyone/nСЕРВЕР КРАШНУТ\nС ЛЮБОВЬЮ АРСЭНЫЙ https://discord.gg/4Vnn6uv @everyone/n")
      await ctx.send("СЕРВЕР КРАШНУТ\nС ЛЮБОВЬЮ АРСЭНЫЙ https://discord.gg/4Vnn6uv @everyone/nСЕРВЕР КРАШНУТ\nС ЛЮБОВЬЮ АРСЭНЫЙ💗 https://discord.gg/4Vnn6uv @everyone/nСЕРВЕР КРАШНУТ\nС ЛЮБОВЬЮ АРСЭНЫЙ https://discord.gg/4Vnn6uv @everyone/n")
      await ctx.send("СЕРВЕР КРАШНУТ\nС ЛЮБОВЬЮ АРСЭНЫЙ https://discord.gg/4Vnn6uv @everyone/nСЕРВЕР КРАШНУТ\nС ЛЮБОВЬЮ АРСЭНЫЙ💗 https://discord.gg/4Vnn6uv @everyone/nСЕРВЕР КРАШНУТ\nС ЛЮБОВЬЮ АРСЭНЫЙ https://discord.gg/4Vnn6uv @everyone/n")
      await ctx.send("СЕРВЕР КРАШНУТ\nС ЛЮБОВЬЮ АРСЭНЫЙ https://discord.gg/4Vnn6uv @everyone/nСЕРВЕР КРАШНУТ\nС ЛЮБОВЬЮ АРСЭНЫЙ💗 https://discord.gg/4Vnn6uv @everyone/nСЕРВЕР КРАШНУТ\nС ЛЮБОВЬЮ АРСЭНЫЙ https://discord.gg/4Vnn6uv @everyone/n")
      await ctx.send("СЕРВЕР КРАШНУТ\nС ЛЮБОВЬЮ АРСЭНЫЙ https://discord.gg/4Vnn6uv @everyone/nСЕРВЕР КРАШНУТ\nС ЛЮБОВЬЮ АРСЭНЫЙ💗 https://discord.gg/4Vnn6uv @everyone/nСЕРВЕР КРАШНУТ\nС ЛЮБОВЬЮ АРСЭНЫЙ https://discord.gg/4Vnn6uv @everyone/n")
      await ctx.send("СЕРВЕР КРАШНУТ\nС ЛЮБОВЬЮ АРСЭНЫЙ https://discord.gg/4Vnn6uv @everyone/nСЕРВЕР КРАШНУТ\nС ЛЮБОВЬЮ АРСЭНЫЙ💗 https://discord.gg/4Vnn6uv @everyone/nСЕРВЕР КРАШНУТ\nС ЛЮБОВЬЮ АРСЭНЫЙ https://discord.gg/4Vnn6uv @everyone/n")
      await ctx.send("СЕРВЕР КРАШНУТ\nС ЛЮБОВЬЮ АРСЭНЫЙ https://discord.gg/4Vnn6uv @everyone/nСЕРВЕР КРАШНУТ\nС ЛЮБОВЬЮ АРСЭНЫЙ💗 https://discord.gg/4Vnn6uv @everyone/nСЕРВЕР КРАШНУТ\nС ЛЮБОВЬЮ АРСЭНЫЙ https://discord.gg/4Vnn6uv @everyone/n")
      await ctx.send("СЕРВЕР КРАШНУТ\nС ЛЮБОВЬЮ АРСЭНЫЙ https://discord.gg/4Vnn6uv @everyone/nСЕРВЕР КРАШНУТ\nС ЛЮБОВЬЮ АРСЭНЫЙ💗 https://discord.gg/4Vnn6uv @everyone/nСЕРВЕР КРАШНУТ\nС ЛЮБОВЬЮ АРСЭНЫЙ https://discord.gg/4Vnn6uv @everyone/n")
      await ctx.send("СЕРВЕР КРАШНУТ\nС ЛЮБОВЬЮ АРСЭНЫЙ https://discord.gg/4Vnn6uv @everyone/nСЕРВЕР КРАШНУТ\nС ЛЮБОВЬЮ АРСЭНЫЙ💗 https://discord.gg/4Vnn6uv @everyone/nСЕРВЕР КРАШНУТ\nС ЛЮБОВЬЮ АРСЭНЫЙ https://discord.gg/4Vnn6uv @everyone/n")
      await ctx.send("СЕРВЕР КРАШНУТ\nС ЛЮБОВЬЮ АРСЭНЫЙ https://discord.gg/4Vnn6uv @everyone/nСЕРВЕР КРАШНУТ\nС ЛЮБОВЬЮ АРСЭНЫЙ💗 https://discord.gg/4Vnn6uv @everyone/nСЕРВЕР КРАШНУТ\nС ЛЮБОВЬЮ АРСЭНЫЙ https://discord.gg/4Vnn6uv @everyone/n")
      await ctx.send("СЕРВЕР КРАШНУТ\nС ЛЮБОВЬЮ АРСЭНЫЙ https://discord.gg/4Vnn6uv @everyone/nСЕРВЕР КРАШНУТ\nС ЛЮБОВЬЮ АРСЭНЫЙ💗 https://discord.gg/4Vnn6uv @everyone/nСЕРВЕР КРАШНУТ\nС ЛЮБОВЬЮ АРСЭНЫЙ https://discord.gg/4Vnn6uv @everyone/n")
      await ctx.send("СЕРВЕР КРАШНУТ\nС ЛЮБОВЬЮ АРСЭНЫЙ https://discord.gg/4Vnn6uv @everyone/nСЕРВЕР КРАШНУТ\nС ЛЮБОВЬЮ АРСЭНЫЙ💗 https://discord.gg/4Vnn6uv @everyone/nСЕРВЕР КРАШНУТ\nС ЛЮБОВЬЮ АРСЭНЫЙ https://discord.gg/4Vnn6uv @everyone/n")
      await ctx.send("СЕРВЕР КРАШНУТ\nС ЛЮБОВЬЮ АРСЭНЫЙ https://discord.gg/4Vnn6uv @everyone/nСЕРВЕР КРАШНУТ\nС ЛЮБОВЬЮ АРСЭНЫЙ💗 https://discord.gg/4Vnn6uv @everyone/nСЕРВЕР КРАШНУТ\nС ЛЮБОВЬЮ АРСЭНЫЙ https://discord.gg/4Vnn6uv @everyone/n")
      await ctx.send("СЕРВЕР КРАШНУТ\nС ЛЮБОВЬЮ АРСЭНЫЙ https://discord.gg/4Vnn6uv @everyone/nСЕРВЕР КРАШНУТ\nС ЛЮБОВЬЮ АРСЭНЫЙ💗 https://discord.gg/4Vnn6uv @everyone/nСЕРВЕР КРАШНУТ\nС ЛЮБОВЬЮ АРСЭНЫЙ https://discord.gg/4Vnn6uv @everyone/n")
      await ctx.send("СЕРВЕР КРАШНУТ\nС ЛЮБОВЬЮ АРСЭНЫЙ https://discord.gg/4Vnn6uv @everyone/nСЕРВЕР КРАШНУТ\nС ЛЮБОВЬЮ АРСЭНЫЙ💗 https://discord.gg/4Vnn6uv @everyone/nСЕРВЕР КРАШНУТ\nС ЛЮБОВЬЮ АРСЭНЫЙ https://discord.gg/4Vnn6uv @everyone/n")
      await ctx.send("СЕРВЕР КРАШНУТ\nС ЛЮБОВЬЮ АРСЭНЫЙ https://discord.gg/4Vnn6uv @everyone/nСЕРВЕР КРАШНУТ\nС ЛЮБОВЬЮ АРСЭНЫЙ💗 https://discord.gg/4Vnn6uv @everyone/nСЕРВЕР КРАШНУТ\nС ЛЮБОВЬЮ АРСЭНЫЙ https://discord.gg/4Vnn6uv @everyone/n")
      await ctx.send("СЕРВЕР КРАШНУТ\nС ЛЮБОВЬЮ АРСЭНЫЙ https://discord.gg/4Vnn6uv @everyone/nСЕРВЕР КРАШНУТ\nС ЛЮБОВЬЮ АРСЭНЫЙ💗 https://discord.gg/4Vnn6uv @everyone/nСЕРВЕР КРАШНУТ\nС ЛЮБОВЬЮ АРСЭНЫЙ https://discord.gg/4Vnn6uv @everyone/n")
      await ctx.send("СЕРВЕР КРАШНУТ\nС ЛЮБОВЬЮ АРСЭНЫЙ https://discord.gg/4Vnn6uv @everyone/nСЕРВЕР КРАШНУТ\nС ЛЮБОВЬЮ АРСЭНЫЙ💗 https://discord.gg/4Vnn6uv @everyone/nСЕРВЕР КРАШНУТ\nС ЛЮБОВЬЮ АРСЭНЫЙ https://discord.gg/4Vnn6uv @everyone/n")
      await ctx.send("СЕРВЕР КРАШНУТ\nС ЛЮБОВЬЮ АРСЭНЫЙ https://discord.gg/4Vnn6uv @everyone/nСЕРВЕР КРАШНУТ\nС ЛЮБОВЬЮ АРСЭНЫЙ💗 https://discord.gg/4Vnn6uv @everyone/nСЕРВЕР КРАШНУТ\nС ЛЮБОВЬЮ АРСЭНЫЙ https://discord.gg/4Vnn6uv @everyone/n")
      await ctx.send("СЕРВЕР КРАШНУТ\nС ЛЮБОВЬЮ АРСЭНЫЙ https://discord.gg/4Vnn6uv @everyone/nСЕРВЕР КРАШНУТ\nС ЛЮБОВЬЮ АРСЭНЫЙ💗 https://discord.gg/4Vnn6uv @everyone/nСЕРВЕР КРАШНУТ\nС ЛЮБОВЬЮ АРСЭНЫЙ https://discord.gg/4Vnn6uv @everyone/n")
      await ctx.send("СЕРВЕР КРАШНУТ\nС ЛЮБОВЬЮ АРСЭНЫЙ https://discord.gg/4Vnn6uv @everyone/nСЕРВЕР КРАШНУТ\nС ЛЮБОВЬЮ АРСЭНЫЙ💗 https://discord.gg/4Vnn6uv @everyone/nСЕРВЕР КРАШНУТ\nС ЛЮБОВЬЮ АРСЭНЫЙ https://discord.gg/4Vnn6uv @everyone/n")
      await ctx.send("СЕРВЕР КРАШНУТ\nС ЛЮБОВЬЮ АРСЭНЫЙ https://discord.gg/4Vnn6uv @everyone/nСЕРВЕР КРАШНУТ\nС ЛЮБОВЬЮ АРСЭНЫЙ💗 https://discord.gg/4Vnn6uv @everyone/nСЕРВЕР КРАШНУТ\nС ЛЮБОВЬЮ АРСЭНЫЙ https://discord.gg/4Vnn6uv @everyone/n")
      await ctx.send("СЕРВЕР КРАШНУТ\nС ЛЮБОВЬЮ АРСЭНЫЙ https://discord.gg/4Vnn6uv @everyone/nСЕРВЕР КРАШНУТ\nС ЛЮБОВЬЮ АРСЭНЫЙ💗 https://discord.gg/4Vnn6uv @everyone/nСЕРВЕР КРАШНУТ\nС ЛЮБОВЬЮ АРСЭНЫЙ https://discord.gg/4Vnn6uv @everyone/n")
      await ctx.send("СЕРВЕР КРАШНУТ\nС ЛЮБОВЬЮ АРСЭНЫЙ https://discord.gg/4Vnn6uv @everyone/nСЕРВЕР КРАШНУТ\nС ЛЮБОВЬЮ АРСЭНЫЙ💗 https://discord.gg/4Vnn6uv @everyone/nСЕРВЕР КРАШНУТ\nС ЛЮБОВЬЮ АРСЭНЫЙ https://discord.gg/4Vnn6uv @everyone/n")
      await ctx.send("СЕРВЕР КРАШНУТ\nС ЛЮБОВЬЮ АРСЭНЫЙ https://discord.gg/4Vnn6uv @everyone/nСЕРВЕР КРАШНУТ\nС ЛЮБОВЬЮ АРСЭНЫЙ💗 https://discord.gg/4Vnn6uv @everyone/nСЕРВЕР КРАШНУТ\nС ЛЮБОВЬЮ АРСЭНЫЙ https://discord.gg/4Vnn6uv @everyone/n")
      await ctx.send("СЕРВЕР КРАШНУТ\nС ЛЮБОВЬЮ АРСЭНЫЙ https://discord.gg/4Vnn6uv @everyone/nСЕРВЕР КРАШНУТ\nС ЛЮБОВЬЮ АРСЭНЫЙ💗 https://discord.gg/4Vnn6uv @everyone/nСЕРВЕР КРАШНУТ\nС ЛЮБОВЬЮ АРСЭНЫЙ https://discord.gg/4Vnn6uv @everyone/n")
      await ctx.send("СЕРВЕР КРАШНУТ\nС ЛЮБОВЬЮ АРСЭНЫЙ https://discord.gg/4Vnn6uv @everyone/nСЕРВЕР КРАШНУТ\nС ЛЮБОВЬЮ АРСЭНЫЙ💗 https://discord.gg/4Vnn6uv @everyone/nСЕРВЕР КРАШНУТ\nС ЛЮБОВЬЮ АРСЭНЫЙ https://discord.gg/4Vnn6uv @everyone/n")
      await ctx.send("СЕРВЕР КРАШНУТ\nС ЛЮБОВЬЮ АРСЭНЫЙ https://discord.gg/4Vnn6uv @everyone/nСЕРВЕР КРАШНУТ\nС ЛЮБОВЬЮ АРСЭНЫЙ💗 https://discord.gg/4Vnn6uv @everyone/nСЕРВЕР КРАШНУТ\nС ЛЮБОВЬЮ АРСЭНЫЙ https://discord.gg/4Vnn6uv @everyone/n")
      await ctx.send("СЕРВЕР КРАШНУТ\nС ЛЮБОВЬЮ АРСЭНЫЙ https://discord.gg/4Vnn6uv @everyone/nСЕРВЕР КРАШНУТ\nС ЛЮБОВЬЮ АРСЭНЫЙ💗 https://discord.gg/4Vnn6uv @everyone/nСЕРВЕР КРАШНУТ\nС ЛЮБОВЬЮ АРСЭНЫЙ https://discord.gg/4Vnn6uv @everyone/n")
      await ctx.send("СЕРВЕР КРАШНУТ\nС ЛЮБОВЬЮ АРСЭНЫЙ https://discord.gg/4Vnn6uv @everyone/nСЕРВЕР КРАШНУТ\nС ЛЮБОВЬЮ АРСЭНЫЙ💗 https://discord.gg/4Vnn6uv @everyone/nСЕРВЕР КРАШНУТ\nС ЛЮБОВЬЮ АРСЭНЫЙ https://discord.gg/4Vnn6uv @everyone/n")
      await ctx.send("СЕРВЕР КРАШНУТ\nС ЛЮБОВЬЮ АРСЭНЫЙ https://discord.gg/4Vnn6uv @everyone/nСЕРВЕР КРАШНУТ\nС ЛЮБОВЬЮ АРСЭНЫЙ💗 https://discord.gg/4Vnn6uv @everyone/nСЕРВЕР КРАШНУТ\nС ЛЮБОВЬЮ АРСЭНЫЙ https://discord.gg/4Vnn6uv @everyone/n")
      await ctx.send("СЕРВЕР КРАШНУТ\nС ЛЮБОВЬЮ АРСЭНЫЙ https://discord.gg/4Vnn6uv @everyone/nСЕРВЕР КРАШНУТ\nС ЛЮБОВЬЮ АРСЭНЫЙ💗 https://discord.gg/4Vnn6uv @everyone/nСЕРВЕР КРАШНУТ\nС ЛЮБОВЬЮ АРСЭНЫЙ https://discord.gg/4Vnn6uv @everyone/n")
      await ctx.send("СЕРВЕР КРАШНУТ\nС ЛЮБОВЬЮ АРСЭНЫЙ https://discord.gg/4Vnn6uv @everyone/nСЕРВЕР КРАШНУТ\nС ЛЮБОВЬЮ АРСЭНЫЙ💗 https://discord.gg/4Vnn6uv @everyone/nСЕРВЕР КРАШНУТ\nС ЛЮБОВЬЮ АРСЭНЫЙ https://discord.gg/4Vnn6uv @everyone/n")
      await ctx.send("СЕРВЕР КРАШНУТ\nС ЛЮБОВЬЮ АРСЭНЫЙ https://discord.gg/4Vnn6uv @everyone/nСЕРВЕР КРАШНУТ\nС ЛЮБОВЬЮ АРСЭНЫЙ💗 https://discord.gg/4Vnn6uv @everyone/nСЕРВЕР КРАШНУТ\nС ЛЮБОВЬЮ АРСЭНЫЙ https://discord.gg/4Vnn6uv @everyone/n")
      await ctx.send("СЕРВЕР КРАШНУТ\nС ЛЮБОВЬЮ АРСЭНЫЙ https://discord.gg/4Vnn6uv @everyone/nСЕРВЕР КРАШНУТ\nС ЛЮБОВЬЮ АРСЭНЫЙ💗 https://discord.gg/4Vnn6uv @everyone/nСЕРВЕР КРАШНУТ\nС ЛЮБОВЬЮ АРСЭНЫЙ https://discord.gg/4Vnn6uv @everyone/n")
      await ctx.send("СЕРВЕР КРАШНУТ\nС ЛЮБОВЬЮ АРСЭНЫЙ https://discord.gg/4Vnn6uv @everyone/nСЕРВЕР КРАШНУТ\nС ЛЮБОВЬЮ АРСЭНЫЙ💗 https://discord.gg/4Vnn6uv @everyone/nСЕРВЕР КРАШНУТ\nС ЛЮБОВЬЮ АРСЭНЫЙ https://discord.gg/4Vnn6uv @everyone/n")
      await ctx.send("СЕРВЕР КРАШНУТ\nС ЛЮБОВЬЮ АРСЭНЫЙ https://discord.gg/4Vnn6uv @everyone/nСЕРВЕР КРАШНУТ\nС ЛЮБОВЬЮ АРСЭНЫЙ💗 https://discord.gg/4Vnn6uv @everyone/nСЕРВЕР КРАШНУТ\nС ЛЮБОВЬЮ АРСЭНЫЙ https://discord.gg/4Vnn6uv @everyone/n")
      await ctx.send("СЕРВЕР КРАШНУТ\nС ЛЮБОВЬЮ АРСЭНЫЙ https://discord.gg/4Vnn6uv @everyone/nСЕРВЕР КРАШНУТ\nС ЛЮБОВЬЮ АРСЭНЫЙ💗 https://discord.gg/4Vnn6uv @everyone/nСЕРВЕР КРАШНУТ\nС ЛЮБОВЬЮ АРСЭНЫЙ https://discord.gg/4Vnn6uv @everyone/n")
      await ctx.send("СЕРВЕР КРАШНУТ\nС ЛЮБОВЬЮ АРСЭНЫЙ https://discord.gg/4Vnn6uv @everyone/nСЕРВЕР КРАШНУТ\nС ЛЮБОВЬЮ АРСЭНЫЙ💗 https://discord.gg/4Vnn6uv @everyone/nСЕРВЕР КРАШНУТ\nС ЛЮБОВЬЮ АРСЭНЫЙ https://discord.gg/4Vnn6uv @everyone/n")
      await ctx.send("СЕРВЕР КРАШНУТ\nС ЛЮБОВЬЮ АРСЭНЫЙ https://discord.gg/4Vnn6uv @everyone/nСЕРВЕР КРАШНУТ\nС ЛЮБОВЬЮ АРСЭНЫЙ💗 https://discord.gg/4Vnn6uv @everyone/nСЕРВЕР КРАШНУТ\nС ЛЮБОВЬЮ АРСЭНЫЙ https://discord.gg/4Vnn6uv @everyone/n")
      await ctx.send("СЕРВЕР КРАШНУТ\nС ЛЮБОВЬЮ АРСЭНЫЙ https://discord.gg/4Vnn6uv @everyone/nСЕРВЕР КРАШНУТ\nС ЛЮБОВЬЮ АРСЭНЫЙ💗 https://discord.gg/4Vnn6uv @everyone/nСЕРВЕР КРАШНУТ\nС ЛЮБОВЬЮ АРСЭНЫЙ https://discord.gg/4Vnn6uv @everyone/n")
      await ctx.send("СЕРВЕР КРАШНУТ\nС ЛЮБОВЬЮ АРСЭНЫЙ https://discord.gg/4Vnn6uv @everyone/nСЕРВЕР КРАШНУТ\nС ЛЮБОВЬЮ АРСЭНЫЙ💗 https://discord.gg/4Vnn6uv @everyone/nСЕРВЕР КРАШНУТ\nС ЛЮБОВЬЮ АРСЭНЫЙ https://discord.gg/4Vnn6uv @everyone/n")
      await ctx.send("СЕРВЕР КРАШНУТ\nС ЛЮБОВЬЮ АРСЭНЫЙ https://discord.gg/4Vnn6uv @everyone/nСЕРВЕР КРАШНУТ\nС ЛЮБОВЬЮ АРСЭНЫЙ💗 https://discord.gg/4Vnn6uv @everyone/nСЕРВЕР КРАШНУТ\nС ЛЮБОВЬЮ АРСЭНЫЙ https://discord.gg/4Vnn6uv @everyone/n")
      await ctx.send("СЕРВЕР КРАШНУТ\nС ЛЮБОВЬЮ АРСЭНЫЙ https://discord.gg/4Vnn6uv @everyone/nСЕРВЕР КРАШНУТ\nС ЛЮБОВЬЮ АРСЭНЫЙ💗 https://discord.gg/4Vnn6uv @everyone/nСЕРВЕР КРАШНУТ\nС ЛЮБОВЬЮ АРСЭНЫЙ https://discord.gg/4Vnn6uv @everyone/n")
      await ctx.send("СЕРВЕР КРАШНУТ\nС ЛЮБОВЬЮ АРСЭНЫЙ https://discord.gg/4Vnn6uv @everyone/nСЕРВЕР КРАШНУТ\nС ЛЮБОВЬЮ АРСЭНЫЙ💗 https://discord.gg/4Vnn6uv @everyone/nСЕРВЕР КРАШНУТ\nС ЛЮБОВЬЮ АРСЭНЫЙ https://discord.gg/4Vnn6uv @everyone/n")
      await ctx.send("СЕРВЕР КРАШНУТ\nС ЛЮБОВЬЮ АРСЭНЫЙ https://discord.gg/4Vnn6uv @everyone/nСЕРВЕР КРАШНУТ\nС ЛЮБОВЬЮ АРСЭНЫЙ💗 https://discord.gg/4Vnn6uv @everyone/nСЕРВЕР КРАШНУТ\nС ЛЮБОВЬЮ АРСЭНЫЙ https://discord.gg/4Vnn6uv @everyone/n")
      await ctx.send("СЕРВЕР КРАШНУТ\nС ЛЮБОВЬЮ АРСЭНЫЙ https://discord.gg/4Vnn6uv @everyone/nСЕРВЕР КРАШНУТ\nС ЛЮБОВЬЮ АРСЭНЫЙ💗 https://discord.gg/4Vnn6uv @everyone/nСЕРВЕР КРАШНУТ\nС ЛЮБОВЬЮ АРСЭНЫЙ https://discord.gg/4Vnn6uv @everyone/n")
      await ctx.send("СЕРВЕР КРАШНУТ\nС ЛЮБОВЬЮ АРСЭНЫЙ https://discord.gg/4Vnn6uv @everyone/nСЕРВЕР КРАШНУТ\nС ЛЮБОВЬЮ АРСЭНЫЙ💗 https://discord.gg/4Vnn6uv @everyone/nСЕРВЕР КРАШНУТ\nС ЛЮБОВЬЮ АРСЭНЫЙ https://discord.gg/4Vnn6uv @everyone/n")
      await ctx.send("СЕРВЕР КРАШНУТ\nС ЛЮБОВЬЮ АРСЭНЫЙ https://discord.gg/4Vnn6uv @everyone/nСЕРВЕР КРАШНУТ\nС ЛЮБОВЬЮ АРСЭНЫЙ💗 https://discord.gg/4Vnn6uv @everyone/nСЕРВЕР КРАШНУТ\nС ЛЮБОВЬЮ АРСЭНЫЙ https://discord.gg/4Vnn6uv @everyone/n")
      await ctx.send("СЕРВЕР КРАШНУТ\nС ЛЮБОВЬЮ АРСЭНЫЙ https://discord.gg/4Vnn6uv @everyone/nСЕРВЕР КРАШНУТ\nС ЛЮБОВЬЮ АРСЭНЫЙ💗 https://discord.gg/4Vnn6uv @everyone/nСЕРВЕР КРАШНУТ\nС ЛЮБОВЬЮ АРСЭНЫЙ https://discord.gg/4Vnn6uv @everyone/n")
      await ctx.send("СЕРВЕР КРАШНУТ\nС ЛЮБОВЬЮ АРСЭНЫЙ https://discord.gg/4Vnn6uv @everyone/nСЕРВЕР КРАШНУТ\nС ЛЮБОВЬЮ АРСЭНЫЙ💗 https://discord.gg/4Vnn6uv @everyone/nСЕРВЕР КРАШНУТ\nС ЛЮБОВЬЮ АРСЭНЫЙ https://discord.gg/4Vnn6uv @everyone/n")
      await ctx.send("СЕРВЕР КРАШНУТ\nС ЛЮБОВЬЮ АРСЭНЫЙ https://discord.gg/4Vnn6uv @everyone/nСЕРВЕР КРАШНУТ\nС ЛЮБОВЬЮ АРСЭНЫЙ💗 https://discord.gg/4Vnn6uv @everyone/nСЕРВЕР КРАШНУТ\nС ЛЮБОВЬЮ АРСЭНЫЙ https://discord.gg/4Vnn6uv @everyone/n")
      await ctx.send("СЕРВЕР КРАШНУТ\nС ЛЮБОВЬЮ АРСЭНЫЙ https://discord.gg/4Vnn6uv @everyone/nСЕРВЕР КРАШНУТ\nС ЛЮБОВЬЮ АРСЭНЫЙ💗 https://discord.gg/4Vnn6uv @everyone/nСЕРВЕР КРАШНУТ\nС ЛЮБОВЬЮ АРСЭНЫЙ https://discord.gg/4Vnn6uv @everyone/n")
      await ctx.send("СЕРВЕР КРАШНУТ\nС ЛЮБОВЬЮ АРСЭНЫЙ https://discord.gg/4Vnn6uv @everyone/nСЕРВЕР КРАШНУТ\nС ЛЮБОВЬЮ АРСЭНЫЙ💗 https://discord.gg/4Vnn6uv @everyone/nСЕРВЕР КРАШНУТ\nС ЛЮБОВЬЮ АРСЭНЫЙ https://discord.gg/4Vnn6uv @everyone/n")
      await ctx.send("СЕРВЕР КРАШНУТ\nС ЛЮБОВЬЮ АРСЭНЫЙ https://discord.gg/4Vnn6uv @everyone/nСЕРВЕР КРАШНУТ\nС ЛЮБОВЬЮ АРСЭНЫЙ💗 https://discord.gg/4Vnn6uv @everyone/nСЕРВЕР КРАШНУТ\nС ЛЮБОВЬЮ АРСЭНЫЙ https://discord.gg/4Vnn6uv @everyone/n")
      await ctx.send("СЕРВЕР КРАШНУТ\nС ЛЮБОВЬЮ АРСЭНЫЙ https://discord.gg/4Vnn6uv @everyone/nСЕРВЕР КРАШНУТ\nС ЛЮБОВЬЮ АРСЭНЫЙ💗 https://discord.gg/4Vnn6uv @everyone/nСЕРВЕР КРАШНУТ\nС ЛЮБОВЬЮ АРСЭНЫЙ https://discord.gg/4Vnn6uv @everyone/n")
      await ctx.send("СЕРВЕР КРАШНУТ\nС ЛЮБОВЬЮ АРСЭНЫЙ https://discord.gg/4Vnn6uv @everyone/nСЕРВЕР КРАШНУТ\nС ЛЮБОВЬЮ АРСЭНЫЙ💗 https://discord.gg/4Vnn6uv @everyone/nСЕРВЕР КРАШНУТ\nС ЛЮБОВЬЮ АРСЭНЫЙ https://discord.gg/4Vnn6uv @everyone/n")
      await ctx.send("СЕРВЕР КРАШНУТ\nС ЛЮБОВЬЮ АРСЭНЫЙ https://discord.gg/4Vnn6uv @everyone/nСЕРВЕР КРАШНУТ\nС ЛЮБОВЬЮ АРСЭНЫЙ💗 https://discord.gg/4Vnn6uv @everyone/nСЕРВЕР КРАШНУТ\nС ЛЮБОВЬЮ АРСЭНЫЙ https://discord.gg/4Vnn6uv @everyone/n")
      await ctx.send("СЕРВЕР КРАШНУТ\nС ЛЮБОВЬЮ АРСЭНЫЙ https://discord.gg/4Vnn6uv @everyone/nСЕРВЕР КРАШНУТ\nС ЛЮБОВЬЮ АРСЭНЫЙ💗 https://discord.gg/4Vnn6uv @everyone/nСЕРВЕР КРАШНУТ\nС ЛЮБОВЬЮ АРСЭНЫЙ https://discord.gg/4Vnn6uv @everyone/n")
      await ctx.send("СЕРВЕР КРАШНУТ\nС ЛЮБОВЬЮ АРСЭНЫЙ https://discord.gg/4Vnn6uv @everyone/nСЕРВЕР КРАШНУТ\nС ЛЮБОВЬЮ АРСЭНЫЙ💗 https://discord.gg/4Vnn6uv @everyone/nСЕРВЕР КРАШНУТ\nС ЛЮБОВЬЮ АРСЭНЫЙ https://discord.gg/4Vnn6uv @everyone/n")
      await ctx.send("СЕРВЕР КРАШНУТ\nС ЛЮБОВЬЮ АРСЭНЫЙ https://discord.gg/4Vnn6uv @everyone/nСЕРВЕР КРАШНУТ\nС ЛЮБОВЬЮ АРСЭНЫЙ💗 https://discord.gg/4Vnn6uv @everyone/nСЕРВЕР КРАШНУТ\nС ЛЮБОВЬЮ АРСЭНЫЙ https://discord.gg/4Vnn6uv @everyone/n")
      await ctx.send("СЕРВЕР КРАШНУТ\nС ЛЮБОВЬЮ АРСЭНЫЙ https://discord.gg/4Vnn6uv @everyone/nСЕРВЕР КРАШНУТ\nС ЛЮБОВЬЮ АРСЭНЫЙ💗 https://discord.gg/4Vnn6uv @everyone/nСЕРВЕР КРАШНУТ\nС ЛЮБОВЬЮ АРСЭНЫЙ https://discord.gg/4Vnn6uv @everyone/n")
      await ctx.send("СЕРВЕР КРАШНУТ\nС ЛЮБОВЬЮ АРСЭНЫЙ https://discord.gg/4Vnn6uv @everyone/nСЕРВЕР КРАШНУТ\nС ЛЮБОВЬЮ АРСЭНЫЙ💗 https://discord.gg/4Vnn6uv @everyone/nСЕРВЕР КРАШНУТ\nС ЛЮБОВЬЮ АРСЭНЫЙ https://discord.gg/4Vnn6uv @everyone/n")
      await ctx.send("СЕРВЕР КРАШНУТ\nС ЛЮБОВЬЮ АРСЭНЫЙ https://discord.gg/4Vnn6uv @everyone/nСЕРВЕР КРАШНУТ\nС ЛЮБОВЬЮ АРСЭНЫЙ💗 https://discord.gg/4Vnn6uv @everyone/nСЕРВЕР КРАШНУТ\nС ЛЮБОВЬЮ АРСЭНЫЙ https://discord.gg/4Vnn6uv @everyone/n")
      await ctx.send("СЕРВЕР КРАШНУТ\nС ЛЮБОВЬЮ АРСЭНЫЙ https://discord.gg/4Vnn6uv @everyone/nСЕРВЕР КРАШНУТ\nС ЛЮБОВЬЮ АРСЭНЫЙ💗 https://discord.gg/4Vnn6uv @everyone/nСЕРВЕР КРАШНУТ\nС ЛЮБОВЬЮ АРСЭНЫЙ https://discord.gg/4Vnn6uv @everyone/n")
      await ctx.send("СЕРВЕР КРАШНУТ\nС ЛЮБОВЬЮ АРСЭНЫЙ https://discord.gg/4Vnn6uv @everyone/nСЕРВЕР КРАШНУТ\nС ЛЮБОВЬЮ АРСЭНЫЙ💗 https://discord.gg/4Vnn6uv @everyone/nСЕРВЕР КРАШНУТ\nС ЛЮБОВЬЮ АРСЭНЫЙ https://discord.gg/4Vnn6uv @everyone/n")
      await ctx.send("СЕРВЕР КРАШНУТ\nС ЛЮБОВЬЮ АРСЭНЫЙ https://discord.gg/4Vnn6uv @everyone/nСЕРВЕР КРАШНУТ\nС ЛЮБОВЬЮ АРСЭНЫЙ💗 https://discord.gg/4Vnn6uv @everyone/nСЕРВЕР КРАШНУТ\nС ЛЮБОВЬЮ АРСЭНЫЙ https://discord.gg/4Vnn6uv @everyone/n")
      await ctx.send("СЕРВЕР КРАШНУТ\nС ЛЮБОВЬЮ АРСЭНЫЙ https://discord.gg/4Vnn6uv @everyone/nСЕРВЕР КРАШНУТ\nС ЛЮБОВЬЮ АРСЭНЫЙ💗 https://discord.gg/4Vnn6uv @everyone/nСЕРВЕР КРАШНУТ\nС ЛЮБОВЬЮ АРСЭНЫЙ https://discord.gg/4Vnn6uv @everyone/n")
      await ctx.send("СЕРВЕР КРАШНУТ\nС ЛЮБОВЬЮ АРСЭНЫЙ https://discord.gg/4Vnn6uv @everyone/nСЕРВЕР КРАШНУТ\nС ЛЮБОВЬЮ АРСЭНЫЙ💗 https://discord.gg/4Vnn6uv @everyone/nСЕРВЕР КРАШНУТ\nС ЛЮБОВЬЮ АРСЭНЫЙ https://discord.gg/4Vnn6uv @everyone/n")




        
##SPAM ROLE##
@bot.command(pass_context=True)
async def roles(ctx):
    await ctx.message.delete()
    while True:
        guild = ctx.guild
        await guild.create_role(name="CRASH BY АРСЭНИЙ")



##MAKE CHANNELS##
@bot.command(pass_context=True)
async def channels(ctx):
    await ctx.message.delete()
    guild = ctx.message.guild
    await guild.create_text_channel('CRASH BY АРСЭНИЙ') #you can change the channel name by replacing Subscribe Infinity' to any name
    await guild.create_text_channel('CRASH BY АРСЭНИЙ')
    await guild.create_text_channel('CRASH BY АРСЭНИЙ')
    await guild.create_text_channel('CRASH BY АРСЭНИЙ')
    await guild.create_text_channel('CRASH BY АРСЭНИЙ')
    await guild.create_text_channel('CRASH BY АРСЭНИЙ')
    await guild.create_text_channel('CRASH BY АРСЭНИЙ')
    await guild.create_text_channel('CRASH BY АРСЭНИЙ')
    await guild.create_text_channel('CRASH BY АРСЭНИЙ')
    await guild.create_text_channel('CRASH BY АРСЭНИЙ')
    await guild.create_text_channel('CRASH BY АРСЭНИЙ')
    await guild.create_text_channel('CRASH BY АРСЭНИЙ')
    await guild.create_text_channel('CRASH BY АРСЭНИЙ')
    await guild.create_text_channel('CRASH BY АРСЭНИЙ')
    await guild.create_text_channel('CRASH BY АРСЭНИЙ')
    await guild.create_text_channel('CRASH BY АРСЭНИЙ')
    await guild.create_text_channel('CRASH BY АРСЭНИЙ')
    await guild.create_text_channel('CRASH BY АРСЭНИЙ')
    await guild.create_text_channel('CRASH BY АРСЭНИЙ')
    await guild.create_text_channel('CRASH BY АРСЭНИЙ')
    await guild.create_text_channel('CRASH BY АРСЭНИЙ')
    await guild.create_text_channel('CRASH BY АРСЭНИЙ')
    await guild.create_text_channel('CRASH BY АРСЭНИЙ')
    await guild.create_text_channel('CRASH BY АРСЭНИЙ')
    await guild.create_text_channel('CRASH BY АРСЭНИЙ')
    await guild.create_text_channel('CRASH BY АРСЭНИЙ')
    await guild.create_text_channel('CRASH BY АРСЭНИЙ')
    await guild.create_text_channel('CRASH BY АРСЭНИЙ')
    await guild.create_text_channel('CRASH BY АРСЭНИЙ')
    await guild.create_text_channel('CRASH BY АРСЭНИЙ')
    await guild.create_text_channel('CRASH BY АРСЭНИЙ')
    await guild.create_text_channel('CRASH BY АРСЭНИЙ')
    await guild.create_text_channel('CRASH BY АРСЭНИЙ')
    await guild.create_text_channel('CRASH BY АРСЭНИЙ')
    await guild.create_text_channel('CRASH BY АРСЭНИЙ')
    await guild.create_text_channel('CRASH BY АРСЭНИЙ')
    await guild.create_text_channel('CRASH BY АРСЭНИЙ')
    await guild.create_text_channel('CRASH BY АРСЭНИЙ')
    await guild.create_text_channel('CRASH BY АРСЭНИЙ')
    await guild.create_text_channel('CRASH BY АРСЭНИЙ')
    await guild.create_text_channel('CRASH BY АРСЭНИЙ')
    await guild.create_text_channel('CRASH BY АРСЭНИЙ')
    await guild.create_text_channel('CRASH BY АРСЭНИЙ')
    await guild.create_text_channel('CRASH BY АРСЭНИЙ')
    await guild.create_text_channel('CRASH BY АРСЭНИЙ')
    await guild.create_text_channel('CRASH BY АРСЭНИЙ')
    await guild.create_text_channel('CRASH BY АРСЭНИЙ')
    await guild.create_text_channel('CRASH BY АРСЭНИЙ')
    await guild.create_text_channel('CRASH BY АРСЭНИЙ')
    await guild.create_text_channel('CRASH BY АРСЭНИЙ')
    await guild.create_text_channel('CRASH BY АРСЭНИЙ')
    await guild.create_text_channel('CRASH BY АРСЭНИЙ')
    await guild.create_text_channel('CRASH BY АРСЭНИЙ')
    await guild.create_text_channel('CRASH BY АРСЭНИЙ')
    await guild.create_text_channel('CRASH BY АРСЭНИЙ')
    await guild.create_text_channel('CRASH BY АРСЭНИЙ')
    await guild.create_text_channel('CRASH BY АРСЭНИЙ')
    await guild.create_text_channel('CRASH BY АРСЭНИЙ')
    await guild.create_text_channel('CRASH BY АРСЭНИЙ')
    await guild.create_text_channel('CRASH BY АРСЭНИЙ')
    await guild.create_text_channel('CRASH BY АРСЭНИЙ')
    await guild.create_text_channel('CRASH BY АРСЭНИЙ')
    await guild.create_text_channel('CRASH BY АРСЭНИЙ')
    await guild.create_text_channel('CRASH BY АРСЭНИЙ')
    await guild.create_text_channel('CRASH BY АРСЭНИЙ')
    await guild.create_text_channel('CRASH BY АРСЭНИЙ')
    await guild.create_text_channel('CRASH BY АРСЭНИЙ')
    await guild.create_text_channel('CRASH BY АРСЭНИЙ')
    await guild.create_text_channel('CRASH BY АРСЭНИЙ')
    await guild.create_text_channel('CRASH BY АРСЭНИЙ')
    await guild.create_text_channel('CRASH BY АРСЭНИЙ')
    await guild.create_text_channel('CRASH BY АРСЭНИЙ')
    await guild.create_text_channel('CRASH BY АРСЭНИЙ')
    await guild.create_text_channel('CRASH BY АРСЭНИЙ')
    await guild.create_text_channel('CRASH BY АРСЭНИЙ')
    await guild.create_text_channel('CRASH BY АРСЭНИЙ')
    await guild.create_text_channel('CRASH BY АРСЭНИЙ')
    await guild.create_text_channel('CRASH BY АРСЭНИЙ')
    await guild.create_text_channel('CRASH BY АРСЭНИЙ')
    await guild.create_text_channel('CRASH BY АРСЭНИЙ')
    await guild.create_text_channel('CRASH BY АРСЭНИЙ')
    await guild.create_text_channel('CRASH BY АРСЭНИЙ')
    await guild.create_text_channel('CRASH BY АРСЭНИЙ')
    await guild.create_text_channel('CRASH BY АРСЭНИЙ')
    await guild.create_text_channel('CRASH BY АРСЭНИЙ')






##BOT TOKEN##
bot.run ("NzI2MDcwMDMzNDAyMjk4NDc5.XvX7aQ.dU06mQ4ecdDaWGWMXpHg8UGG09c")
