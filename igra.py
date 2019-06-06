#igra - pogodi broj

import random


tajnibroj = random.randint(1,30)
odgovor = 0

while odgovor != tajnibroj:
    odgovor = int(input("Pogodi broj od 1 - 30: "))

    if tajnibroj == odgovor:
        print("Bravo! Pogodili ste broj.")
    elif odgovor > tajnibroj:
        print("Niste pogodili broj, probajte neki manji")
    elif odgovor < tajnibroj:
        print("Niste pogodili broj, probajte neki veći")