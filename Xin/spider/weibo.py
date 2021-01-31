#微博自动发微博
import requests
class WeiboSpider:
    def __init__(self):
        self.session=requests.Session()
        self.headers = {
            'user-agent':'',
            'referer':'',
            'cookie':''
        }
        self.session.headers.update(self.headers)
    def login(self):
        login_data = {
            'username': '18792303289',
            'password': 'Xx18792303289',
            'savestate': '1',
            'r': 'https://m.weibo.cn/',
            'ec': '0',
            'pagerefer': 'https://m.weibo.cn/',
            'entry': 'mweibo',
            'wentry':'',
            'loginfrom':'',
            'client_id':'',
            'code':'',
            'qq':'',
            'mainpageflag': '1',
            'hff':'',
            'hfp': ''
        }
        self.session.post('https://passport.weibo.cn/sso/login',data=login_data)
    def get_st(self):
        config_req = self.session.get('https://m.weibo.cn/api/config')
        config = config_req.json()
        st = config['data']['st']
        return st
    def compose(self,content):
        compose_data = {
            'content': content,
            'st': self.get_st(),
        }
        comment_req = self.session.post('https://m.weibo.cn/api/statuses/update',data=compose_data)
        print(comment_req.status_code)
    def send(self,content):
        self.login()
        self.compose(content)

weibo = WeiboSpider()
weibo.send('本条微博由 Python 发送')
