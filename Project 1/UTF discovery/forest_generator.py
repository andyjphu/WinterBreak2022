import random
with open("test_UTF_terrain.txt","w") as f:
    for i in range (10):
        for i in range(10):
                f.write(random.choice((" ", "𓋇")))
        f.write("\n")