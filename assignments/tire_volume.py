# I added option for the user to buy tires from the specifications entered and saved the user's phone number in volumes.txt if user accepts to buy and handled the situation if the user declines.

import math
from datetime import date


current_date = date.today()

width = float(input("Enter the width of the tire in mm (ex 205): "))
aspect_ratio = float(input("Enter the aspect ratio of the tire (ex 60): "))
diameter = float(input("Enter the diameter of the wheel in inches (ex 15): "))

volume = math.pi * math.pow(width,2) * aspect_ratio * (width * aspect_ratio + (2540 * diameter)) / math.pow(10,10)

with open("volumes.txt", "at") as file:
    file.write(f"{current_date}, {width:.0f}, {aspect_ratio:.0f}, {diameter:.0f}, {volume:.2f}\n")

print(f"The approximate volume is {volume:.2f} liters")

is_buying_tire = input("Do you want to buy a tire with the dimensions you entered? (Y/N) ").lower()

if is_buying_tire == "y" or is_buying_tire == "yes":
    phone = input("Input your phone number? ")
    with open("volumes.txt", "at") as file:
        file.write(f"{phone}\n")
        print("Thank you, have a nice day")
else: 
    print("Thank you, have a nice day")