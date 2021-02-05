import requests
from bs4 import BeautifulSoup
from concurrent import futures
import time

header = {
    'user-agent':''
}

title = []
link = []
links = []
comment = []
# 获取假链接
def get_fake_link(text):
    soup = BeautifulSoup(text, 'html.parser')
    items = soup.find_all('div', class_='post-title')
    for item in items:
        the_title = item.find('a')
        title.append(the_title.text)
        link.append(the_title['href'])
        time.sleep(0.5)


# 合成帖子链接
def combine_list(url):
    part_link = 'https://bbs.hupu.com/'
    link = part_link + url
    return link

def get_comment(text):
    soup = BeautifulSoup(text, 'html-parser')
    items = soup.find_all('div', class_='thread-contend-detail').find('p')
    for item in items:
        comment.append(item.text)

executor = futures.ThreadPoolExecutor(max_workers=5)
session = requests.Session()
session.headers.update(header)
f = executor.submit(session.get, 'https://bbs.hupu.com/acg')
get_fake_link(f.result().text)

for link in link:
    link = combine_list(link)
    links.append(link)

fs = []
f = executor.submit(session.get, links)
get_comment(f.result().text)
fs.append(f)
futures.wait(fs)
