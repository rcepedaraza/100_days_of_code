import random

names_string = "Ricardo, Eva, Ana, Martha, Mike, Joseph"
names = names_string.split(", ")
# The code above converts the input into an array seperating
#each name in the input by a comma and space.
# 🚨 Don't change the code above 👆
random_name_index = random.randint(0, len(names) - 1)
print(f"{names[random_name_index]} is going to buy the meal today!")