import random

def randInt(min=0,max=100):
     x = random.random()
     x *= (max-min)
     x += min
     return int(x)