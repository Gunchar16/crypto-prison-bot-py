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
    News('https://cryptonews.com/news/bitcoin-news/', 'bitcoinnews.html'),
    News('https://cryptonews.com/news/ethereum-news/', 'ethereumnews.html'),
    News('https://cryptonews.com/news/defi-news/', 'definews.html'),
    News('https://cryptonews.com/news/altcoin-news/', 'altcoinnews.html'),
    News('https://cryptonews.com/news/blockchain-news/', 'blockchainnews.html'),
    News('https://cryptonews.com/news/cryptonews-deals/', 'cryptodeals.html')
    ]
  return news_service(client, news)