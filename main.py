import time
import schedule as schedule
from bs4 import BeautifulSoup
import requests
import datetime
from pyfcm import FCMNotification

APIKEY = "Your Server Key"
url = 'https://www.smu.ac.kr/ko/life/restaurantView.do'
push_service = FCMNotification(APIKEY)


def get_menu():
    today = datetime.datetime.today().weekday()
    page = requests.get(url)
    html_doc = page.text
    soup = BeautifulSoup(html_doc, 'html.parser')
    smu_menu = []
    all_menu = soup.findAll('ul', {'class': 's-dot'})
    notice = all_menu[0]  # 시간 언젠지

    del all_menu[0]
    # 1~5까지는 학식 6~10까지는 컵밥
    # idx = 0~4까지 학식 5~9까지는 컵밥
    for i in range(len(all_menu)):
        smu_menu.append(all_menu[i].getText('li').replace('li', ''))


def sendMessage(body, title):
    # 메시지 (data 타입)
    data_message = {
        "body": body,
        "title": title
    }

    result = push_service.notify_topic_subscribers(topic_name="chicken", data_message=data_message)
    print(result)


# schedule.every(1).days.do(send_message)  # 3일마다 job 실행
schedule.every().day.at("08:30").do(sendMessage('asd','asd'))
# schedule.every().day.at("10:30").do(send_message)
while True:
    schedule.run_pending()
    time.sleep(1)
