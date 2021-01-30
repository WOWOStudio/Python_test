#B站自动评论
import requests

headers={
    'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36',
    'Cookie':'_uuid=7ED4E3EC-F7F6-54E9-007E-CF74A3F0881056700infoc; buvid3=25677BD8-BB23-42C5-90AF-F1421D56F7F6143098infoc; CURRENT_FNVAL=80; blackside_state=1; rpdid=|(kYJR|~Y|lu0J\'uY|ukm)lJm; LIVE_BUVID=AUTO8616036209854995; CURRENT_QUALITY=112; PVID=1; buvid_fp_plain=25677BD8-BB23-42C5-90AF-F1421D56F7F6143098infoc; buivd_fp=25677BD8-BB23-42C5-90AF-F1421D56F7F6143098infoc; bp_video_offset_501016466=479728158838631872; fingerprint=74a8917616fbe1ac4dac3e18f3b4f1cb; buvid_fp=25677BD8-BB23-42C5-90AF-F1421D56F7F6143098infoc; fingerprint3=75fdd721acc470860ffd05ce8026b6ad; fingerprint_s=14a8d1b3e65ae5132642ea00c5e3c25c; SESSDATA=65152d02%2C1627557294%2C7cba1%2A11; bili_jct=96bbdd73fd14796fbcf41769e07e29e4; DedeUserID=501016466; DedeUserID__ckMd5=5b25956dc92f7698; sid=iqreb8le'
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
