import time

import discord
from bs4 import BeautifulSoup
import requests
import datetime

url = 'https://www.smu.ac.kr/ko/life/restaurantView.do'
smu_menu = []
discord_token = 'Add Your Key'
intents = discord.Intents.default()
intents.message_content = True



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
        result = "```"+get_menu(today)+"```"
        return result
    elif msg == "give_me_others":
        result = "```"+get_menu(today+5)+"```"
        return result
    elif msg == "help":
        help_msg = "```[명령어 메뉴]\n!give_me_haksik : 학식메뉴 불러오기 \n!give_me_others : 컵밥메뉴 불러오기```"
        return help_msg
    else:
        error_msg = "we don't have that order keyword"
        return error_msg


# discord Client class를 생성합니다.
client = discord.Client(intents=intents)

# event decorator를 설정하고 on_ready function을 할당해줍니다.
@client.event
async def on_ready():  # on_ready event는 discord bot이 discord에 정상적으로 접속했을 때 실행됩니다.
    print('We have logged in as {}'.format(client))
    print('Bot name: {}'.format(client.user.name))  # 여기서 client.user는 discord bot을 의미합니다. (제가 아닙니다.)
    print('Bot ID: {}'.format(client.user.id))  # 여기서 client.user는 discord bot을 의미합니다. (제가 아닙니다.)


# event decorator를 설정하고 on_message function을 할당해줍니다.
@client.event
async def on_message(message):
    # message란 discord 채널에 올라오는 모든 message를 의미합니다.
    # 따라서 bot이 보낸 message도 포함이되죠.
    # 아래 조건은 message의 author가 bot(=clinet.user)이라면 그냥 return으로 무시하라는 뜻입니다.
    if message.author == client.user:
        return

    # message를 보낸 사람이 bot이 아니라면 message가 give로 시작하는 경우 채널에 급식이라는 글자를 보내라는 뜻입니다.
    elif message.content.startswith('!give_me_haksik'):
        info = today_message('give_me_haksik')
        await message.channel.send(info) #여기에 코드 박기
    elif message.content.startswith('!give_me_others'):
        info = today_message('give_me_others')
        await message.channel.send(info) #여기에 코드 박기
    elif message.content.startswith('!help'):
        info = today_message('help')
        await message.channel.send(info) #여기에 코드 박기


# 위에서 설정한 client class를 token으로 인증하여 실행합니다.
client.run(discord_token)