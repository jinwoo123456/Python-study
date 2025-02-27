# 모듈 임포트(판다스, 셀레니움, 웹드라이버, 키, 바이, 뷰티풀숲)
"""
이 스크립트는 Selenium과 BeautifulSoup을 사용하여 벅스의 실시간 음악 차트를 스크랩합니다.

모듈:
- pandas as pd: 데이터 조작 및 분석을 위해 사용.
- selenium.webdriver: 웹 브라우저 상호작용 자동화를 위해 사용.
- selenium.webdriver.common.keys: 키보드 입력을 시뮬레이션하기 위해 사용.
- selenium.webdriver.common.by: HTML 요소를 찾기 위해 사용.
- bs4 (BeautifulSoup): HTML 콘텐츠를 파싱하기 위해 사용.

함수:
- strip(): 문자열의 앞뒤 공백을 제거합니다.

작업 흐름:
1. 필요한 모듈을 임포트합니다.
2. Chrome WebDriver를 초기화합니다.
3. 벅스 실시간 음악 차트 URL로 이동합니다.
4. BeautifulSoup을 사용하여 HTML 소스를 파싱합니다.
5. 노래 제목과 아티스트를 추출합니다.
6. 추출한 데이터를 리스트에 저장합니다.
"""
# 판다스 모듈 임포트
import pandas as pd

# 셀레니움 웹드라이버 모듈 임포트
from selenium import webdriver

# 셀레니움 키 모듈 임포트 (키보드 입력을 자동화하는 데 사용)
from selenium.webdriver.common.keys import Keys

# 셀레니움 바이 모듈 임포트 (HTML 요소를 찾는 데 사용)
from selenium.webdriver.common.by import By

# 뷰티풀숲 모듈 임포트 (HTML 파싱을 위한 라이브러리)
from bs4 import BeautifulSoup

driver = webdriver.Chrome()

# 벅스차트
url = "https://music.bugs.co.kr/chart/track/realtime/total?wl_ref=M_contents_03_01"
driver.get(url)

# 얻어온 HTML소스를 파싱하기위해 Soup객체로 변환
html = driver.page_source
soup = BeautifulSoup(html, "html.parser")
song_data = []
rank = 1

# 암묵적 대기 (최대 10초)
driver.implicitly_wait(10)

# 노래 제목과 가수를 선택하는 CSS 선택자
songs = soup.select("tbody > tr")

# 상위 100곡의 제목과 가수를 추출하여 리스트에 저장
for song in songs:
    if rank % 10 == 0:
        driver.implicitly_wait(5)

    title_element = song.select("th[scope='row'] > p.title > a")
    singer_element = song.select("p.artist > a")

    if title_element and singer_element:
        title = title_element[0].text.strip()
        singer = singer_element[0].text.strip()
        song_data.append(["Bugs", rank, title, singer])
        rank += 1

col = ["서비스", "순위", "타이틀", "가수"]

df = pd.DataFrame(song_data, columns=col)
print(df.head())
df.to_excel("../01PythonGrammar/saveFiles/bugs_chart.xlsx", index=False)
