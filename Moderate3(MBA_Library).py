#Last question of the Moderate Series guys!!, good going!!, Im really proud of you!!
#Bet its been a while since you heard that, dont worry though, im really proud of you!!
#Lets get to the point now, The last moderate one, is..., yk, it'll need atleast some brains..
#Dont worry, you got this!!
#Just dont limit yourslef...;)

from Hidden.vault import mod4, decoder

def collect_clue(data):
    clue_dict = {}
    for i, ch in enumerate(data):
        clue_dict[i % 5] = ch 
    return ''.join(clue_dict[k] for k in sorted(clue_dict))

print("Clue:", decoder(collect_clue(mod4)))