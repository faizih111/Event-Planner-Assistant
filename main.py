from datetime import date
import math
import json
import re

event_name = " Birthday Party"
location = "Central Park"
exact_date = date(2025, 12, 25)
today_date = date.today()
left_day = exact_date - today_date

total_guests = 53
seats_per_table = 10
left_chair = math.ceil(53 / 10)


event = {"name": "Birthday Party", "location": "Central Park", "date": "2025-12-25"}
event_details = json.dumps(event)

txt = "Event Planner Assistant"
regex_check = "Event name is valid"

checking = re.findall("\s", txt)

print(f"Event Name:{event_name}")
print(f"Location:{location}")
print(f"Date:{today_date}")
print(f"Days left until event: :{left_day}\n")

print("Math Calculation:")
print(f"Total guests: {total_guests}")
print(f"Seats per table: {seats_per_table}")
print(f"Tables needed: {left_chair}\n")

print("Event details saved as JSON:")
print(event)

if checking:
    print(f"RegEx Check: {regex_check}")
else:
    print("No match")
