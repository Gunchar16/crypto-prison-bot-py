from asyncio.windows_events import NULL
from urllib.request import Request, urlopen
import requests
from bs4 import BeautifulSoup
import discord
from datetime import datetime

from Controllers.wired_news_controller import news_service
from Infrastructure.News import News



async def message_handler(client):
  news = [
    News('https://www.wired.com/tag/coding/', 'coding.html'),
    News('https://www.wired.com/tag/programming/', 'programming.html'),
    News('https://www.wired.com/tag/technology/', 'technology.html')
    ]
  return news_service(client, news)