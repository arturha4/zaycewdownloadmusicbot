import requests
from bs4 import BeautifulSoup
url="http://zaycev.net/search.html?query_search=клава+кока+краш"
#url нужно сделать так чтобы считывал с телеги последнюю часть, сплитил и вставлял в url
url_music_download=[]
data_urls=[]
def get_html(url):
   page=requests.get(url)
   return page

def parse(url):
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
def parse_data_music():
   for link in data_urls:
      print(parse_end_urls(get_html(link).text))
      break
def  parse_end_urls(link):
   return link[link.find('https'):link.find('"}')]

parse(url)
parse_data_music()




