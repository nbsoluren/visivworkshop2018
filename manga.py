import os #For creating folder
from bs4 import BeautifulSoup #For parsing through sourcecode
from urllib.request import Request, urlopen #For retrieving source code and img

#Creating a folder to store it by Chapter
def make_folder(directory_name):
    try:
        if not os.path.exists(directory_name):
            os.makedirs(directory_name)
    except OSError:
        print ('Error: Creating directory. ' +  directory_name)
    directory = os.getcwd() + "/" + directory_name
    return directory_name

#Retrieving Chapter LINKS
def get_chapter_links(soup):
    chapter_links = []
    tester = soup.find("div", class_="chapter-list").find_all("div",class_="row")
    for i in tester:
        chapter_links.append(i.find("span").a['href'])
    return chapter_links

url = input("Happy to serve. Enter URL: ")
url = 'http://mangakakalot.com/manga/the_freudstein_twins'

#Retrieving the sourcecode
#We are pretending to be Mozilla browser
req = Request(url, headers={'User-Agent': 'Mozilla/5.0'})
webpage = urlopen(req).read()

#Passing it through BeautifulSoup so we can parse through it.
soup = BeautifulSoup(webpage, 'html.parser')

chapter_links = get_chapter_links(soup)
