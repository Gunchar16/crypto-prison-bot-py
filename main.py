import os
from genericpath import getatime
from pydoc import describe
from sqlite3 import Timestamp
from jinja2 import Undefined
import requests
import json
import schedule
import discord
from discord.ext import commands, tasks
from discord.voice_client import VoiceClient
from discord_slash import SlashCommand, SlashContext
from discord_slash.utils.manage_commands import create_choice, create_option
import youtube_dl
import random
from random import choice
from Server.keep_alive import keepAlive
from datetime import datetime
import numpy as np
import Controllers.nft_news_controller as nft_news_controller
import Controllers.crypto_news_controller as crypto_news_controller
import Controllers.it_news_controller as it_news_controller

intents = discord.Intents.default()
intents.members = True

client = commands.Bot(intents=intents, command_prefix = '?')
slash = SlashCommand(client, sync_commands=True)


status = ['Counting Ethereum', 'Collecting NFTs', 'Dropping $OAP', 'Solving Sneaky Peakys', 'Covering Tracks For Gramps', 'Hiding From M']



guild_id = 932592179275243531


@client.event
async def on_ready():
    change_status.start()
    messageIntervalCrypto.start()
    messageIntervalNft.start()
    messageIntervalIT.start()
    print("The bot is ready.")


@client.event
async def on_member_join(member):
    print(f"{member} has joined the server kekw.")


@tasks.loop(seconds = 8)
async def change_status():
    await client.change_presence(activity= discord.Game(np.random.choice(status, p=[0.2, 0.2, 0.32, 0.2, 0.06, 0.02])))



@slash.slash(
  name='random',
  description='Get A List of Random User(s)', 
  guild_ids=[guild_id],
  options=[
    create_option(
      name='number',
      description='Choose The Number',
      required=True,
      option_type=4
    )
  ]
  )
async def get_random(ctx:SlashContext, number:int):
    if number > 25:
        await ctx.send('The number cannot be bigger than 25')
        return
    embed=discord.Embed(color=0xd17000, title='The Winner' if number == 1 else 'The List of Winners', description='The Winner!' if number == 1 else 'The List of Winners!')
    random_user = []
    for x in range(number):
        if(len(random_user) == 0):
            choose = random.choice(client.get_guild(guild_id).members)
            random_user.append(choose)
            embed.add_field(name= f'Winner Number {x + 1}:' if number != 1 else 'Winner:', value=choose)
        else:
            choose = random.choice(client.get_guild(guild_id).members)
            while choose in random_user:
                choose = random.choice(client.get_guild(guild_id).members)
            random_user.append(choose)
            embed.add_field(name= f'Winner Number {x + 1}:', value=choose)
    await ctx.send(embed=embed)



@client.command()
async def RepeatMessageCrypto(ctx,enabled='start', interval=10):
    if enabled.lower() == 'stop':
        messageIntervalCrypto.cancel()
    elif enabled.lower() == 'start':
        messageIntervalCrypto.change_interval(seconds=int(interval))
        messageIntervalCrypto.start(ctx)

@tasks.loop(seconds=10800)
async def messageIntervalCrypto():
    channel = client.get_channel(963405867468849152)
    get_embed = await crypto_news_controller.message_handler(client)
    if get_embed is not None:
        await channel.send(embed=get_embed)

@client.command()
async def RepeatMessageIT(ctx,enabled='start', interval=10):
    if enabled.lower() == 'stop':
        messageIntervalIT.cancel()
    elif enabled.lower() == 'start':
        messageIntervalIT.change_interval(seconds=int(interval))
        messageIntervalIT.start(ctx)

@tasks.loop(seconds=10800)
async def messageIntervalIT():
    channel = client.get_channel(963405890340421672)
    get_embed = await it_news_controller.message_handler(client)
    if get_embed is not None:
        await channel.send(embed=get_embed)

@client.command()
async def RepeatMessageNft(ctx,enabled='start', interval=10):
    if enabled.lower() == 'stop':
        messageIntervalNft.cancel()
    elif enabled.lower() == 'start':
        messageIntervalNft.change_interval(seconds=int(interval))
        messageIntervalNft.start(ctx)
@tasks.loop(seconds=10800)
async def messageIntervalNft():
    channel = client.get_channel(963405890340421672)
    get_embed = await nft_news_controller.message_handler(client)
    if get_embed is not None:
        await channel.send(embed=get_embed)

my_secret = os.environ['TAH420']
keepAlive()
client.run(my_secret)
