#Well, this is the last question...
#I hope you're ready for it...
#This is a simple Queue problem, with some minor errors...
#There's mainly 2 changes to be made, thats it
#So, good luck...
#You know what, the changes are to be made in the given lines
#14-17, 26, go on, have fun!!
from collections import deque
from Hidden.vault import tiebreaker2

def decrypt(encoded):
    out = ""
    for num in encoded:
        if num % 2 == 0:
            char = chr(num ^ 35)
        else:
           continue
        out += char
    return out

def rebuild_queue(s):
    q = deque()
    word = ""
    for ch in s:
        if ch == ' ':
            q.append(word[::-1])
            word = ""
        else:
            word += ch
    q.append(word[::-1])
    return q

def restore_clue(q):
    if not q:
        return ""
    w = q.popleft()
    return w + " " + restore_clue(q)

clue = decrypt(tiebreaker2)
queue = rebuild_queue(clue)
final = restore_clue(queue)

print("Clue:", final.strip())
