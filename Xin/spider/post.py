#发送邮件
import yagmail

user = '2846941483@qq.com'
password = ''
host = 'smtp.qq.com'
to = ['2737539721@qq.com', '18792303289@163.com']
subject = '音乐评论'
contents = ['这是音乐评论哈~', 'C:\\mywork\\Python_test\\Xin\\spider\\音乐评论.csv']

yag = yagmail.SMTP(user=user, password=password, host=host)
yag.send(to=to, subject=subject, contents=contents)
