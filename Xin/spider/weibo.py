#微博自动发评论
import requests
class WeiboSpider:
    def __init__(self):
        self.session=requests.Session()
        self.headers = {
            'user-agent':'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.104 Mobile Safari/537.36',
            'referer':'https://passport.weibo.cn/signin/login?entry=mweibo&res=wel&wm=3349&r=https%3A%2F%2Fm.weibo.cn%2F',
            'cookie':'_T_WM=71847762812; XSRF-TOKEN=fc2f06; WEIBOCN_FROM=1110005030; SCF=Apa0tsI10GAfq-cBVcc61JcAhyH8QwhG0jC9ABNvuB76NGnoyxoCyOf7OqJnKgTiUYtsEWN7FeP-RvPW56yfzWI.; SUB=_2A25NEvKxDeRhGeBM41QX9CjKyTmIHXVu_J75rDV6PUJbktAfLW_skW1NRKDrrWRG20Tb7ypu3wjwYIIdWMQYF_vl; SUBP=0033WrSXqPxfM725Ws9jqgMF55529P9D9WFPHuNv69upsiLrgrB9lpCG5JpX5KzhUgL.FoqE1hqcShqceo-2dJLoIEBLxKnL1h.LB.-LxK.L1hzLB--LxK.LB.2LB.zLxK.LBonLB-Bt; SSOLoginState=1612088034; ALF=1614680034; MLOGIN=1; M_WEIBOCN_PARAMS=luicode=10000011&lfid=102803&uicode=20000174&fid=2304136286646625_-_WEIBO_SECOND_PROFILE_WEIBO'
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
