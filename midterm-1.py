# Author: CRS 12/14/21
import random
def clone_number():
    if question == "Y":
        while x in random.randrange(0, 10000):
            if x <= 9:
                print("Clone name: CT-000" + x)
                clone_lst.append
            elif x<= 99:
                print("Clone name: CT-00" + x)
                clone_lst.append
            elif x<= 999:
                print("Clone name: CT-0" + x)
                clone_lst.append
            elif x<= 9999:
                print("Clone name: CT-" + x)
                clone_lst.append
    elif question == "N":
        print("Your clones are: " + clone_lst)

        
question = input("Make a clone?")
x = random.randrange(0, 10000)
clone_lst = []