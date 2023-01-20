import os

for f in os.listdir("conversion_folder"):
    print (f)
    #os.system(f'ftransc -f mp3 "conversion_folder/{f}"')
    os.system(f'ftransc -r -q extreme -f mp3 "conversion_folder/{f}"')
    