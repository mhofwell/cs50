// Implements a dictionary's functionality

#include <stdbool.h>
#include "dictionary.h"
#include <stdio.h>
#include <string.h>
#include <math.h>
#include <stdlib.h>
#include <ctype.h>
#include <stdint.h>

// Represents a node in a hash table
typedef struct node
{
    char word[LENGTH + 1];
    struct node *next;
} node;

// Number of buckets in hash table
const unsigned int N = 1;

// Hash table
node *table[N];

// Returns true if word is in dictionary else false
bool check(const char *word)
{
    // TODO
    return false;
}

// Hashes word to a number
unsigned int hash(const char *word)
{
    // TODO

    return 0;
}

// Loads dictionary into memory, returning true if successful else false
bool load(const char *dictionary)
{
    // open the dictionary file
    FILE *dictPtr = fopen(dictionary, "r");
    if (dictPtr == NULL)
    {
        return false;
    }

    // allocate enough memory for even the longest word
    char *wordBuffer = malloc(sizeof(LENGTH + 1));

    // load words into buffer, create node, hash them, place into table at correct index
    while (fscanf(dictPtr, "%s", wordBuffer) == 1)
    {

        // for each of those words, create a new node
        // malloc heap memory
        node *n = malloc(sizeof(node));

        if (n == NULL)
        {
            return 1;
        }

        // strcpy word into the node from buffer?
        strcpy(n->word, wordBuffer);

        // set the node pointer to NULL
        n->next = NULL;

        // you're going to hash the word to obtain a hash value to tell you where it goes
        unsigned int loc = hash(n->word);

        printf("%i\n", loc);
    }
    return true;
    // take each of those words (nodes) and insert them at the correct bucket
    // index into the hash table
    // go to the head of a list starting at that index
    // have a tmp variable point to where the bucket is pointing
    // point the list to the new node
    // point the new node to tmp
    //
    return false;
}

// Returns number of words in dictionary if loaded else 0 if not yet loaded
unsigned int size(void)
{
    // TODO
    return 0;
}

// Unloads dictionary from memory, returning true if successful else false
bool unload(void)
{
    // TODO
    return false;
}
