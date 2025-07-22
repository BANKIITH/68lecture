import random

heads = 1
tails = 2
tosses = 10

def tosses_coin():
    for toss in range(tosses):
        if random.randint(heads, tails) == heads:
            print("heads")
        else:
            print("tails")    

tosses_coin()