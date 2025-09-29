import numpy as np

def generate(p1):
    # change this so that it generates 10000 random zeros and ones
    # where the probability of one is p1
    seq = np.random.choice([0,1], p=[1-p1, p1], size=10000)
    return seq

def count(seq):
    # insert code to return the number of occurrences of 11111 in the sequence
    counter = 0
    array = [1,1,1,1,1]
    n = len(array)
    for i in range(len(seq)-n+1):
        if list(seq[i:i+n]) == array:
            counter+=1   
    return counter

def main(p1):
    seq = generate(p1)
    return count(seq)

print(main(2/3))
