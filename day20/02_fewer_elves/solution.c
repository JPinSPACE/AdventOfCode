/* Solution to the second puzzle of Day 20 on adventofcode.com
   C is fast..
*/
#include <stdio.h>

#define TARGET 29000000

int main(int argc, char *argv[])
{
    int i;
    for (i = 0; i < TARGET; i++) {
        int presents = i * 11;

        int cand;
        for (cand = 1; cand < i / 2 + 1; cand++) {
            if (i % cand == 0) {
                if (i <= cand * 50)  {
                    presents += cand * 11;
                }
            }
        }

        if (presents >= TARGET) {
            printf("answer: %d\n", i);
            return 0;
        }
    }
    return 0;
}
