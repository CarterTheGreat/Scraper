from urllib.request import urlopen
from bs4 import BeautifulSoup

html = urlopen('https://en.wikipedia.org/wiki/Mathematical_constant')
bsh = BeautifulSoup(html.read(), 'html.parser')
print(bsh)
print( "bsh.h1: "+str(bsh.h3) )
