# Install Parser library
# https://pythonprogramminglanguage.com/get-links-from-webpage/#:~:text=To%20get%20all%20links%20from%20a%20webpage%3A%20How,%E2%80%98a%E2%80%99%20is%20the%20indicator%20for%20links%20in%20html.
# from importlib.resources import contents
# import requests
# from urllib.request import Request, urlopen
# from bs4 import BeautifulSoup
# import re
# url='https://caselaw.in/'
# r=requests.get(url)
# req = Request("https://indiankanoon.org",headers={'User-Agent': 'Mozilla/5.0'})
# req = Request("https://indiankanoon.org",headers={'User-Agent': 'Mozilla/5.0'})
# req = Request("https://caselaw.in")

# html_page = urlopen(req)

# soup = BeautifulSoup(html_page, "lxml")

# links = []
# for link in soup.findAll('a',rel:"bookmark"):
#     links.append(link.get('href'))

# print(links)


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


# htmlContent=r.content
# # print(htmlContent)

# soup=BeautifulSoup(htmlContent,'html.parser')
# # print(soup.prettify)

# title=soup.title

# # paras=soup.find_all('p')
# # print(paras)


# anchor=soup.find_all('h2')
# print(anchor)