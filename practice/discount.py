import datetime as dt

total = 0
salestax = 0
discount = 0
subtotal = float(input("What's the subtotal? "))
weekday = dt.datetime.now().strftime("%A").lower()
print(weekday)
    


if subtotal >=50:
    discount = subtotal * 0.1
    subtotal = subtotal - discount
    salestax = (subtotal * 0.06)
    total = subtotal + salestax

    if weekday == "tuesday" or weekday == "wednesday":
        print(f"Your discount is ${discount:.2f}, sales tax amount is ${salestax:.2f}, and the total amount due is ${total:.2f} ")
    else: 
          print(f"There is no discount today, Your sales tax amount is ${salestax:.2f}, and the total amount due is ${total:.2f} ")

else:
    subtotal = subtotal - discount
    salestax = (subtotal * 0.06)
    total = subtotal + salestax

    if weekday == "tuesday" or weekday == "wednesday":
        discount_balance = 50 - subtotal
        print(f"You need to purchase an additional ${discount_balance} to be eligible for discounts")
    else:
         print(f"There is no discount today, Your sales tax amount is ${salestax:.2f}, and the total amount due is ${total:.2f} ")