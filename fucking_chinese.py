import sys
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome('chromedriver.exe')
driver.implicitly_wait(15)

driver.maximize_window()
time.sleep(1)

start_url = 'https://weibo.com/newlogin?tabtype=weibo&gid=102803&url=https%3A%2F%2Fweibo.com%2F'
driver.get(start_url)
driver.implicitly_wait(15)

login_button = driver.find_element_by_xpath('/html/body/div/div[1]/div[2]/div[2]/main/div[2]/div/div/div[1]/div[1]/div/button')
login_button.click()

print("[w] weibo QR 로그인 제한시간")
limit_time = 10
for i in range(limit_time):
    print(limit_time-i)
    time.sleep(1)
print("...")
time.sleep(5)

if start_url == driver.current_url:
    print("[e] weibo QR 로그인 실패")
    driver.quit()
    sys.exit()

print("[s] weibo QR 로그인 성공")

words = [
    '黄大宪犯规'
]
comment_words = ["test"*(i+1) for i in range(5)]

page_number = 2
post_number = 1

driver.get('https://s.weibo.com/weibo?q=%23'+words[0]+'%23&page='+str(page_number))
driver.implicitly_wait(15)
time.sleep(2)

posts = driver.find_elements_by_class_name('card-wrap')
print(len(posts)-5)

for i in range(5):
    post_number = i+1

    comment_button = driver.find_element_by_xpath('/html/body/div[1]/div[2]/div/div[2]/div[1]/div[4]/div['+str(post_number)+']/div['+str(page_number)+']/div[2]/ul/li[2]/a')
    comment_button.click()
    time.sleep(2)

    comment_text_box = driver.find_element_by_xpath('/html/body/div[1]/div[2]/div/div[2]/div[1]/div[4]/div[' + str(
        post_number) + ']/div[2]/div[3]/div/div[1]/div/div[2]/div[1]/textarea')
    comment_text_box.send_keys(comment_words[i])
    time.sleep(1)

    submit_button = driver.find_element_by_xpath('/html/body/div[1]/div[2]/div/div[2]/div[1]/div[4]/div[' + str(
        post_number) + ']/div[2]/div[3]/div/div[1]/div/div[2]/div[2]/div/a')
    submit_button.click()
    time.sleep(2)

    driver.refresh()
    driver.implicitly_wait(15)
    time.sleep(2)

    print('[i] ' + str(post_number) + '번째 게시글 조회 완료')

"""""""""
# 이전 창으로 이동 2번하기
driver.back()
driver.back()

# 다음 창으로 2번 이동하기
driver.forward()
driver.forward()
"""""""""

#driver.quit()