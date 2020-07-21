#Boxes
from random import *
from time import *
inventory = []
boxes = []
cM = 0
common = ["Rock", "Iron", "Wood", "Pistol", "Spear", "Arrow & Bow"]
c2 = ["Shotgun", "Gold", "Average PC", "MS-DOS", "Knuclers", "Car Engine"]
c3 = ["Automated Shotgun", "Laptop", "Medicine", "Map of the World", "Golf Cart"]
inv = open("items.txt", 'a+')
money = open("money.txt", 'a+')
boxInv = open("box.txt", 'a+')
Lines = inv.readlines()
inv.close()
Money = money.readlines()
money.close()
Boxes = boxInv.readlines()
boxInv.close()
for line in Lines:
    inventory.append(line)
for box in Boxes:
    boxes.append(line)
for money in Money:
    cM = str(money)
    cM = int(cM)
    money = str(money)
print ("Boxes V1")
while True:
    print ("What to do? (Buy/Unbox)")
    do = input("> ")
    if do == "Buy":
        print ("C Box - 10")
        print ("C2 Box - 30")
        print ("C3 Box - 90")
        do = input("> ")
        if do == "C Box":
            if cM > 10:
                boxes.append("C Box")
                cM -= 10
        elif do == "C2 Box":
            if cM > 30:
                boxes.append("C2 Box")
                cM -= 30
        elif do == "C3 Box":
            if cM > 90:
                boxes.append("C3 Box")
                cM -= 90
    elif do == "Unbox":
        print ("What box do you want to open?")
        print (", ".join(boxes))
        do = input("> ")
        if do in boxes:
            if do == "C Box":
                thing = choice(common)
                inv.append(thing)
                boxes.remove("C Box")
                print ("You got one " + thing)
            elif do == "C2 Box":
                thing = choice(c2)
                inv.append(thing)
                boxes.remove("C2 Box")
                print ("You got one " + thing)
            elif do == "C3 Box":
                thing = choice(c3)
                inv.append(thing)
                boxes.remove("C3 Box")
                print ("You got one " + thing)
    elif do == "XXXX":
        cM = cM + 1000
    inv = open("items.txt", 'w')
    inv.truncate(0)
    inv.close()
    money = open("money.txt", 'w')
    money.truncate(0)
    money.close()
    boxInv = open("box.txt", 'w')
    boxInv.truncate(0)
    boxInv.close()
    #I know it is not pratcital...
    index = 0
    with open("items.txt", 'w') as inv:
        for item in inventory:
            inv.write(inventory[index])
            index = index + 1
    inv.close()
    money = open("money.txt", 'w')
    money.write(str(cM))
    index = 0
    with open("box.txt", 'w') as boxInv:
        for item in inventory:
            boxInv.write(box[index])
            index = index + 1
    boxInv.close()
