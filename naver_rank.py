import time, os, requests
from bs4 import BeautifulSoup
from termcolor import *
import colorama

colorama.init()

# naver로 부터 text, headers, ststus, ok 정보를 받아 req 오브젝트에 저장
req = requests.get('https://www.naver.com/')
html = req.text
header = req.headers
status = req.status_code
is_ok = req.ok

# 노란색 글씨
C_YELLOW = '\033[33m'
while True:
    soup = BeautifulSoup(html, 'html.parser')

    rank_title = soup.select(
        '#PM_ID_ct > div.header > div.section_navbar > div.area_hotkeyword.PM_CL_realtimeKeyword_base > div.ah_roll.PM_CL_realtimeKeyword_rolling_base > div > ul > li > a > span.ah_k'
    )
    rank_num = soup.select(
        '#PM_ID_ct > div.header > div.section_navbar > div.area_hotkeyword.PM_CL_realtimeKeyword_base > div.ah_roll.PM_CL_realtimeKeyword_rolling_base > div > ul > li > a > span.ah_r'
    )
    for i in range(20):
        if len(rank_num[i].text) == 1:
            cprint('0' + str(rank_num[i].text) + ' ' + rank_title[i].text, 'yellow')
        else:
            cprint(rank_num[i].text + ' ' + rank_title[i].text, 'yellow')

    time.sleep(10)
    os.system('cls')
