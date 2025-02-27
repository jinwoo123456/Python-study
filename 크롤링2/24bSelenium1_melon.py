from selenium import webdriver

driver = webdriver.Chrome()

driver.implicitly_wait(5)

url = "https://www,melon.com/chart/index.htm"
driver.get(url)
html = driver.page_source

from bs4 import BeautifulSoup

soup = BeautifulSoup(html, "html.parser")

song_data = []

rank = 1

song = soup.select("tbody > tr")

for song in songs:
    # 노래제목
    title = song.select("div.ellipsis.rank01 > span > a")[0].text
    # 가수
    singer = song.select("div.ellipsis.rank02 > a")[0].text
    # 좋아요 갯수
    favo = song.select("td:nth-child(8) > div > button > span.cnt")[0].text
    print(title, singer, favo, sep="|")
    song_data.append(["Melon", rank, title, singer, favo])
    rank += 1

import pandas as pd

coloumns = ["서비스", "순위", "타이틀", "가수", "좋아요"]
pd_data = pd.DataFrame(song_data, columns=columns)
print(pd_data.head())
pd_data.to_excel("../01PythonGrammar/saveFiles/melon_chart.xlsx", index=False)
