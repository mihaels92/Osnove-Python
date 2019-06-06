
broj = int(input("Unesi broj: "))


if broj %7 == 0:
    print("Broj je djeljiv sa 7")
else:
    print("Broj nije djeljiv sa 7")


vrijeme = input("Unesi kakvo je vani vrijeme? (sunce, kiša, snijeg) ")


if vrijeme == "kiša":
    print("Ponesi kišobran")
elif vrijeme == "snijeg":
    print("Obuci čizme")
elif vrijeme == "sunce":
    print("Uzmi sunčane naočale")
else:
    print("Nije odabrano vrijeme! Pokušaj ponovno")