# 모듈 임포트(판다스, 셀레니움, 웹드라이버, 키, 바이, 뷰티풀숲)
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup

# 웹드라이버 로드
driver = webdriver.Chrome()
# 지니차트200 페이지 접속 후 정보 얻어오기
url = "https://www.genie.co.kr/chart/top200"
driver.get(url)

# 얻어온 HTML소스를 파싱하기위해 Soup객체로 변환
html = driver.page_source
soup = BeautifulSoup(html, "html.parser")

# 파싱한 정보를 저장하기 위해 리스트 생성
song_data = []
rank = 1
# 1~4페이지까지 순차적으로 반복
for page in range(1, 5):
    print("페이지", page)
    # 묵시적 대기 2초
    driver.implicitly_wait(2)
    # 차트가 있는 Table에서 반복되는 요소 <tr>을 얻어옴,
    songs = soup.select("tbody > tr")
    for song in songs:
        # 노래 제목
        title = song.select("a.title.ellipsis")[0].text.strip()
        # 가수
        singer = song.select("a.artist.ellipsis")[0].text
        # 제목과 가수,순위까지 새로운 리스트를 생성 후 추가
        song_data.append(["Genie", rank, title, singer])
        rank += 1
    # 페이지 바로가기 버튼의 Xpath를 파악한 후 f-String으로 처리
    if page < 4:
        # 각 버튼은 [1]~[4]까지의 패턴을 가지고 있음
        driver.find_element(
            By.XPATH, f'//*[@id="body-content"]/div[7]/a[{page+1}]'
        ).click()
    driver.implicitly_wait(5)
    # 1~4페이지까지 페이지번호 링크를 누르면서 순차적으로 크롤링

# 크롤링이 완료되면 판다스를 이용해서 엑셀로 저장
columns = ["서비스", "순위", "타이틀", "가수"]
# 데이터프레임 생성 시 컬럼을 하나 추가
pd_data = pd.DataFrame(song_data, columns=columns)
# 최상위 5개의 데이터 확인
print(pd_data.head())
pd_data.to_excel("../01PythonGrammar/saveFiles/genie_chart.xlsx", index=False)
