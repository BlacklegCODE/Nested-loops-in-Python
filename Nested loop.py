

#nested loops practice in python !!

rows = int(input("Enter number of rows :"))
cols = int(input("Enter columns :"))

sy = input("Enter symbol :")

for x in range(rows):
    for y in range(cols):
        print(sy, end="")
    print()
