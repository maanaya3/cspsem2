#Marco A Anaya
#init
import random
c=0
g=[ "♥", "♦", "♠", "♣", "☆", "7", "⚀", "⚁", "⚂", "⚃", "⚄", "⚅"]
#variables
def slot():
    global c
    print("Welcome to Gambling 101")
    print("These are the slot machine choices: ♥, ♦, ♠, ♣, ☆, ⚀, ⚁, ⚂, ⚃, ⚄, ⚅, and 7")
    try:
        x=int(input("Please insert how much USD you would wish to enter. 1USD = 1 credit"))
    except:
        print("Please insert a value in USD")
    c=x
    while True:
        if c<10:
                b=int(input("Not enough credits for an additional spin remaining, insert additional cash"))
                c=b
        m= int(input("You have " + str(c)+" credits"))
        try:
            y=input("Press 's' to spin or 'q' to quit")
        except:
            print("ERROR, must type s or q to continue,")
        if y=="s":
            slot1=(random.choice(g))
            slot2=(random.choice(g))
            slot3=(random.choice(g))
            print(slot1)
            print(slot2)
            print(slot3)
            if slot1==7 and slot2==7 and slot3==7:
                print("You have won the grand jackpot!!!!")
                c=c+1000
            elif slot1==slot2==slot3:
                print("You have matched 3 in a row!!")
                c=c+100
            elif slot1==slot2 or slot1==slot3 or slot2==slot3:
                print("You got 2 of a kind! Your 10 credits are refunded")
            else:
                print("U suck, thx for ur money anyways)
                c=c-10
        elif y=="q":
            break

#main
slot()
