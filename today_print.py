import datetime
import time

import discord
from bs4 import BeautifulSoup
import requests
import datetime

url = 'https://www.smu.ac.kr/ko/life/restaurantView.do'
smu_menu = []
discord_token = 'ADD Your Key'
intents = discord.Intents.default()
intents.message_content = True


#월 : 0 화 : 1 수 : 2 목 : 3 금 : 4
today = datetime.datetime.today().weekday()


def get_menu(idx):
    page = requests.get(url)
    html_doc = page.text
    soup = BeautifulSoup(html_doc, 'html.parser')
    all_menu = soup.findAll('ul', {'class': 's-dot'})
    notice = all_menu[0]  # 시간 언젠지

    del all_menu[0]
    # 1~5까지는 학식 6~10까지는 컵밥
    # idx = 0~4까지 학식 5~9까지는 컵밥
    for i in range(len(all_menu)):
        smu_menu.append(all_menu[i].getText('li').replace('li', ''))

    result = str(smu_menu[idx])
    return result


def today_message(msg):
    # get_menu()
    today = datetime.datetime.today().weekday()
    if msg == 'give_me_haksik':
        result = get_menu(today)
        return result
    elif msg == "give_me_others":
        result = get_menu(today + 5)
        return result
    else:
        help_msg = "[명령어 메뉴]\n!give_me_haksik : 학식메뉴 불러오기 \n!give_me_others : 컵밥메뉴 불러오기"
        return help_msg
print(today_message('give_me_haksik'))
print(today_message('give_me_others'))
print(today_message('help'))
