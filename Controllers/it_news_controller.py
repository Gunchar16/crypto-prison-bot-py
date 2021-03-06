from urllib.request import Request, urlopen
import requests
from bs4 import BeautifulSoup
import discord
from datetime import datetime

from Controllers.wired_news_controller import news_service
from Infrastructure.News import News



async def message_handler(client):
  news = [
    News('https://www.wired.com/tag/coding/', 'coding.txt'),
    News('https://www.wired.com/tag/programming/', 'programming.txt'),
    News('https://www.wired.com/tag/technology/', 'technology.txt')
    ]
  return news_service(client, news)