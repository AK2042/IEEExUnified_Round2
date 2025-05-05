#Ayyy, 2nd Moderate code!!
#This time, it can be a bit tricky..., to solve this, you need to observe carefully.
#Do you want a hint? its pretty simple, its just the way you join(Zip)... ;)

from Hidden.vault import mod2a, mod2b, decoder

###########################
def combine(a, b):
    return "".join(a + b)
###########################

clue = combine(mod2a, mod2b)
print("Clue:", decoder(clue))