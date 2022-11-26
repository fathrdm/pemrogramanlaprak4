#include <stdio.h>
int main (){
      int angka, a, i;
      scanf("%d %c", &angka, &a);
      for(i = 1; i <= 50; i++){
            if(i % angka == 0){
                  printf("%c ", a);
            }
            else{
                  printf("%d ", i);
            }
      }
}