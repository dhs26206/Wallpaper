import requests as r
def writeimg(link):
  print(link)
  namel=link[58::]
  f=open("downloads/"+namel,"wb")
  data=r.get(link)
  f.write(data.content)
  f.close()
  