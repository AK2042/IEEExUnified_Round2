#In the given code,
#The program is supposed to return the a location as a clue
#Enjoy your time debugging to find the location (PS, its verry easy)
#Hint: No hint for this question, just try it out!
#you can only edit in the given area

from Hidden.vault import easy4,decoder

def clue():
    ################################################################
    jumbled = ''.join([easy2[i] for i in range(len(easy2)-1, -1,-1)])
    return jumbled[2::-1]
    ################################################################

print("Clue:", decoder(clue()))