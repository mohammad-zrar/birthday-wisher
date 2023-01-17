#!/usr/bin/python3

 #################### Extra Hard Starting Project ######################
import pandas
import smtplib
import random
import datetime as dt
import os

PLACEHOLDER = "[NAME]"
MY_EMAIL = os.environ.get("MY_EMAIL")
MY_PASSWORD = os.environ.get("MY_PASSWORD")


# 1. Update the birthdays.csv
data = pandas.read_csv("birthdays.csv")
info = data.to_dict(orient="records")

# 2. Check if today matches a birthday in the birthdays.csv
today = dt.datetime.now()
month = today.month
day = today.day
#
# for person in info:
#     if person["month"] == month and person["day"] == day:
#         letter_path = f"letter_templates/letter_{random.randint(1, 3)}.txt"
#         with open(letter_path) as letter:
#             letter_content = letter.read()
#             new_letter = letter_content.replace(PLACEHOLDER, person["name"])
#             message = f"subject:Happy birthday\n\n{new_letter}"
#             with smtplib.SMTP("smtp.gmail.com", 587) as connection:
#                 connection.starttls()
#                 connection.login(user=MY_EMAIL, password=MY_PASSWORD)
#                 connection.sendmail(
#                     from_addr=MY_EMAIL,
#                     to_addrs=person["email"],
#                     msg=message
#                 )

# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME]
# with the person's actual name from birthdays.csv

# 4. Send the letter generated in step 3 to that person's email address.
