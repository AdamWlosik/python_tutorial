import random

def generuj_liczbe(min, max):
    return random.randint(min, max)

for i in range (0, 20):
    print(generuj_liczbe(0, 100))

