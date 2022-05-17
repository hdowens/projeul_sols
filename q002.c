#include <stdio.h>

int main(){
    int first = 1;
    int second = 2;
    int sum = 2;
    printf("%d,%d,",first,second);
    while(second < 4000000){
        int new = first + second;
        if(new % 2 == 0){
            sum = sum + new;
        }
        printf("%d,",new);
        first = second;
        second = new;
    }
    printf("TOTAL: %d\n",sum);
    return 0;
}
