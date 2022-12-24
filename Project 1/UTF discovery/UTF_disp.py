with open("UTF_ALL.txt", "w") as f:
    try:
        for i in range (100000):
            if  (i < 55296 or i > 57343): #and not (i > 55296):
                print(chr(i), end = " , ")
                f.write(f"{chr(i)}   ")
    except Exception as e:
        print(e)
        pass
