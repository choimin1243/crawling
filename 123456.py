import requests

from bs4 import BeautifulSoup
response=requests.get('https://workey.codeit.kr/music/index')
soup=BeautifulSoup(response.text,'html.parser')
li_tag=soup.select(".rank__order .list")

order_list=[]

for i in li_tag:
    order_list.append(i.text.strip().split()[2])


print(order_list)