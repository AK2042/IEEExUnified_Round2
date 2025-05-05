/*
In the given code,
    A simple "reverseing a string" code is given.
    You are supposed to debug the given code logic and print the reversed string.
    This will reveal the clue in reverse.
    only parts between //#######################################
    are editable.
*/ 
/*
Hint: Only two changes are to be made.
*/

#include <stdio.h>
#include "Hidden/easy1.h"

int main() {
    int reversed[LEN];
//##################################################################
    for (int i = 0; i < LEN; i++) {
        reversed[i] = CLUE[LEN - i];
    }
//##################################################################

    char clue[LEN + 1];
    decode(clue, reversed);

    printf("Clue: %s\n", clue);
    return 0;
}
