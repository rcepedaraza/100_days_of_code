print(
'''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/______/_
*******************************************************************************
''')

print("Welcome to Treasure Island")
print("Your mission is to find the treasure.")
print("You 're at a cross road.\nWhere would you like to go?")
left_right = input("'left' or 'right'? ").lower()
if left_right == "left":
    print("You come to a lake.\nThere is an island in the middle of the lake.\nWould you like to wait for a boat or swim across?")
    swim_wait = input("'swim' or 'wait? ").lower()
    if swim_wait == "wait":
        print("You arrive at the island unharmed.\nThere is a house with 2 doors.\nOne red, one yellow, and one blue.\nWhich color do you choose?")
        red_yellow_blue = input("'red', 'yellow', 'blue'? ").lower()
        if red_yellow_blue == "red":
            print("Game Over.")
        elif red_yellow_blue == "blue":
            print("Game Over.")
        elif red_yellow_blue == "yellow":
            print("You Win!")
        else:
            print("Wron selection! Game Over.")
    elif swim_wait == "swim":
        print("Game Over.")
        
elif left_right == "right":
    print("You fell into a hole. Game Over.")
else:
    exit()
