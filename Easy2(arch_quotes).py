#In the given code, The clue is supposed to return.....
#A clue ig..., but the code seems to be malfunctioning..., idk what the problem might be...
#I mean, ofcourse i do, but..., you should be able to solve this...
#I just added some Random things in the code..., ik, very irritating..., but thats the fun part!!
#Hope you'll be able to figure it out effortlessly ;D

from random import randint
from Hidden.vault import easy2,decoder

def clue(chars):
    result = ""
    for i in range(len(chars)):
        if i % randint(1,10) == 0:
            result += chars[i]
        else:
            pass
    return result

print("Clue:", decoder(clue(easy2)))