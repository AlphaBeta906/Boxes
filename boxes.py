#Boxes
from random import *
from time import *
inventory = []
boxes = []
cM = 0
common = ["Rock", "Iron", "Wood", "Pistol", "Spear", "Arrow & Bow", "Plastic Shard", "Water Bottle"]
c2 = ["Shotgun", "Gold", "Average PC", "MS-DOS", "Knuclers", "Car Engine"]
c3 = ["Automated Shotgun", "Laptop", "Medicine", "Map of the World", "Golf Cart"]
c4 = ["Pack of Bullets", "Average Tent", "Laptop+", "Money Bag", "Credit Card"]
inv = open("items.txt", 'r')
money = open("money.txt", 'r')
boxInv = open("box.txt", 'r')
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
    print ("What to do? (Buy, Unbox, Inv, Craft)")
    do = input("> ").upper()
    if do == "BUY":
        print ("C Box - 10")
        print ("C2 Box - 30")
        print ("C3 Box - 90")
        print ("C4 Box - 120")
        do = input("> ").upper()
        if do == "C BOX":
            if cM > 10:
                boxes.append("C Box")
                cM -= 10
                print ("Bought a C Box")
            else:
                print ("Too poor lad")
        elif do == "C2 BOX":
            if cM > 30:
                boxes.append("C2 Box")
                cM -= 30
                print ("Bought a C2 Box")
            else:
                print ("Too poor lad")
        elif do == "C3 BOX":
            if cM > 90:
                boxes.append("C3 Box")
                cM -= 90
                print ("Bought a C3 Box")
            else:
                print ("Too poor lad")
        elif do == "C4 BOX":
            if cM > 90:
                boxes.append("C4 Box")
                cM -= 130
                print ("Bought a C4 Box")
            else:
                print ("Too poor lad")
    elif do == "UNBOX":
        print ("What box do you want to open?")
        print (", ".join(boxes))
        do = input("> ")
        if do in boxes:
            if do == "C Box":
                thing = choice(common)
                inventory.append(thing)
                boxes.remove("C Box")
                print ("You got one " + thing)
            elif do == "C2 Box":
                thing = choice(c2)
                inventory.append(thing)
                boxes.remove("C2 Box")
                print ("You got one " + thing)
            elif do == "C3 Box":
                thing = choice(c3)
                inventory.append(thing)
                boxes.remove("C3 Box")
                print ("You got one " + thing)
            elif do == "C4 Box":
                thing = choice(c4)
                inventory.append(thing)
                boxes.remove("C4 Box")
                print ("You got one " + thing)
    elif do == "INV":
        print ("Inventory: " + ", ".join(inventory))
        print ("Boxes: " + ", ".join(boxes))
    elif do == "CRAFT":
        item1 = input("Item 1: ").upper()
        item2 = input("Item 2: ").upper()
        if (item1 == "IRON" and item2 == "CAR ENGINE") or (item1 == "CAR ENGINE" and item2 == "IRON"):
            inventory.remove("Iron")
            inventory.remove("Car Engine")
            inventory.append("Golf Cart")
            print ("You made a Golf Cart!")
    elif do == "XXXX":
        cM = cM + 1000
        print ("1000 money recived")
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
    if len(inventory) == 0:
        index = 0
        with open("items.txt", 'w') as inv:
            for item in inventory:
                inv.write(inventory[index])
                index = index + 1
        inv.close()
    money = open("money.txt", 'w')
    money.write(str(cM))
    if len(boxes) == 0:
        inde = 0
        with open("box.txt", 'w') as boxInv:
            for box in boxes:
                boxInv.write(boxes[inde])
                inde += 1
        boxInv.close()
