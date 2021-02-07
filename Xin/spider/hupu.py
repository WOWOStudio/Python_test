'''import requests
from bs4 import BeautifulSoup
from concurrent import futures
import time

title = []  # 存放标题
link = []  # 存放链接
comment = []  # 存放评论

header = {
    'user-agent': '',
    'cookie': ''
}


# 获取部分链接
def get_part_link(text):
    soup = BeautifulSoup(text, 'html.parser')
    items = soup.find_all('div', class_='post-title')
    for item in items:
        the_title = item.find('a')
        title.append(the_title.text)
        link.append(the_title['href'])
        time.sleep(0.5)


# 合成帖子链接
def combine_list(url):
    part_link = 'https://bbs.hupu.com'
    link = part_link + url
    return link


# 获取评论
def get_comment(text):
    soup = BeautifulSoup(text, 'html.parser')
    items = soup.find_all('div', class_='thread-content-detail')
    for item in items:
        comments = item.find_all('p')
        comment.append(comments)
executor = futures.ThreadPoolExecutor(max_workers=5)  # 初始化线程池
session = requests.Session()  # 获取session对象
session.headers.update(header)  # 提供cookie和user-agent

f = executor.submit(session.get, 'https://bbs.hupu.com/acg-postdate')  # 提交任务
get_part_link(f.result().text)  # 获取部分链接

fs = []
for the_link in link:
    url = combine_list(the_link)  # 获取完整链接
    f = executor.submit(session.get, url)  # 提交任务
    fs.append(f)

futures.wait(fs)  # 等待任务完成
result = [f.result().text for f in fs]  # 存储结果
i = 0
for item in result:
    comment.append(get_comment(item))
    print('{}:\n{}'.format(title[i], comment[i]))
    i += 1

'''

import requests
from concurrent import futures
from bs4 import BeautifulSoup

headers = {
    'user-agent': '',
    'cookie': ''
}

session = requests.Session()
session.headers.update(headers)
executor = futures.ThreadPoolExecutor(max_workers=5)

def parse_list_page(text):
    soup = BeautifulSoup(text, 'html.parser')
    ul = soup.find('div', class_='bbs-sl-web-post').find('ul')
    urls = []
    prefix = 'https://bbs.hupu.com'
    for li in ul.find_all('li'):
        url = li.div.find('a', class_='p-title').attrs['href']
        url = prefix + url
        urls.append(url)
    return urls

def parse_content_page(text):
    soup = BeautifulSoup(text, 'html.parser')
    title = soup.find('h1', class_='name').text

    contents = []
    for floor in soup.find_all('div', class_='post-reply-list-container'):
        floor_box = floor.find('div', class_='thread-content-detail')
        if not floor_box:
            return None, None
        content = floor_box.text
        contents.append(content)
    return title, contents

def get_content_urls(list_url):
    res = session.get(list_url)
    content_urls = parse_list_page(res.text)
    return content_urls

def get_content(content_url):
    res = session.get(content_url)
    title, contents = parse_content_page(res.text)
    return title, contents

fs = []
url = 'https://bbs.hupu.com/acg'
fs.append(executor.submit(get_content_urls, url))
futures.wait(fs)
content_urls = set()
for f in fs:
    for url in f.result():
        content_urls.add(url)

fs = []
for url in content_urls:
    fs.append(executor.submit(get_content, url))
futures.wait(fs)
result = {}
for f in fs:
    title, contents = f.result()
    if title:
        result[title] = contents

for name, key in result.items():
    print('{}:\n{}'.format(name, key))
