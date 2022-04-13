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
import youtube_dl
import random
from random import choice
from Server.keep_alive import keepAlive
from datetime import datetime
import numpy as np
import Controllers.nft_news_controller as nft_news_controller
import Controllers.crypto_news_controller as crypto_news_controller
import Controllers.it_news_controller as it_news_controller

client = commands.Bot(command_prefix = '?')

status = ['Counting Ethereum', 'Collecting NFTs', 'Dropping $OAP', 'Solving Sneaky Peakys', 'Covering Tracks For Gramps', 'Hiding From M']




@client.event
async def on_ready():
    change_status.start()
    print("The bot is ready.")


@client.event
async def on_member_join(member):
    print(f"{member} has joined the server kekw.")


@tasks.loop(seconds = 8)
async def change_status():
    await client.change_presence(activity= discord.Game(np.random.choice(status, p=[0.2, 0.2, 0.32, 0.2, 0.06, 0.02])))







@client.command()
async def RepeatMessageCrypto(ctx,enabled='start', interval=10):
    if enabled.lower() == 'stop':
        messageIntervalCrypto.cancel()
    elif enabled.lower() == 'start':
        messageIntervalCrypto.change_interval(seconds=int(interval))
        messageIntervalCrypto.start(ctx)

@tasks.loop(seconds=10)
async def messageIntervalCrypto(ctx):
    get_embed = await crypto_news_controller.message_handler(client)
    if get_embed is not None:
        await ctx.send(embed=get_embed)

@client.command()
async def RepeatMessageIT(ctx,enabled='start', interval=10):
    if enabled.lower() == 'stop':
        messageIntervalIT.cancel()
    elif enabled.lower() == 'start':
        messageIntervalIT.change_interval(seconds=int(interval))
        messageIntervalIT.start(ctx)

@tasks.loop(seconds=10)
async def messageIntervalIT(ctx):
    get_embed = await it_news_controller.message_handler(client)
    if get_embed is not None:
        await ctx.send(embed=get_embed)

@client.command()
async def RepeatMessageNft(ctx,enabled='start', interval=10):
    if enabled.lower() == 'stop':
        messageIntervalNft.cancel()
    elif enabled.lower() == 'start':
        messageIntervalNft.change_interval(seconds=int(interval))
        messageIntervalNft.start(ctx)

@tasks.loop(seconds=10)
async def messageIntervalNft(ctx):
    get_embed = await nft_news_controller.message_handler(client)
    if get_embed is not None:
        await ctx.send(embed=get_embed)



keepAlive()
client.run('OTYxOTYwNTAzOTM1MTExMTk5.YlAliA.wHtGE5LXukdJ5FdtxCirVyVEf1I')
