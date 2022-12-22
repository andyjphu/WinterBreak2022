with open("UTF_ALL.txt", "w") as f:
    try:
        for i in range (69420):
            print(chr(i), end = " , ")
            f.write(f"{chr(i)}   ")
    except Exception as e:
        pass
