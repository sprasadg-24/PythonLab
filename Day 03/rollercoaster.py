print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))
if height > 120:
    print("You can ride the rollercoaster!")
    age = int(input("Enter your age: "))
    bill = 0
    if age > 18:
        bill+= 12
        print(f"You pay : ${bill}")
    else : 
        bill +=7
        print(f"You pay : ${bill}")


else:
    print("Sorry, you have to gro taller before you can ride.")