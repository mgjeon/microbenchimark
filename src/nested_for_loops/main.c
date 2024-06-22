#include <stdio.h>

int main() {
    int n, i, j;
    double result;
    
    n = 100000;
    result = 0.0;

    for (i = 1; i <= n; i++) {
        for (j = 1; j <= n; j++) {
            result += 0.00001;
        }
    }

    printf("Result: %f", result);
    return 0;
}