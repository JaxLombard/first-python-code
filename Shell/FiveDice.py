import random
keep_going = True
while keep_going:
    dice = [0,0,0,0,0]
    for i in range(5):
        dice[i] = random.randint(1,6)
    print("You rolled:", dice)
    dice.sort()
    if dice[0] == dice[4]:
        print("Yahtzee!")
    elif (dice[0] == dice[3]) or (dice[1] == dice[4]):
        print("Four of a kind!")
    elif (dice[0] == dice[2]) or (dice[1] == dice[3]) or (dice[2] == dice[4]):
        print("Three of a kind!")
    keep_going = (input("Hit [ENTER] to keep going, any key to exit: ") == "")
    
          
    
