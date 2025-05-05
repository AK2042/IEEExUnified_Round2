#Last Easy question!!Yayy!!
#In the given code,
#I mean, youve solved this far, you might know what to do...
#But, as a friend, id like to say, dont stress it, its really easy this time as well...
#Although, it would be easier if your team were in a multiple of 3 ig...  ;)

from Hidden.vault import easy5, decoder

def clue(text):
    clue = ""
    #########################################
    for i in range(len(text)): 
        clue += text[i]
    #########################################
    return clue

print("Clue:", decoder(clue(easy5)))