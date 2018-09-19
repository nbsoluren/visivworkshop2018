import requests
import os
from bs4 import BeautifulSoup
from urllib.request import Request, urlopen



req = Request('http://mangakakalot.com/manga/the_freudstein_twins', headers={'User-Agent': 'Mozilla/5.0'})
webpage = urlopen(req).read()

soup = BeautifulSoup(webpage, 'html.parser')
