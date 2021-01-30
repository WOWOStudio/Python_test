#爬qq音乐歌曲评论
import requests
import time
headers = {
    'user-agent':''
}
lasthotcommentid = ''
comments = []
for pagenum in range(5):
    params = {
        "g_tk_new_20200303":"5381",
        "g_tk":"5381",
        "loginUin":"0",
        "hostUin":"0",
        "format":"json",
        "inCharset":"utf8",
        "outCharset":"GB2312",
        "notice":"0",
        "platform":"yqq.json",
        "needNewCode":"0",
        "cid":"205360772",
        "reqtype":"2",
        "biztype":"1",
        "topid":"212877900",
        "cmd":"8",
        "needmusiccrit":"0",
        "pagenum":pagenum,
        "pagesize":"5",
        "lasthotcommentid": lasthotcommentid,
        "domain":"qq.com",
        "ct":"24",
        "cv":"10101010"
    }
    res = requests.get('https://c.y.qq.com/base/fcgi-bin/fcg_global_comment_h5.fcg',headers = headers,params = params)
    data = res.json()
    for item in data['comment']['commentlist']:
        if 'rootcommentcontent' in item:
            comments.append((item['nick'],item['rootcommentcontent']))
    lasthotcommentid = data['comment']['commentlist'][-1]['commentid']
    time.sleep(1)
comments = set(comments)
for nick,content in comments:
    print('{}:{}'.format(nick,content))
