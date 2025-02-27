from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

# 드라이버 로드
driver = webdriver.Chrome()

# 네이버 메인에 접속
url = "https://www.naver.com/"
driver.get(url)

# XPath를 이용해서 네이버 메인의 로그인 버튼을 클릭
driver.find_element(By.XPATH, '//*[@id="account"]/div/a').click()
# 로드와 상관없이 무조건 2초 대기
time.sleep(2)

# 입력 후 로그인 버튼을 클릭해서 로그인 시도
driver.find_element(By.NAME, "id").send_keys("dnwls0622")
# 셀레니움 로그인을 감지하므로 캡쳐 화면이 뜬다
time.sleep(2)
# 조금 긴 시간을 대기하면서 직접 입력해야한다.

# 로그인이 완료되면 메인으로 자동 이동하므로 상단의 검색창에 검색어를 입력
driver.find_element(By.NAME, "pw").send_keys("ksd90430@")

time.sleep(2)

# 검색 버튼을 눌러서 결과를 확인
driver.find_element(By.XPATH, '//*[@id="log.login"]').click()
time.sleep(30)

driver.find_element(By.NAME, "query").send_keys("셀레니움")
time.sleep(2)

driver.find_element(By.CLASS_NAME, "btn_search").click()
time.sleep(10)
