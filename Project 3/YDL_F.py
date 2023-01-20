import os

do_not_move = []
for l in os.listdir():
    do_not_move += l

os.system("youtube-dl --no-check-certificate -i 'https://www.youtube.com/watch?v=nSWt0CqMYDg'")

# move_list = []
# for g in os.listdir():
#     if g not in do_not_move:
#         #move_list += g
#         os.rename(g,f"conversion_folder/{g}")

'''youtube-dl -x --audio-format mp3 video_URL'''


'''
for f in os.listdir("conversion_folder"):
    print (f)
    #os.system(f'ftransc -f mp3 "conversion_folder/{f}"')
    os.system(f'ftransc -r -q extreme -f mp3 "conversion_folder/{f}"')
    
    
       '''