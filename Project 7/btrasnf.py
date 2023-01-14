flag = r"picoCTF{opnbehdaunl12oj123456bedhuj}"
#original 灩捯䍔䙻ㄶ形楴獟楮獴㌴摟潦弸弲㘶㠴挲ぽ  adding 2 chars only adds 1 more charc??
         #灩捯䍔䙻潰湢敨摡畮汯樱㈳㐵㙢敤桵橽
         #灩捯䍔䙻筯灮扥桤慵湬潪扥摨番絽
print(''.join([chr((ord(flag[i]) << 8) + ord(flag[i + 1])) for i in range(0, len(flag), 2)]))