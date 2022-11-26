#include <stdio.h>
int main (){
      int angka1, angka2, i;
      int a = 0;
      scanf("%d %d", &angka1, &angka2);
      if (angka1 > angka2){
            for (i = angka1; i>= angka2; i--){
                  if (i == angka1){}
                  else {
                        printf(" - ");
                  }
                  printf("%d %d", i, angka2 + a); a++;
            }
      }
      else {
            for (i = angka1; i <= angka2; i++){
                  if (i == angka1){}
                  else {
                        printf(" - ");
                  }
                     printf("%d %d", i, angka1 + angka2 - i);
            }
      }
}