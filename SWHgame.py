# Snake Water Gun game

import random as r

def result(user,comp):
    if user==comp:
        return "Match is DRAW."
    elif ((user==0 and comp==1) or (user==1 and comp==2) or (user==2 and comp==0)):
        return "You WIN."
    elif ((user==0 and comp==2) or (user==1 and comp==0) or (user==2 and comp==1)):
        return "You LOST."
    else:
        return "Please gives a correct input."
    

print("Here, 0=Snake, 1=Water, 2=Gun")
l=[0, 1, 2]
comp=r.choice(l)

user=int(input("Enter any digit:"))
print(f"The computer gives: {comp}")
print(result(user,comp))