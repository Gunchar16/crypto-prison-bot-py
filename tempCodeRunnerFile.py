from urllib.request import Request, urlopen



print(urlopen(Request('https://hodlershub.com', headers = {'User-Agent': 'Mozilla/5.0'})))