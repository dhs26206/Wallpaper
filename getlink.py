import requests
from bs4 import BeautifulSoup
def getlist(link):
  p=requests.get(link)
  soup = BeautifulSoup(p.text, 'html.parser')
  k=soup.find_all('img',class_="thumbnail")
  liou=[]
  for i in k:
    raw_link=(i['src'])
    newlink=raw_link[:-13:]+'.jpg'
    liou.append(newlink)
  return liou
