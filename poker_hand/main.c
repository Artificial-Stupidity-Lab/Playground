#include <stdio.h>
#include <stdlib.h>

int main()
{
    char hand[50];
    fgets(hand, sizeof(hand),stdin);
    printf("%s",hand);

    return 0;
}
