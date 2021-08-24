print("1. Reset all spaces in the car park")
print("2. Park a car")
print("3. Remove a car")
print("4. Display the car park grid")
print("5. Quit/n")
option = 0
x = int(0)
y = int(0)
parking_xy = 0
parking = list(range(60))
parking.clear()
for x in range(0,60):
    parking.append(("empty"))
num = 0
def reset(num):
    parking.clear()
    for x in range(0,60):
        parking.append(("empty"))
def park(parking,parking_xy):
    registration = str(input("enter registration "))
    parking.remove(("empty"))
    xy = str(parking_xy)
    lengh = len(xy)
    if lengh > 1:
        x = xy[1]
        y = xy[0]
    else:
        x = xy[0]
        y = ("0")
    parked = (("lisence plate ")+ registration +(" parked at row ")+ x +(" column ") + y)
    parking.insert(parking_xy,parked)
    int(parking_xy)
def remove(parking):
    registration = str(input("enter the registartion you wish to remove "))
    x = str(input("enter the row it is in "))
    y = str(input("enter the column it is in "))
    remove = (("lisence plate ")+ registration +(" parked at row ")+ x +(" column ") + y)
    if remove in parking:
        delete = parking.index(remove)
        parking.pop(delete)
        parking.insert(delete,("empty"))
    else:
        print("invalid choice- please re-enter")
while option != ("5"):
    option = str(input("enter number "))
    if option == ("1"):
        reset(num)
    elif option == ("2"):
        park(parking,parking_xy)
        parking_xy = parking_xy + 1
    elif option == ("3"):
        remove(parking)
    elif option == ("4"):
        print(parking)
    else:
        if option != ("5"):
            option = ("Invalid choice- please re-enter")
            print(option)
        else:
            print("Goodbye")


