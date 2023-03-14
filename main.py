from bs4 import BeautifulSoup
import requests

url = 'https://www.smu.ac.kr/ko/life/restaurantView.do'

page = requests.get(url)
html_doc = page.text
soup = BeautifulSoup(html_doc,'html.parser')

#all_menu = soup.find_all('tr')
#print(all_menu[3]) #2

all_menu = soup.findAll('ul', {'class':'s-dot'})
notice = all_menu[0] #시간 언젠지
mon = all_menu[1].getText('li')
mon = mon.replace('li','')

tue = all_menu[2].getText('li')
tue = tue.replace('li','')

wends = all_menu[3].getText('li')
wends = wends.replace('li','')

thu = all_menu[4].getText('li')
thu = thu.replace('li','')

fri = all_menu[5].getText('li')
fri = fri.replace('li','')

print(all_menu[1].getText('li').replace('li',''))
cupbab = all_menu[6].getText('li')
print(cupbab)