import requests

headers={
    'user-agent':'',
    'Cookie':''
}
login_data={
    'entry': 'account',
    'gateway': '1',
    'from': 'null',
    'savestate': '30',
    'useticket': '0',
    'pagerefer': 'https://login.sina.com.cn/crossdomain2.php?action=logout&r=https%3A%2F%2Flogin.sina.com.cn',
    'vsnf': '1',
    'su': 'MTg3OTIzMDMyODk=',
    'service': 'account',
    'servertime': '1611927707',
    'nonce': '8ZXORH',
    'pwencode': 'rsa2',
    'rsakv': '1330428213',
    'sp': '7e032f9b981d974b09dac5b887b5f567f3e8d6412c2a2e9afd29992ec650103330feee78349cba9ad7941285645644cf2d8cb5d555767c8209b65d80ca1013e5e2d99dd40aa2ac68a63aa6f57f1e5b607114cfdee1de7acc353c88db3f3e8a674a08450723c2664e95b5b76698e535166de067026d064869afbf5aa4e100d914',
    'sr': '1536*864',
    'encoding': 'UTF-8',
    'cdult': '3',
    'domain': 'sina.com.cn',
    'prelt': '113',
    'returntype': 'TEXT'
}

comment_data = {
    'act': 'post',
    'mid': '4598802881716889',
    'uid': '6286646625',
    'forward': '1',
    'isroot': '0',
    'content': '....',
    'location': 'page_100206_home',
    'module': 'scommlist',
    'tranandcomm': '1',
    'pdetail': '1002061618051664',
    '_t': '0'
}
session = requests.Session()
session.headers.update(headers)
#login_req = session.post('https://login.sina.com.cn/sso/login.php?client=ssologin.js(v1.4.19)',data=login_data)
comment_req = session.post('https://weibo.com/aj/v6/comment/add?ajwvr=6&__rnd=1611930189794',data=comment_data)
print(comment_req.status_code)
