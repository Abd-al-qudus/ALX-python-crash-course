#!/usr/bin/python3
user_age = input("Enter your age: ")
user_age_int = int(user_age)
#chain that determines a person’s stage of life


if user_age_int < 0:
    print("Error: Age cannot be negative")
if user_age_int < 2:
    print("You are a Baby")
elif user_age_int >= 2 and user_age_int < 4:
    print("You are a Toddler")
elif user_age_int >= 4 and user_age_int < 13:
    print("You are a kid")
elif user_age_int >= 13 and user_age_int < 20:
    print("You are a Teenager")
elif user_age_int >= 20 and user_age_int < 65:
    print("You are an Adult")
else:
    print("You are an Elder")
