rows = int(input("Enter in the amount of rows: "))
for r in range(1, rows + 1):
    for c in range(r):
        print(r, end = " ")
    print()