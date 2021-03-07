from bs4 import BeautifulSoup
import requests
from concurrent import futures



# 解析列表页内容，得到部分链接
def parse_list_page(text):
    soup = BeautifulSoup(text, 'html.parser')
    tbody = soup.find('table', class_='board-list tiz').tbody
    urls = []
    for tr in tbody:
        td = tr.find('td', class_='title_9')
        urls.append(td.a.attrs['href'])
    return urls


# 解析内容页，得到标题和帖子内容
def parse_content_page(text):
    soup = BeautifulSoup(text, 'html.parser')
    title = soup.find('span', class_='n-left').text.strip('文章主题:').strip()
    content_div = soup.find('div', class_='b-content corner')
    contents = []
    for awrap in content_div.find_all('div', class_='a-wrap corner'):
        content = awrap.p.text
        contents.append(content)
    return title, contents


# 链接组合
def convert_content_url(path):
    URL_PREFIX = 'http://www.newsmth.net'
    path += '?ajax'
    return URL_PREFIX + path


# 生成前十页链接
list_urls = []
for i in range(1, 11):
    url = 'http://www.newsmth.net/nForum/board/Python?ajax&p='
    url += str(i)
    list_urls.append(url)

session = requests.Session()
executor = futures.ThreadPoolExecutor(max_workers=5)


# 生成真链接
def get_content_urls(list_url):
    res = session.get(list_url)
    content_urls = parse_list_page(res.text)
    real_content_urls = []
    for url in content_urls:
        url = convert_content_url(url)
        real_content_urls.append(url)
    return real_content_urls


# 为进程池提交任务，生成所有的真链接
fs = []
for list_url in list_urls:
    fs.append(executor.submit(get_content_urls, list_url))
futures.wait(fs)

content_urls = set()
for f in fs:
    for url in f.result():
        content_urls.add(url)


# 获取标题和帖子内容
def get_content(url):
    r = session.get(url)
    title, contents = parse_content_page(r.text)
    return title, contents


# 提交解析任务，解析帖子正文，获得所有帖子标题和内容
fs = []
for url in content_urls:
    fs.append(executor.submit(get_content, url))
futures.wait(fs)

results = {}
for f in fs:
    title, contents = f.result()
    results[title] = contents
for key, value in results.items():
    print('{}:{}'.format(key, value))
