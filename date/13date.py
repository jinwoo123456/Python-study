import time
from datetime import date, datetime, timedelta

# 오늘 날짜와 년,월,일 출력
today = date.today()
print("오늘 날짜 :", today, today.year, today.month, today.day)
print("=" * 30)


# 현재 시각과 년,월,일,시,분,초,밀리세컨즈 출력ㅔㅛ
dtime = datetime.now()
print("현재 시각", dtime)
print("년/월/일", dtime.year, dtime.month, dtime.day)
print("시/분/초/밀리세컨즈", dtime.hour, dtime.minute, dtime.second, dtime.microsecond)

print("=" * 30)

# 날짜계산
one_day = timedelta(days=1)
yesterday = today - one_day
tomorrow = today + one_day
print("어제와 오늘", yesterday, today)

# 날짜계산2
data_diff = today - yesterday
print("날짜차이 : ", data_diff)

# 날짜형식
print("형식지정", today.strftime("%Y/%m/%d"))

# 크리스마스까지 남은 날짜 계산

# 올해 크리스마스 지정
x_mas_str = f"{today.year}-12-25"
# str -> datetime 타입으로 변환
x_mas_datetime = datetime.strptime(x_mas_str, "%Y-%m-%d")
# datetime -> date 타입으로 변환
x_mas_date = datetime.date(x_mas_datetime)
# 값 확인
print(x_mas_str, x_mas_datetime, x_mas_date)
# 타입 확인
print(type(x_mas_str), type(x_mas_datetime), type(x_mas_date))
# 크리스마스에서 오늘 날짜를 빼면 남은 날짜를 계산할 수 있음.
date_diff = x_mas_date - today
print("크리스마스까지 남은 날짜", date_diff)
print("크리스마스까지 남은 날짜", date_diff.days)
