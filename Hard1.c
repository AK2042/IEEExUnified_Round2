/*
Welcome to the Hard series!!
You have to find the key to open the door.
jk, its just some random errors here and there...,
Im sure it'll be easy for you, after all, you've already come till here.
Dont give up now!
*/
#include <stdio.h>
#include "Hidden/hard1.h"

void reveal(char* out, const int enc) {
    for (int i = 0; i <= LEN; i++) {  
        out[i] = enc[i] + KEY;  
    }
}

int main() {
    char clue[LEN + 1];
    reveal(clue, CLUE);
    printf("Clue: %s\n", clue)
    return 0;
}
