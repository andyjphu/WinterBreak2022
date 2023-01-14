enc = "灩捯䍔䙻ㄶ形楴獟楮獴㌴摟潦弸弲㘶㠴挲ぽ"

flag = "PicoCTF{{ddddd}}"
#print("{lmao}")
print(flag)
#print(''.join([chr((ord(flag[i]) << 8) + ord(flag[i + 1])) for i in range(0, len(flag), 2)]))

#for index, element in enumerate(enc):
#    print((chr(ord(element)-ord()>>8))) #- ord(enc[index+1])))

'''
el1 = the ord of the first flag character, then shift 8 digits << bitwise,
then add the ord of the second flag character. Keep going until 19 len
since flag len had to be 19 + 2, flag len had to be 20 to prevent index errors

therefore each character was encoded with the next

so starting at the end of the string, we know that the 20th character was
a "}" and therefore the 19th character had to be encoded with 125 in the mix

the 19th character had to be defined as the character of:
    the ordinal of the 19th flag character shifted bitwise << 8 times and + 125


'''
def recurse(raw, ordinal_last_true):
    if raw == "":
        return 
    else:
        olt= ((ord(raw[-1]) - ordinal_last_true) >>8)
        print(olt, chr(olt))
        recurse(raw[:-1], olt)
recurse(enc, 125)