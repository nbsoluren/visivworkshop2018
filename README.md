# VISIV Workshop on web scraping  :japanese_ogre:

Technopedia defines it as:

> Web scraping is essentially a form of data mining. Items like weather reports, auction details, market pricing, or any other list of collected data can be sought in Web scraping efforts. 

## Do a ctrl + u
That is what we call the **page source**. I won’t really dwindle down on the terminology for this workshop. You can **GOOGLE that**. Here let’s try to build something. 

## We will be using Beautifulsoup 
Find the documentation here: https://www.crummy.com/software/BeautifulSoup/bs4/doc/

> Beautiful Soup is a Python library for pulling data out of HTML and XML files. It works with your favorite parser to provide idiomatic ways of navigating, searching, and modifying the parse tree. It commonly saves programmers hours or days of work.

## Clone it.
Start with cloning the repo and creating your own branch
```
$ git clone https://github.com/nbsoluren/visivworkshop2018
$ git checkout -b dev/jedd
```

## Let's start with the set-up
Things you don’t really need to put much thought into
#### 1. Time to Import
Make sure you’ve properly installed beautifulsoup4 on your machines.
```
#For creating folders
import os
from bs4 import BeautifulSoup
#For retrieving page source and img
from urllib.request import Request, urlopen
```
#### 2. Function you don't really need to analyze. 
I just googled this. Just know what it does. No need to memorize.
```
#Creating a folder to store it by Chapter
def make_folder(directory_name):
   try:
       if not os.path.exists(directory_name):
           os.makedirs(directory_name)
   except OSError:
       print ('Error: Creating directory. ' +  directory_name)
   directory = os.getcwd() + "/" + directory_name
   return directory_name
```
###### Start with a verb
```
$git add -A 
$git commit -m “Imported libraries and Added folder creation function”
```
## Now let’s get to the good stuff
Get your thinking caps on.

### We'll be using Mangakakalot
Their website is relatively easy to parse through so we’ll use this for now. 
Search for **“about death”** for uniformity

#### 3. Getting the soup. 
**CTRL+U** to show the page source
```
url = 'https://manganelo.com/manga/about_death'

#Retrieving the page source
#We are pretending to be Mozilla
req = Request(url, headers={'User-Agent': 'Mozilla/5.0'})
webpage = urlopen(req).read()

#Passing it into Beautifulsoup format.
soup = BeautifulSoup(webpage, 'html.parser')
```

###### Commit regularly
```
$git add -A 
$git commit -m “Retrieved URL and parsed into Beautifulsoup format”
```

#### 4. Getting Chapter links.
Ctrl+f search for “chapter-list"

I better explain this in the slides to see step by step what each command mean:
```
chapter_links = []
tester = soup.find("div", class_="chapter-list").find_all("div",class_="row")
for i in tester:
   chapter_links.append(i.find("span").a['href'])
```

###### Testing
Let’s see if our code works. We should have a list of chapter links.
```
file = open("moot" + ".html","w+")
file.write(str(chapter_links))
file.close()
```
###### We will push later.
```
$git add -A 
$git commit -m “Added retrieval of chapter links”
```

#### 5. Getting Img Links.
**Ctrl+C** one chapter from your chapter links
```
#Retrieving Page Source of link and storing it in chapter_page
url = 'https://manganelo.com/chapter/about_death/chapter_24'
req = Request(url, headers={'User-Agent': 'Mozilla/5.0'})
chapter_page = urlopen(req).read()
```
I better explain this in the slides to see step by step what each command mean:
```
soup_chapter = BeautifulSoup(chapter_page, 'html.parser').find_all("img", class_="img_content")

img_links = []
for i in soup_chapter:
   img_links.append(i['src'])
```
###### Testing
Let’s see if our code works. We should have a list of img links.
```
file = open("moot" + ".html","w+")
file.write(str(img_links))
file.close()
```
###### Commit your work
```
$git add -A 
$git commit -m “Added retrieval of img links”
```

#### 6. Downloading Images
**Ctrl+C** one img form your img links.
```
#Retrieving Image data and storing it in imgdata 
folder = make_folder("Chapter X") #Makes folder to store Img in
url = 'http://s5.mkklcdnv2.com/mangakakalot/a1/about_death/chapter_0_prologue/1.jpg'
req = Request(url, headers={'User-Agent': 'Mozilla/5.0'})
imgdata = urlopen(req).read()
```
Writing/Downloading the image:
```
filename = url.split('/')[-1]
output = open(folder+"/"+filename,"wb")
output.write(imgdata)
output.close()
```

#### After running this look at the network in github
```
$git add -A 
$git commit -m “Added retrieval of img links”
$git push
```
## ALMOST DONE!
We finished tackling the essential parts of the program, next bits are just modularity stuff, loops. Basically you just loop through the chapters and loop through each img in those chapters. EZ PZ no need to teach :D
### Check it out:
```
$git checkout master
```
## Stuff I didn't use sadly:
- **.strip([chars])**
This method returns a copy of the string in which all chars have been stripped from the beginning and the end of the string.
- **.text**
Get the text between tags
- **Export to CSV**
```
import csv
from datetime import datetime
with open(‘index.csv’, ‘a’) as csv_file:
  writer = csv.writer(csv_file)
writer.writerow([visiv, datetime.now()])
```
- **Export to JSON**
See my project on github (TipidPC Parser)
- **Using APIs**
Some big sites gives you a more abstracted (easier) way of getting data.
- **Scrappy**
“Scrapy is a free and open-source web-crawling framework written in Python. Originally designed for web scraping, it can also be used to extract data using APIs or as a general-purpose web crawler. It is currently maintained by Scrapinghub Ltd., a web-scraping development and services company.”

## References and Useful Links:
#### Projects I've done:
- https://github.com/nbsoluren/tipidPCParser (JSON FORMAT)
- https://github.com/nbsoluren/stackoverflowparser
#### Resources:
- https://www.crummy.com/software/BeautifulSoup/bs4/doc/
- Tons of Stackoverflow pages I’ve forgotten
- https://medium.freecodecamp.org/how-to-scrape-websites-with-python-and-beautifulsoup-5946935d93fe
- https://stackoverflow.com/questions/7200252/how-does-urllib-urlopen-work 
## QUESTIONS? 
Google/ Stackoverflow is your friend.

















