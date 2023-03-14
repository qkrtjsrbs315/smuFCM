from bs4 import BeautifulSoup
import requests
import  datetime

url = 'https://www.smu.ac.kr/ko/life/restaurantView.do'
today = datetime.datetime.today().weekday()
print(today)

page = requests.get(url)
html_doc = page.text
soup = BeautifulSoup(html_doc,'html.parser')
smu_menu = []
all_menu = soup.findAll('ul', {'class':'s-dot'})
notice = all_menu[0] #시간 언젠지

del all_menu[0]
#1~5까지는 학식 6~10까지는 컵밥
#idx = 0~4까지 학식 5~9까지는 컵밥
for i in range(len(all_menu)):
    smu_menu.append(all_menu[i].getText('li').replace('li',''))

