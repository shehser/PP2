#!/usr/bin/env python3

# dates.py
import datetime

# 1. Get current date and time
now = datetime.datetime.now()
print(f"Current full date/time: {now}")
print(f"Current year: {now.year}")

# 2. Formatting date strings using strftime()
# %A - weekday name, %B - month name
print(f"Weekday name: {now.strftime('%A')}")
print(f"Month name: {now.strftime('%B')}")
print(f"Readable format: {now.strftime('%Y-%m-%d %H:%M:%S')}\n")

# 3. Creating a specific date object
custom_date = datetime.datetime(2020, 5, 17)
print(f"Created custom date object: {custom_date}")
