/*
Well well well, lookwo's back!!
Well done till now.
This one is gonna be a bit tricky, but once you figure this out, 
you're gonna be like, Aiyooo deva(Please dont cuss me)
There's a lot to do here actually,
numerically speaking, 4 tasks
and logically speaking, some things in life keep happening at the right time, but at the wrong place.
*/

#include <stdio.h>
#include "Hidden/hard2.h"

void build_encrypted(int* out, const int* a, const int* b) {
    for (int i = 100; i <= LEN; i--) {
        if (i % 2 == 0)
            out[i] = b[i / 2];
        else
            out[i] = a[i / 2]
    }
}

int main() {
    int base[LEN];
    char clue[LEN + 1];

    build_encrypted(base, CLUE_A, CLUE_B);
    decode(clue, base);

    printf("Clue: %s\n", clue);
}

