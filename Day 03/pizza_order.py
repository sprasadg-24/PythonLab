print("Thank you for choosing Python Pizza Deliveries! ")
size = input('What size pizza do you want? S, M, or L ') # What size pizza do you want? S, M, or L
add_pepperoni = input('Do you want pepperoni? Y or N ') # Do you want pepperoni? Y or N
extra_cheese = input('Do you want pepperoni? Y or N ') # Do you want extra cheese? Y or N
# 🚨 Don't change the code above 👆
# Write your code below this line 👇
bill = 0
size = size.upper()
add_pepperoni =add_pepperoni.upper()

if size == 'S':
    bill  += 15
elif size == 'M':
    bill += 20
elif size == 'L':
    bill +=25
if add_pepperoni  == 'Y':
    if size == 'S':
        bill += 2
    else:
        bill += 3
if extra_cheese.upper() == 'Y':
    bill += 1
print(f"Your final bill is: ${bill}.")

 
