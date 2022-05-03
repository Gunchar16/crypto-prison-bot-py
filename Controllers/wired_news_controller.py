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
      html_news = result.find('div',attrs={'class': 'SummaryItemWrapper-gdEuvf bheJMz summary-item summary-item--has-border summary-item--article summary-item--no-icon summary-item--text-align-left summary-item--layout-placement-side-by-side-desktop-only summary-item--layout-position-image-left summary-item--layout-proportions-33-66 summary-item--side-by-side-align-center summary-item--standard SummaryItemWrapper-bGkJDw ifBcbu summary-list__item'})
      url = 'https://www.wired.com' + html_news.find('a', {'class': 'SummaryItemHedLink-cgPsOZ cEGVhT summary-item-tracking__hed-link summary-item__hed-link'})['href']
      if not str(url).split('com/')[1] in html_reader.read():
        html_writer = open(new.file_name, "w", encoding="utf-8")
        html_writer.write(str(url))
        value = html_news.find('h3').string
        src = html_news.find('img')['src']
        embed=discord.Embed(color=0xd17000, title='Latest News', description=value)
        embed.add_field(name='To Read Fully', value='[click here](' + url + ')!')
        embed.timestamp=datetime.utcnow()
        embed.set_footer(text='Sent')
        embed.set_author(name=client.user.name, icon_url=client.user.avatar_url)
        embed.set_image(url=src)
        return embed
      