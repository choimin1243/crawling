import time
import requests
from bs4 import BeautifulSoup

pages=[]

page_num=1


while True:
    response=requests.get("http://www.ssg.com/search.ssg?target=all&query=nintendo&page="+str(page_num))
    soup=BeautifulSoup(response.text,'html.parser')

    if len(soup.select('.csrch_tip'))==0:
        pages.append(soup)
        print(str(page_num)+"번째 페이지 가져오기 완료")
        page_num+=1
        time.sleep(3)

    else:
        break

print(len(page_num))
