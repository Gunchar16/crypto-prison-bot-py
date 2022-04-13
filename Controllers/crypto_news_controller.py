from asyncio.windows_events import NULL
from urllib.request import Request, urlopen
import requests
from bs4 import BeautifulSoup
import discord
from datetime import datetime

from Controllers.news_controller import news_service



async def message_handler(client):
  return news_service(client,'https://cryptonews.com/news/cryptonews-deals/', 'cryptonews.html')