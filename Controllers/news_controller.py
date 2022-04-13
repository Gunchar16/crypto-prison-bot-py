from urllib.request import Request, urlopen
import requests
from bs4 import BeautifulSoup
import discord
from datetime import datetime


def news_service(client, url, file_name):
    req = Request(url, 
                  headers={'User-Agent': 'Mozilla/5.0'})
    get_html = urlopen(req).read()
    result = BeautifulSoup(get_html, "html.parser")
    html_reader = open(file_name, "r", encoding="utf-8")
    html_news = result.find_all('article')[0].parent.find('a')

    if html_reader.read() != str(html_news):
      html_writer = open(file_name, "w", encoding="utf-8")
      html_writer.write(str(html_news))
      url = 'https://cryptonews.com' + html_news['href']
      value = html_news.find('img')['alt']
      src = html_news.find('img')['src']
      embed=discord.Embed(color=0xd17000, title='Latest News', description=value)
      embed.add_field(name='To Read Fully', value='[click here](' + url + ')!')
      embed.timestamp=datetime.utcnow()
      embed.set_footer(text='Sent')
      embed.set_author(name=client.user.name, icon_url=client.user.avatar_url)
      embed.set_image(url=src)
      return embed
    return None