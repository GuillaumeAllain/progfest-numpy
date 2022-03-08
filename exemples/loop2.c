#include <stdio.h>

int main()

{
    int num, count, sum = 0;

    // for loop terminates when num is less than count
    for(count = 1; count <= 100; ++count)
    {
        if (count<=50){
            sum += count;
        }
    }

    printf("Sum = %d\n", sum);

    return 0;
}
