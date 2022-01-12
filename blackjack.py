import random
import sys
total= 0
if total >= 21:
    print("you lose")
else:
    print("its not over yet")

print("welcome to blackjack")
card1 = random.randint(1,12)
print("your first card is",card1)
total = (total+card1)
hit_fold = input("would you like to hit or fold? ")
if hit_fold == "hit":
    card2 = random.randint(1,12)
    print("your scond card is",card2)
    total = total+card2
    print("your current total is",total)
elif hit_fold == "fold":
    print(total)
    print("you win")
    exit()
    
else :
    print("please enter hit or fold")
if total >= 21:
    print("you lose")
else:
    print("its not over yet")

hit_fold = input("would you like to hit or fold? ")
if hit_fold == "hit":
    card3 = random.randint(1,12)
    print("your third question is",card3)
    total = total+card2
    print("your current total is",total)
elif hit_fold == "fold":
    print(total)
    print("you win")
    exit()
else :
    print("please enter hit or fold")
if total >= 21:
    print("you lose")
else:
    print("its not over yet")

hit_fold = input("would you like to hit or fold? ")
if hit_fold == "hit":
    card4 = random.randint(1,12)
    print("your fourth card is",card4)
    total = total+card2
    print("your current total is",total)
elif hit_fold == "fold":
    print(total)
    print("you win")
    exit()
else :
    print("please enter hit or fold")
if total >= 21:
    print("you lose")
else : 
    print("its not over yet")

hit_fold = input("would you like to hit or fold? ")
if hit_fold == "hit":
    card5 = random.randint(1,12)
    print("your fith card is",card5)
    total = total+card2
    print("your current total is",total)
elif hit_fold == "fold":
    print(total)
    print("you win")
    exit()
else :
    print("please enter hit or fold")
if total >= 21:
    print("you lose")
else : 
    print("its not over yet")
    
hit_fold = input("would you like to hit or fold? ")
if hit_fold == "hit":
    card6 = random.randint(1,12)
    print("your sixth card is",card6)
    total = total+card2
    print("your current total is",total)
elif hit_fold == "fold":
    print(total)
    print("you win")
    exit()
else :
    print("please enter hit or fold")
if total >= 21:
    print("you lose")
else : 
    print("its not over yet")

hit_fold = input("would you like to hit or fold? ")
if hit_fold == "hit":
    card7 = random.randint(1,12)
    print("your seventh card is",card7)
    total = total+card2
    print("your current total is",total)
elif hit_fold == "fold":
    print(total)
    print("you win")
    exit()
else :
    print("please enter hit or fold")
if total >= 21:
    print("you lose")
else : 
    print("its not over yet")
