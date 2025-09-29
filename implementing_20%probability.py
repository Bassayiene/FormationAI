import random
prob = 0.20


def luckGame():
    if random.random() < prob:
        return "you win"
    else :
        return "you lose"
    

def wins():
    wins = 0
    for i in range(1000):
        if luckGame() == "you win":
            wins +=1
    return wins

def avg():
    sum = 0
    for i in range(1000):
        sum+= wins()
    return sum/10000

print("the average : %f per cent" % avg())

    


    

