import requests
from bs4 import BeautifulSoup
url="http://zaycev.net/search.html?query_search=30+seconds+to+mars"
#url нужно сделать так чтобы считывал с телеги последнюю часть, сплитил и вставлял в url
url_music_download=[]
data_urls=[]
def get_html(url):
   page=requests.get(url)
   return page

def parse():
   html=get_html(url)
   if html.status_code==200:
      get_content(html.text)

def get_content(html):
   boss="https://zaycev.net"
   soup=BeautifulSoup(html,"html.parser")
   items=soup.find_all('div',class_="musicset-track clearfix")
   for download_link in items:
      data_urls.append(boss+download_link.get('data-url'))
urls=[]
def parse_data_urls():
   for link in data_urls:
      print(get_html(link).text)






parse()
parse_data_urls()




