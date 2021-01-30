#
from selenium import webdriver
import time
browser = webdriver.Chrome()
browser.get('https://wpblog.x0y1.com')
login_btn = browser.find_element_by_link_text('登录')
login_btn.click()
user_login = browser.find_element_by_id('user_login')
user_login.send_keys('codetime')
user_pass = browser.find_element_by_id('user_pass')
user_pass.send_keys('shanbay520')
wp_submit = browser.find_element_by_id('wp-submit')
wp_submit.click()
more_link = browser.find_element_by_class_name('more-link')
more_link.click()
comment = browser.find_element_by_id('comment')
comment.send_keys('自动评论')
time.sleep(3)
submit = browser.find_element_by_id('submit')
submit.click()
browser.quit()

