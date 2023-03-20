#include <stdio.h>
 
int main() {
 
    double n = 3.14159;
    double R;
    
    scanf("%lf", &R);
    
    double quad = (R*R);
    double A = n * quad;
    
    printf("A=%.4lf\n", A);
    
    return 0;
}