import random
import sys
total= 0
dealertotal = random.randint(7,20)
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
    if total > dealer :
        print("your total was", total, "the dealers total was", dealertotal, "you win")
    elif dealertotal > total:
        print("your total was",total,"dealer total was",dealertotal,"you lose")
    else :
        print("your total was",total,"dealer total was",dealertotal,"you drew")
        

print("please enter hit or fold")
if total >= 21:
    print("you lose")
    exit()
else:
    print("its not over yet")

hit_fold = input("would you like to hit or fold? ")
if hit_fold == "hit":
    card3 = random.randint(1,12)
    print("your third question is",card3)
    total = total+card3
    print("your current total is",total)
elif hit_fold == "fold":
    if total > dealertotal :
        print("your total was", total, "the dealers total was", dealertotal, "you win")
    elif dealertotal > total:
        print("your total was",total,"dealer total was",dealertotal,"you lose")
    else :
        print("your total was",total,"dealer total was",dealertotal,"you drew")
exit()
       
print("please enter hit or fold")
if total >= 21:
    print("you lose")
    exit()
else:
    print("its not over yet")

hit_fold = input("would you like to hit or fold? ")
if hit_fold == "hit":
    card4 = random.randint(1,12)
    print("your fourth card is",card4)
    total = total+card4
    print("your current total is",total)
elif hit_fold == "fold":
    if total > dealertotal :
        print("your total was", total, "the dealers total was", dealertotal, "you win")
    elif dealertotal > total:
        print("your total was",total,"dealer total was",dealertotal,"you lose")
    else :
        print("your total was",total,"dealer total was",dealertotal,"you drew")
exit()
       
        
print("please enter hit or fold")
if total >= 21:
    print("you lose")
    exit()
else : 
    print("its not over yet")

hit_fold = input("would you like to hit or fold? ")
if hit_fold == "hit":
    card5 = random.randint(1,12)
    print("your fith card is",card5)
    total = total+card5
    print("your current total is",total)
elif hit_fold == "fold":
    if total > dealertotal :
        print("your total was", total, "the dealers total was", dealertotal, "you win")
    elif dealer > total :
        print("your total was",total,"dealer total was",dealertotal,"you lose")
    else :
        print("your total was",total,"dealer total was",dealertotal,"you drew")
else:
    print("its not over yet")
exit()

print("please enter hit or fold")
if total >= 21:
    print("you lose")
    exit()
else : 
    print("its not over yet")
    
hit_fold = input("would you like to hit or fold? ")
if hit_fold == "hit":
    card6 = random.randint(1,12)
    print("your sixth card is",card6)
    total = total+card6
    print("your current total is",total)
elif hit_fold == "fold":
    if total > dealertotal :
        print("your total was", total, "the dealers total was", dealertotal, "you win")
    elif dealertotal > total:
        print("your total was",total,"dealer total was",dealertotal,"you lose")
    else :
        print("your total was",total,"dealer total was",dealertotal,"you drew")
    exit()
else :
    print("please enter hit or fold")
if total >= 21:
    print(
        "you lose")
    exit()
else : 
    print("its not over yet")

hit_fold = input("would you like to hit or fold? ")
if hit_fold == "hit":
    card7 = random.randint(1,12)
    print("your seventh card is",card7)
    total = total+card7
    print("your current total is",total)
elif hit_fold == "fold":
    if total > dealertotal :
        print("your total was", total, "the dealers total was", dealertotal, "you win")
    elif dealertotal > total:
        print("your total was",total, "dealer total was",dealertotal, " you lose")
    else :
        print("your total was",total, "dealer total was",dealertotal, "you drew")
        exit()
else:
    print("its not over yet")
print("please enter hit or fold")
if total >= 21:
    print("you lose")
    exit()
else : 
    print("its not over yet")
