import requests
import urllib.request
import time
from bs4 import BeautifulSoup

url = 'http://carterwatts.com/post_comment.php'
response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")



# To download the whole data set, let's do a for loop through all a tags
for i in range(0,len(soup.findAll('h1'))+1): #'a' tags are for links
    print("Loop "+str(i))
    one_a_tag = soup.findAll('h1')[i]
    print("Made tag")
    link = one_a_tag['href']
    print("Made link")
    download_url = url + link
    print("Downloaded url")
    print(urllib.request.urlretrieve(download_url,'./'+link[link.find('/turnstile_')+1:]) )
    print("Requested info")
    time.sleep(1) #pause the code for a second