from selenium import webdriver
import time
time.sleep(2)
options = webdriver.ChromeOptions()
options.add_argument('--headless')
browser = webdriver.Chrome(options=options)
browser.get('http://10.2.5.251/')
inputI = browser.find_elements_by_class_name('edit_lobo_cell')
inputI[1].send_keys('08183098')
inputI[2].send_keys('230052')
clickI = browser.find_elements_by_tag_name('option')
clickI[3].click()
clickII = browser.find_element_by_class_name('edit_lobo_cell')
browser.execute_script("arguments[0].click();", clickII)
browser.quit()