/*
In the given code, no changes are actually required, 
just decode the given ascii output.
Enjoy Ascii hunting guys!!!
*/
/*
Hint: Btw, 32 is the ascii value of the space character,
*/

#include <stdio.h>
#include "Hidden/easy3.h"

int main() {
    int clue[] = CLUE;

    printf("Clue: ");
    for (int i = 0; i < LENGTH; i++) {
        printf("%d", clue[i]);
        if (i < LENGTH - 1) {
            printf(", ");
        }
    }
    printf("\n(For more hints, look around...)");

    return 0;
}
