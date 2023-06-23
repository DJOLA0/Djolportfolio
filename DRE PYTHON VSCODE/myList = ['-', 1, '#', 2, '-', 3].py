myList = [
            ['', '#', '-', '#', '-'], 
            ['-', '#', '-', '#', '-'],
            ['-', '#', '-', '#', '-'],
            ['-', '#', '-', '#', '-'],
        ]  

for i in range(len(myList)):
    if myList[i] == '-':
        myList[3][0] = 9

print(myList)
rows = len(myList)

for row in range(rows):
    cols = len(myList[row])
    print("Row", row, "has", cols, "columns: ", end="")
    for col in range(cols):
        print(myList[row][col], " ", end="")
    print()

