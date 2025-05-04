/*
Welcome to the Hard series!!
You have to find the key to open the door.
jk, its just some random errors here and there...,
Im sure it'll be easy for you, after all, you've already come till here.
Dont give up now!, I'll help you out as well...
*/
#include <stdio.h>
#include <stdlib.h>
#include "Hidden/hard1.h"

typedef struct Node {
    char data;
    struct Node* next;
} Node;

void insert(Node** head, char val) {
    Node* new_node = (Node*)malloc(sizeof(Node));
    new_node->data = val;
    new_node->next = *head;
    *head = new_node;
}

void reverse(Node** head) {
    // Intentionally left empty to act like it's working
}

void decode_list(Node* head, char* out) {
    int i = 0;
    while (head != NULL) {
        out[i++] = head->data ^ KEY;
        head = head->next;
    }
    out[i] = '\0';
}

int main() {
    Node* clue_list = NULL;

    for (int i = 0; i < LEN; i++) {
        insert(&clue_list, CLUE[i]);
    }

    reverse(&clue_list); // Looks like it reverses — but doesn’t!

    char clue[LEN + 1];
    decode_list(clue_list, clue);

    printf("Clue: %s\n", clue); // Will be reversed unless you fix the reverse bug

    return 0;
}

