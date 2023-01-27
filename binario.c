#include<stdio.h>
#include<conio.h>

int main(void){
    int number;
    printf("Ingre un numero de un digito: ");
    scanf("%d", &number);
    
    if(number > 9){
        printf("No es un numero de un dígito");
        return;
    }

    if(number == 0){
        printf("Binario de %d es 0000",number);
        return;
    }

    printf("%d", number);

    return;
}