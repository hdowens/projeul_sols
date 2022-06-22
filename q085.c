#include <stdio.h>
#include <stdlib.h>

int rect_count(int a, int b){
    return ((a * (a + 1) * b * (b + 1) )) / 4;
}

int main(){
    int lmin = 10000;
    int n1 = 0; 
    int n2 = 0;

    for (int i = 2 ; i < 100 ; i++){
        for(int j = 3 ; j < 100 ; j++){
             int temp = abs(2000000 - rect_count(i, j));
             if(temp < lmin){
                lmin = temp;
                n1 = i;
                n2 = j;
             }
        }
    }

    printf("The result is -> %d\tformed from these two values %d x %d\t with a min difference of %d\n", n1 * n2, n1, n2, lmin);
    return 0;
}
/*

gcc q085.c -o q85
time ./q85

The result is -> 2772   formed from these two values 36 x 77     with a min difference of 2

real    0m0.004s
user    0m0.001s
sys     0m0.000s

*/
