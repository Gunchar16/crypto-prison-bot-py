from asyncio.windows_events import NULL
from urllib.request import Request, urlopen
import requests
from bs4 import BeautifulSoup
import discord
from datetime import datetime

from Controllers.cryptonews_news_controller import news_service
from Infrastructure.News import News



async def message_handler(client):
  news = [
    News('https://cryptonews.com/news/nft-news/', 'nftnews.html'),
    News('https://nftnow.com/category/news/', 'nftnow.html')
    ]
  return news_service(client, news)