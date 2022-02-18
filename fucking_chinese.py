import sys
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
import time

def initSet():
    global driver

    driver = webdriver.Chrome('chromedriver.exe')
    driver.implicitly_wait(15)

    driver.maximize_window()
    time.sleep(1)

def getLogin(limit_time):
    global driver

    print("[i] weibo QR 로그인")

    start_url = 'https://weibo.com/newlogin?tabtype=weibo&gid=102803&url=https%3A%2F%2Fweibo.com%2F'
    driver.get(start_url)
    driver.implicitly_wait(15)

    login_button = driver.find_element_by_xpath('/html/body/div/div[1]/div[2]/div[2]/main/div[2]/div/div/div[1]/div[1]/div/button')
    login_button.click()

    print("[w] weibo QR 로그인 제한시간")

    for i in range(limit_time):
        print(limit_time - i)
        time.sleep(1)
    print("...")
    time.sleep(5)

    if start_url == driver.current_url:
        print("[e] weibo QR 로그인 실패")
        driver.quit()
        sys.exit()

    print("[s] weibo QR 로그인 성공")

def runMain():
    global driver

    for i in range(len(tags)):
        tag = tags[i]

        driver.get('https://s.weibo.com/weibo?q=%23'+tag+'%23')
        driver.implicitly_wait(15)
        time.sleep(2)

        page_limit = len(driver.find_elements_by_xpath("//div[@class='m-page']//span[@class='list']/ul/li"))

        print("[i] " + tag + " 태그로 이동 (page: "+str(page_limit)+"개)")

        for j in range(page_limit):
            page = j+1

            driver.get('https://s.weibo.com/weibo?q=%23' + tag + '%23&page='+str(page))
            driver.implicitly_wait(15)
            time.sleep(2)

            post_limit = len(driver.find_elements_by_xpath("//div[@id='pl_feed_main']/div[@id='pl_feedlist_index']/div[4]/div"))

            print("[i] " + str(page) + " page로 이동 (post: "+str(post_limit)+"개)")

            for k in range(post_limit):
                post = k+1

                driver.get('https://s.weibo.com/weibo?q=%23' + tag + '%23&page=' + str(page))
                driver.implicitly_wait(15)
                time.sleep(2)

                print("[i] " + str(post) + " 번째 게시글로 이동")

                comment_button = driver.find_element_by_xpath(
                    "//div[@id='pl_feedlist_index']/div[4]/div["+str(post)+"]/div[@class='card']/div[@class='card-act']/ul/li[2]/a"
                )
                comment_button.click()
                time.sleep(2)

                text_area = driver.find_element_by_xpath(
                    "//div[@id='pl_feedlist_index']/div[4]/div["+str(post)+"]/div[@class='card']/div[3]//div[@class='input-wrap input-wrap-review']/div[@class='input']/textarea"
                )
                text_area.send_keys(comments[k])

                submit_button = driver.find_element_by_xpath(
                    "//div[@id='pl_feedlist_index']/div[4]/div[" + str(post) + "]/div[@class='card']/div[3]//div[@class='input-wrap input-wrap-review']/div[@class='func']/div[@class='btn']/a"
                )
                submit_button.click()
                time.sleep(3)

                is_error = False

                try:
                    driver.find_element_by_xpath("/body/div[@class='m-layer']")
                except NoSuchElementException:
                    is_error = True

                if is_error:
                    print("[e] 댓글을 못쓰는 게시글 입니다")
                else:
                    print("[s] 댓글을 성공적으로 작성하였습니다")


driver = None
tags = [
    '黄大宪犯规',
    '韩国选手拒绝采访直接离场',
]
comments = [
    'test1',
    'test2',
    'test3',
    'test4',
    'test5',
    'test6',
    'test7',
    'test8',
    'test9',
    'test10',
    'test11',
    'test12',
    'test13',
    'test14',
    'test15',
    'test16',
    'test17',
    'test18',
    'test19',
    'test20',
    'test21',
    'test22',
    'test23',
    'test24',
    'test25',
    'test26',
    'test27',
    'test28',
    'test29',
    'test30',
    'test31',
    'test32',
    'test33',
    'test34',
    'test35',
    'test36',
    'test37',
]

initSet()
getLogin(18)
runMain()

"""""""""
# 이전 창으로 이동 2번하기
driver.back()
driver.back()

# 다음 창으로 2번 이동하기
driver.forward()
driver.forward()
"""""""""

#driver.quit()