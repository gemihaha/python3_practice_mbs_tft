from selenium import webdriver
from bs4 import BeautifulSoup
from selenium.webdriver.common.keys import Keys
from datetime import datetime
import pandas as pd
import time
import re

driver = webdriver.Chrome('C:\\Users\\user\\chromedriver_win32\\chromedriver.exe')

print('크롤링 시작')



def getCmt(url):
    youtube_url = url
    driver.get(youtube_url)
    body = driver.find_element_by_tag_name('body')

    print('시작')

    num_of_pagedowns = 10
    datetime.today()

    while num_of_pagedowns:

        body.send_keys(Keys.PAGE_DOWN)
        time.sleep(2)
        num_of_pagedowns -= 1

        try:
            driver.find_element_by_xpath('//*[@id = "sort-menu"]').click()
            driver.find_element_by_xpath('//*[@id="menu"]/a[2]/paper-item/paper-item-body/div[text()="최근 날짜순"]').click()

        except Exception as e:
            pass
# 20에서 100으로 바꿈
    num_of_pagedowns = 100

    while num_of_pagedowns:
        body.send_keys(Keys.PAGE_DOWN)
        time.sleep(2)
        num_of_pagedowns -= 1

    html = driver.page_source

    result = BeautifulSoup(html, 'html.parser')
    body = result.find('body')

    title = body.find_all('yt-formatted-string', attrs={'class': 'style-scope ytd-video-primary-info-renderer'})
    title1 = title[0].get_text()
    print(title1)

    thread = body.find_all('ytd-comment-renderer', attrs={'class': 'style-scope ytd-comment-thread-renderer'})

    last = body.find('yt-formatted-string', attrs={'class':'count-text style-scope ytd-comments-header-renderer'})
    last = last.string

    print(last)
    last_t = re.sub('[^\d]','',last)
    last_t = int(last_t)
    plus_c = 0
    plus_cmt = body.find_all('span',attrs={'id':'more-text'})
    for count in plus_cmt:
        count = count.get_text().strip()
        if count == '답글 보기':
            plus_c += 1
        else:
            cmts = re.sub('[^\d]','',count)
            plus_c += int(cmts)

    cmtlist = []

    for items in thread:
        div = items.find_all('yt-formatted-string', attrs={'id': 'content-text'})
        div2 = items.select('yt-formatted-string > a')[0].get_text()
        for lists in div:
            if lists !=  None:
                try:
                    cmt = lists.string
                    textcmt = re.sub(r"[^\w]", ' ', cmt)
                    cmtlist.append([textcmt, div2])
                    print(textcmt)
                except TypeError as e:
                    pass

            else:
                pass
        num_c = (len(cmtlist) + plus_c)
        print(num_c)

        if num_c >= (last_t - 10) or num_c >= 1328:
            break
        print(div2)
        print('-' * 50)

    print(len(cmtlist))

    result = pd.DataFrame(cmtlist)
    result.to_csv('korea_vs_columbia.csv', encoding = 'utf-8')

# 데이브[요즘 음악 들은 세대별 반응]
i = 'https://www.youtube.com/watch?v=AFTBv_UNWGg'
#피 땀 눈물 MV 처음 본 방탄소년단
j = 'https://www.youtube.com/watch?v=Vtz1R5c2Y6Q'
#michelle choi
z = 'https://www.youtube.com/watch?v=_kVSWRPU4C0'
f = 'https://www.youtube.com/watch?v=7RQ1OswQ32M'
#hyundai review
h = 'https://www.youtube.com/watch?v=H9IcNuVcguA'
#soccer review
s = 'https://www.youtube.com/watch?v=Bxg1CqqkzE0'

getCmt(s)
