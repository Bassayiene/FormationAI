import random

def main():

    random_number = random.random()  # picking a random number 
    if random_number < 0.8 : 
        favourite = "dogs"  # dogs have 80% chances to be picked
    elif 0.8 <= random_number < 0.9 : 
        favourite = "cats" # cats have 10% chances to be picked
    else :
        favourite = "bats" # bats have 10% chances to be picked
        
    print("I love " + favourite) 

main()