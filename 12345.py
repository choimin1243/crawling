import requests
from bs4 import BeautifulSoup


response=requests.get("https://workey.codeit.kr/orangebottle/index")


soup=BeautifulSoup(response.text,'html.parser')

Number=soup.select('.phoneNum')

Number_text=[]

for i in Number:
    Number_text.append(i.text)


print(Number_text)