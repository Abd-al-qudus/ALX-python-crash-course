#!/usr/bin/python3
alien_color = ["green", "yellow", "red"]
#Turn your if-else chain from Exercise 5-4 into an if-elifelse chain


for alien_selection in alien_color:
    if alien_selection == "green":
        print("You've just earned 5 points for shooting the alien GREEN")
    elif alien_selection == "yellow":
        print("You've just earned 10 points for shooting the alien YELLOW")
    else:
        print("You've just earned 15 points for shooting the alien RED")
