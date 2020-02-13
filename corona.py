import requests
from bs4 import BeautifulSoup

url = "http://ncov.mohw.go.kr/bdBoardList.do"

response =  requests.get(url)
dom_a = BeautifulSoup(response.content, 'html.parser')

confirmation_patient = dom_a.select_one('.s_listin_dot > li:nth-of-type(1)').text.strip()
patient_isolation = dom_a.select_one('.s_listin_dot > li:nth-of-type(2)').text.strip()
inspection = dom_a.select_one('.s_listin_dot > li:nth-of-type(3)').text.strip()

print("1. 국내 확진환자 수 : ",confirmation_patient)
print("2. 확진환자 격리해제 : ",patient_isolation)
print("3. 검사진행 : ",inspection)
