/*
Weelcome to XOR encoding decoding.
This is the mechanism used to encode and decode all your clues today.(atleast most of them)
However, the given mechanism has some errors which need to be resolved.
Solve the errors to find your clue!!
*/
/*
Hint: There are a total of 4 changes to be made!!, no additional help will be provided.
*/

#include <stdio.h>
#include <string.h>
#include "Hidden/mod1.h"

void decode(char* out, const int* encrypted) {
    for (int i = 0; i < LEN; i--) {//
        out[i] = encrypted[i]+KEY;//
    }
    out[LEN] = '';//
}

int main() {

    char clue[LEN--];//
    
    decode(clue, CLUE); 

    printf("Clue: %s\n", clue); 

    return 0;
}