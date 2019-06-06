
broj1 = int(input("Unesi broj: "))
broj2 = int(input("Unesi drugi broj: "))
op = input("Odaberi operaciju! (+, -, *, /): ")


if op == "+":
    print(broj1 + broj2)
elif op == "-":
    print(broj1 - broj2)
elif op == "*":
    print(broj1 * broj2)
elif op == "/":
    print(broj1 / broj2)
else:
    print("Pogreška pri odabiru operacje! Pokušaj ponovno")