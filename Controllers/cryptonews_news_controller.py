from urllib.request import Request, urlopen
import requests
from bs4 import BeautifulSoup
import discord
from datetime import datetime


def news_service(client, news):
    for new in news:

      req = Request(new.url, 
                    headers={'User-Agent': 'Mozilla/5.0'})
      get_html = urlopen(req).read()
      result = BeautifulSoup(get_html, "html.parser")
      html_reader = open(new.file_name, "r", encoding="utf-8")
      if new.file_name == 'nftnow.txt':
        html_news = result.find('article', {'class': 'article-loop article-loop__rounded article-loop__inside animate__fade-in'} )
        url = html_news.find('a')['href']
        if html_reader.read() != str(url):
          html_writer = open(new.file_name, "w", encoding="utf-8")
          html_writer.write(str(url))
          value = html_news.find('h3').string
          src = html_news.find('div', attrs={'class': 'article-loop__featured-image'})['style'].split('url(')[1][:-2]
          embed=discord.Embed(color=0xd17000, title='Latest News', description=value)
          embed.add_field(name='To Read Fully', value='[click here](' + url + ')!')
          embed.timestamp=datetime.utcnow()
          embed.set_footer(text='Sent')
          embed.set_author(name=client.user.name, icon_url=client.user.avatar_url)
          embed.set_image(url=src)
          return embed
      else:
        html_news = result.find_all('article')[0].parent.find('a')
        url = 'https://cryptonews.com' + html_news['href']
        if not str(url).split('com/')[1] in html_reader.read():
          html_writer = open(new.file_name, "w", encoding="utf-8")
          html_writer.write(str(url))
          value = html_news.find('img')['alt']
          src = html_news.find('img')['src']
          embed=discord.Embed(color=0xd17000, title='Latest News', description=value)
          embed.add_field(name='To Read Fully', value='[click here](' + url + ')!')
          embed.timestamp=datetime.utcnow()
          embed.set_footer(text='Sent')
          embed.set_author(name=client.user.name, icon_url=client.user.avatar_url)
          embed.set_image(url=src)
          return embed