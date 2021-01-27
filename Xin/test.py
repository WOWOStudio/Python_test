import requests
res = requests.get('http://www.wowo7.xyz')
with open('WOWO.txt','w') as file:
    file.write(res.text)
