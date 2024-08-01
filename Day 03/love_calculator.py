print("The Love Calculator is calculating your score...")
name1 = input('What is your name? ') # What is your name?
name2 = input('What is their name? ') # What is their name?
# 🚨 Don't change the code above 👆
# Write your code below this line 👇
couple_name = (name1 + name2).upper()
T = couple_name.count('T')
R = couple_name.count('R')
U = couple_name.count('U')
E = couple_name.count('E')
true = T+R+U+E
L = couple_name.count('L')
O = couple_name.count('O')
V = couple_name.count('V')
E = couple_name.count('E')
love = L+O+V+E

score = int(str(true)+ str(love))
if score < 10 or score > 90:
    print(f'Your score is {score}, you go together like coke and mentos.')
elif score > 40 and score < 50:
    print(f'Your score is {score}, you are alright together.')
else:
    print(f'Your score is {score}.')
