rows = int(input("Engtter in the amount of rows: "))
number = 1
for r in range(1, rows+1):
    for c in range(1, r+1):
        print(number, end = " ")
        number = number+1
    print()