# for petlja

import random

tajnibroj = random.randint (1,30)

for x in range(5):

    pogodi = int(input("Pogodi jedan proj između 1 i 30: "))

    print(x)

    if tajnibroj == pogodi:
        print("Bravo pogodio si to je bio broj ", tajnibroj)
        break
    else:
        print("Fulao si pokušaj ponovno...")

print("Kraj programa")