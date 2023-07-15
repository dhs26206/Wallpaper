from getlink import getlist
from generate import writeimg
def main():
  rawlink="https://windows10spotlight.com/page/"
  for i in range(3,10):
    modify=rawlink+str(i)
    linklist=getlist(modify)
    for k in linklist:
      writeimg(k)
main()
    