#include <stdio.h>
#include <math.h>


int main(){

    long long lim = 600851475143;
    int max = 0;
    for(long long i = 3; i < lim; i+=2){
        if(i % lim ==0){
            if(i > max){
                max = i;
            }
        }
    }
    printf("MAX: %d\n",max);    
    return 0;
}
