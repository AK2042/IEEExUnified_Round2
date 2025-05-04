#ifndef MOD3_H
#define MOD3_H

#define LEN  18
#define KEY  35

static const int CLUE_A[LEN/2] = {97, 64, 124, 66, 70, 116, 87, 75, 70};
static const int CLUE_B[LEN/2] = {66, 72, 100, 87, 124, 66, 64, 78, 77};

void decode(char* out, const int* encrypted) {
    for (int i = 0; i < LEN; i++) {
        out[i] = encrypted[i] ^ KEY;
    }
    out[LEN] = '\0';
}

#endif