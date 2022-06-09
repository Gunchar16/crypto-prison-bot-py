from urllib.request import Request, urlopen
import requests
from bs4 import BeautifulSoup
import discord
from datetime import datetime

from Controllers.hodlers_hub_controller import news_service
from Infrastructure.News import News



async def message_handler(client):
  news = [
    News('https://hodlershub.com', 'hodlershub.txt')
    ]
  return news_service(client, news)