myList = [
            ['#', '#', '-', '#', '-'], 
            ['-', '#', '-', '#', '-'],
            ['-', '#', '-', '#', '-'],
            ['-', '#', '-', '#', '-'],
        ]  

for x in range(len(myList)):
    if myList[x] == "#":
        myList[x] = 9


rows = len(myList)
for row in range(rows):
    cols = len(myList[row])
    print("Row", row, "has", cols, "columns: ", end="")
    for col in range(cols):
        print(myList[row][col], " ", end="")
    print()

