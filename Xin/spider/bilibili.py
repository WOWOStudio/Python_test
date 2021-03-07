#B站自动评论
import requests

headers={
    'user-agent':'',
    'Cookie':''
}

comment_data = {
    'oid': '671212394',
    'type': '1',
    'message': '666',
    'plat': '1',
    'ordering': 'heat',
    'jsonp': 'jsonp',
    'csrf': '96bbdd73fd14796fbcf41769e07e29e4'
}
session = requests.Session()
session.headers.update(headers)
comment_req = session.post('https://api.bilibili.com/x/v2/reply/add',data=comment_data)
print(comment_req.status_code)
