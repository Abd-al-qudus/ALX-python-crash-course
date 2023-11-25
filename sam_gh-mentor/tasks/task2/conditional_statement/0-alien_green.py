#!/usr/bin/python3
alien_color = ["green", "yellow", "red"]
choice_is_green = "Congratulations! You just earned 5 points!"
""" Imagine an alien was just shot down in a game Create a variable called alien_color and assign it a value of 'green', 'yellow', or 'red'"""


for alien_selection in alien_color:
    if alien_selection == "green":
        break
    else:
        continue

print(choice_is_green)
