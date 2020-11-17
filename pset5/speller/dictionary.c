// Implements a dictionary's functionality

#include <stdbool.h>
#include "dictionary.h"
#include <stdio.h>
#include <string.h>
#include <math.h>
#include <stdlib.h>
#include <ctype.h>
#include <stdint.h>
#include <strings.h>

// Represents a node in a hash table
typedef struct node
{
    char word[LENGTH + 1];
    struct node *next;
} node;

// Number of buckets in hash table
const unsigned int N = 1e4 + 9;

// Hash table
node *table[N];

// successful load counter
int loadCount = 0;

// Returns true if word is in dictionary else false
bool check(const char *word)
{
    unsigned int index = hash(word);

    if (index < N && index >= 0)
    {
        node *tmp = table[index];

        while (tmp != NULL)
        {
            if (strcasecmp(tmp->word, word) == 0)
            {
                return true;
            }

            tmp = tmp->next;
        }

        return false;
    }

    return false;
}

// Hashes word to a number
// Found here: https://cp-algorithms.com/string/string-hashing.html
unsigned int hash(const char *word)
{
    const int p = 23;
    const int mod = 1e4 + 9;
    unsigned int hashValue = 0;
    long long p_pow = 1;
    for (int i = 0; i < strlen(word); i++)
    {
        char c = tolower(word[i]);
        hashValue = (hashValue + (c - 'a' + 1) * p_pow) % mod;
        p_pow = (p_pow * p) % mod;
    }

    return hashValue;
}

// Loads dictionary into memory, returning true if successful else false
bool load(const char *dictionary)
{

    // open the dictionary file
    FILE *dictPtr = fopen(dictionary, "r");

    if (dictPtr == NULL)
    {
        fclose(dictPtr);
        return false;
    }
    else
    {
        // allocate enough memory for even the longest word
        char wordBuffer[LENGTH + 1];

        // load words, one at a time, into buffer using %s
        while (fscanf(dictPtr, "%s", wordBuffer) != EOF)
        {
            // get the index of the dictionary word in Buffer
            unsigned int index = hash(wordBuffer);

            // malloc heap memory for size of a node, n
            node *n = malloc(sizeof(node));

            if (n == NULL)
            {
                fclose(dictPtr);
                return false;
            }
            else
            {

                // strcpy word into the n->word attribute from buffer.
                strcpy(n->word, wordBuffer);

                // if the head of the list is NULL;
                if (table[index] == NULL)
                {
                    // set the head of list to point to n
                    table[index] = n;
                    // set the pointer of n to be NULL since its the last item on the list
                    n->next = NULL;
                    printf("new node\n");
                    loadCount++;
                }
                // the list already exists
                else
                {
                    // init temp pointer to point to the current first node in the list
                    node *tmp = table[index];
                    // set the pointer of the new node (n->next) equal to what tmp is pointing at, which is what the head is poining at, which is the original first node.
                    n->next = tmp;
                    // set the head of the list to point to the new node, n.
                    table[index] = n;
                    printf("added node\n");
                    loadCount++;
                }
            }
        }
        fclose(dictPtr);
        return true;
    }
}

// Returns number of words in dictionary if loaded else 0 if not yet loaded
unsigned int size(void)
{
    return loadCount;
}

// Unloads dictionary from memory, returning true if successful else false
bool unload(void)
{
    for (int i = 0; i < N; i++)
    {
        if (table[i] == NULL)
        {
            free(table[i]);
        }
        else
        {
            node *tmp = table[i];
            node *cursor = table[i]->next;

            while (cursor != NULL)
            {
                free(tmp);
                tmp = cursor;
                cursor = cursor->next;
            }

            free(tmp);
        }
    }
    return true;
}
