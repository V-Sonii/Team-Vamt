# Install Parser library
# https://pythonprogramminglanguage.com/get-links-from-webpage/#:~:text=To%20get%20all%20links%20from%20a%20webpage%3A%20How,%E2%80%98a%E2%80%99%20is%20the%20indicator%20for%20links%20in%20html.
# req = Request("https://indiankanoon.org",headers={'User-Agent': 'Mozilla/5.0'})

from importlib.resources import contents
import requests
from urllib.request import Request, urlopen
from bs4 import BeautifulSoup
import re
req = Request("https://caselaw.in")
html_page = urlopen(req)
soup = BeautifulSoup(html_page, "lxml")
links = []
for link in soup.findAll('a',rel="bookmark"):
    links.append(link.get('href'))
print(links)
a=1
for i in links:   
    req = Request(i)
    html_page = urlopen(req)
    soup2 = BeautifulSoup(html_page, "lxml")
    for j in soup2.find_all("p",style="text-align: justify;"):
        f = open("text_"+str(a)+".txt",'a+')
        res = j.get_text()
        f.write(res)
        f.close()
    a+=1


