#include <stdio.h>
int main(){
    int i, j, a, b, y1 = 0, y2 = 0, y3 = 0;
    scanf("%d %d", &a, &b);
    for(i = 0; i < a; i++){
        for(j = i; j >= 0; j--){
            printf("(%d * %d)", j + 1, b);
            if (j > 0){
                printf(" + ");}}
    y1=(i + 1) * b;
    y2 = y2 + y1;
    printf(" = %d \n", y2);
    y3 = y3 + y2;}
    printf("%d", y3);
}
