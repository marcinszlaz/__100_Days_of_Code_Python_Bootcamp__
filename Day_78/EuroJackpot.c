//in C this is much faster (around 20-25 times faster)
#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#include <stdbool.h>

// Is there digit in array?
bool contains(int *arr, int size, int val) {
    for (int i = 0; i < size; i++) if (arr[i] == val) return true;
    return false;
}

// generating unique digits
void generate_random(int *arr, int size, int max) {
    int i = 0;
    while (i < size) {
        int r = (rand() % max) + 1;
        if (!contains(arr, i, r)) {
            arr[i++] = r;
        }
    }
}

// arrays diff (C doesn't have == for arrays)
bool compare(int *a, int *b, int size) {
    for (int i = 0; i < size; i++) {
        if (!contains(a, size, b[i])) return false;
    }
    return true;
}

int main() {
    srand(time(NULL));
    int win_five[5], win_two[2];
    int guess_five[5], guess_two[2];
    long long attempts = 0;

    generate_random(win_five, 5, 50);
    generate_random(win_two, 2, 12);

    printf("Searching: [%d, %d, %d, %d, %d] [%d, %d]\n",
            win_five[0], win_five[1], win_five[2], win_five[3], win_five[4],
            win_two[0], win_two[1]);

    clock_t start = clock();

    while (1) {
        attempts++;
        generate_random(guess_five, 5, 50);
        generate_random(guess_two, 2, 12);

        if (compare(win_five, guess_five, 5) && compare(win_two, guess_two, 2)) {
            clock_t stop = clock();
            printf("WON! Attempt: %lld\n", attempts);
            printf("Time: %.3f s\n", (double)(stop - start) / CLOCKS_PER_SEC);
            break;
        }
    }

    return 0;
}
