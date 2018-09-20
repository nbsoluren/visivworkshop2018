#For creating folders
import os
from bs4 import BeautifulSoup
#For retrieving page source and img
from urllib.request import Request, urlopen
#Creating a folder to store it by Chapter
def make_folder(directory_name):
   try:
       if not os.path.exists(directory_name):
           os.makedirs(directory_name)
   except OSError:
       print ('Error: Creating directory. ' +  directory_name)
   directory = os.getcwd() + "/" + directory_name
   return directory_name
# url = 'https://manganelo.com/manga/about_death'
#
# #Retrieving the page source
# #We are pretending to be Mozilla
# req = Request(url, headers={'User-Agent': 'Mozilla/5.0'})
# webpage = urlopen(req).read()
#
# #Passing it into Beautifulsoup format.
# soup = BeautifulSoup(webpage, 'html.parser')
#
# chapter_links = []
# tester = soup.find("div", class_="chapter-list").find_all("div",class_="row")
# for i in tester:
#    chapter_links.append(i.find("span").a['href'])
# file = open("moot" + ".html","w+")
# file.write(str(chapter_links))
# file.close()
# #Retrieving Page Source of link and storing it in chapter_page
url = 'https://manganelo.com/chapter/about_death/chapter_24'
req = Request(url, headers={'User-Agent': 'Mozilla/5.0'})
chapter_page = urlopen(req).read()
#chapter links
soup_chapter = BeautifulSoup(chapter_page, 'html.parser').find_all("img", class_="img_content")

img_links = []
for i in soup_chapter:
   img_links.append(i['src'])

file = open("moot" + ".html","w+")
file.write(str(img_links))
file.close()
