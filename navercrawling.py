#네이버 실시간 검색어 크롤링 : http://rednooby.tistory.com/106

import requests
from bs4 import BeautifulSoup

html=requests.get('http://www.naver.com/').text
# print(html) 전체가 나온다

soup=BeautifulSoup(html,'html.parser')

#title_list=soup.select('.PM_CL_realtimeKeyword_rolling')
#실시간 검색어들끼리 출력 print(title_list)

title_list=soup.select('.PM_CL_realtimeKeyword_rolling span[class*=ah_k]')
#PM_CL_realtimeKeyword_rolling 안에 ah_k를 가지고 있는 모든 class를 불러온다 print(title_list)

for idx, title in enumerate(title_list, 1):
    print(idx, title.text)
#불필요한 span 태그 제거
#text를 사용하여 값만 빼오며 enumerate를 사용하여 넘버링하기
