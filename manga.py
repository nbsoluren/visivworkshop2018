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

#Retrieving Chapter Links
def get_chapter_links(soup):
    chapter_links = []
    tester = soup.find("div", class_="chapter-list").find_all("div",class_="row")
    for i in tester:
        chapter_links.append(i.find("span").a['href'])
    return chapter_links

#Retrieving Image Links
def get_img_links(soup_chapter):
    soup_chapter = BeautifulSoup(chapter_page, 'html.parser').find_all("img", class_="img_content")
    img_links = []
    for i in soup_chapter:
        img_links.append(i['src'])
    return img_links

#Downloading Images Per CHAPTER
def download_images_per_chapter(img_links, folder):
    for img in img_links:
        req = Request(img, headers={'User-Agent': 'Mozilla/5.0'})
        webpage = urlopen(req).read()
        filename = img.split('/')[-1]
        output = open(folder+"/"+filename,"wb")
        output.write(webpage)
        output.close()


url = input("Happy to serve. Enter URL: ")
url = 'http://mangakakalot.com/manga/the_freudstein_twins'

#Retrieving the sourcecode
#We are pretending to be Mozilla browser
req = Request(url, headers={'User-Agent': 'Mozilla/5.0'})
webpage = urlopen(req).read()

#Passing it through BeautifulSoup so we can parse through it.
soup = BeautifulSoup(webpage, 'html.parser')

#Get the Chapter Links of the Manga
chapter_links = get_chapter_links(soup)

#Iterrating through each chapter
count = 1
for chapter in chapter_links:
    #Open up sourcecode of Chapter
    req = Request(chapter, headers={'User-Agent': 'Mozilla/5.0'})
    chapter_page = urlopen(req).read()

    #Make a Folder for Each Chapter
    folder = make_folder("Chapter" + str(count))

    #Getting Img Link for Each chapter
    img_links = get_img_links(chapter_page)

    #Download images per chapter
    download_images_per_chapter(img_links,folder)

    #increment counter
    count = count+1
