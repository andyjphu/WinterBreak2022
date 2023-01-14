with open("d.txt") as f:
    for line in f:
        print(chr(int(line)), end="")