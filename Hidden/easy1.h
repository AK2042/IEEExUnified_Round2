#ifndef EASY1_H
#define EASY1_H

#define LEN 10
#define KEY 35

static const int CLUE[LEN] = {114, 86, 66, 71, 81, 66, 77, 68, 79, 70};

void decode(char* out, const int* encrypted) {
    for (int i = 0; i < LEN; i++) {
        out[i] = encrypted[i] ^ KEY;
    }
    out[LEN] = '\0';
}

#endif