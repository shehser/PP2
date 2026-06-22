from datetime import datetime, timedelta

#Task no1
current_date = datetime.now()
result_date = current_date - timedelta(days=5)
print(result_date.strftime("%d-%m-%Y"))

#Task no2
today = datetime.now()
yesterday = today - timedelta(days=1)
tomorrow = today + timedelta(days=1)
print(yesterday.strftime("%d-%m-%Y"))
print(today.strftime("%d-%m-%Y"))
print(tomorrow.strftime("%d-%m-%Y"))
#Task no3
now_with_ms = datetime.now()
now_without_ms = now_with_ms.replace(microsecond=0)
print(now_without_ms)

#Task no4
date1 = datetime.now()
date2 = date1 - timedelta(days=1)
difference = date1-date2
seconds_diff = difference.total_seconds()
print(seconds_diff)
