# import requests
# from bs4 import BeautifulSoup
# url = "https://caselaw.in/"

# r = requests.get(url)
# soup = BeautifulSoup(r.content, 'html.parser')
# for i in soup.find_all("code"):
#     print(i.text)
#     # We can also do it like this
#     # print(i.get_text())
# paras = soup.find_all('a', rel="bookmark")



# for i in paras:
#     print(i)
# Install Parser library
# https://pythonprogramminglanguage.com/get-links-from-webpage/#:~:text=To%20get%20all%20links%20from%20a%20webpage%3A%20How,%E2%80%98a%E2%80%99%20is%20the%20indicator%20for%20links%20in%20html.
# from importlib.resources import contents
# import requests
# from urllib.request import Request, urlopen
# from bs4 import BeautifulSoup
# import re
# # url='https://caselaw.in/'
# # r=requests.get(url)  
# # req = Request("https://indiankanoon.org",headers={'User-Agent': 'Mozilla/5.0'})
# req=Request("https://caselaw.in/",headers={'User-Agent': 'Mozilla/5.0'})
# html_page = urlopen(req)

# soup = BeautifulSoup(html_page, "lxml")

# links = []
# for link in soup.findAll('p'):
#     links.append(link.get('href'))
#     #links.append()
# print(links)
from importlib.resources import contents
from matplotlib import style
import json
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

for i in links:
    req = Request(i)
    html_page = urlopen(req)
    soup2 = BeautifulSoup(html_page, "lxml")
    for j in soup2.find_all("p",style="text-align: justify;"):
        res = j.get_text()
        print(res)


# a=1
# for i in links:   
#     req = Request(i)
#     html_page = urlopen(req)
#     soup2 = BeautifulSoup(html_page, "lxml")
#     for j in soup2.find_all("p",style="text-align: justify;"):
#         # print(j)
#         f = open("text_"+str(a)+".json",'a+')     
#         res = j.get_text()              
#         f.write(res)
#         f.close()
#     a+=1
        
     
    

