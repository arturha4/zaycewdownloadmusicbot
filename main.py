import requests
from bs4 import BeautifulSoup

url = 'http://zaycev.net/search.html?query_search='
# url нужно сделать так чтобы считывал с телеги последнюю часть, сплитил и вставлял в url
url_music_download = []
data_urls = []


def get_html(url):
   page = requests.get(url)
   return page

#получаем страницу в html
def parse(url):
   html = get_html(url)
   if html.status_code == 200:
      get_content(html.text)

#парсит данные которые ввел пользователь, возвращает  ссылку на страницу с песнями
def get_link(track):
   url = 'http://zaycev.net/search.html?query_search='
   for part_name in track.split():
      url+="+"+part_name
   return url

def get_content(html):
   boss = "https://zaycev.net"
   soup = BeautifulSoup(html, "html.parser")
   items = soup.find_all('div', class_="musicset-track clearfix")
   for download_link in items:
      data_urls.append(boss + download_link.get('data-url'))


urls = []

#получает url страницы
def parse_data_music():
     return (parse_end_urls(get_html(data_urls[0]).text))



def parse_end_urls(link):
   return link[link.find('https'):link.find('"}')]


def work(usurl):
   parse(usurl)
   parse_data_music()
