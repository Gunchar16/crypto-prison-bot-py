from urllib.request import Request, urlopen
import requests
from bs4 import BeautifulSoup
import discord
from datetime import datetime

from Controllers.cryptonews_news_controller import news_service
from Infrastructure.News import News



async def message_handler(client):
  news = [
    News('https://cryptonews.com/news/bitcoin-news/', 'bitcoinnews.txt'),
    News('https://cryptonews.com/news/ethereum-news/', 'ethereumnews.txt'),
    News('https://cryptonews.com/news/defi-news/', 'definews.txt'),
    News('https://cryptonews.com/news/altcoin-news/', 'altcoinnews.txt'),
    News('https://cryptonews.com/news/blockchain-news/', 'blockchainnews.txt'),
    News('https://cryptonews.com/news/cryptonews-deals/', 'cryptodeals.txt')
    ]
  return news_service(client, news)