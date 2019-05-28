# while petlja

import random

tajnibroj = random.randint (1,30)

while True:

    pogodi = int(input("Pogodi jedan proj između 1 i 30: "))

    if tajnibroj == pogodi:
        print("Bravo pogodio si to je bio broj ", tajnibroj)
        break
    else:
        print("Fulao si pokušaj ponovno...")

print("Kraj programa")