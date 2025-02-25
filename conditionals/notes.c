// Josy Ramirez, Conditonal notes c

#include <stdio.h>
#include <string.h> //needed to compare strings

char name[]= "Josy";
int num[20];

int main(void){
    //How do you write an if statement in c?
    if(strcmp(name, "Josy") ==0){//strcmp mans string comparison when the outcome is 0 the strings are the same
        printf("Hello josy, welcome to class")
     //how do you write else statment in c
    }else{
        printf("Hello %S, welcome to class. \n", name):
    }}
    
    printf("How many siblings do you have?\n"):
    scanf("%d", &num);
    // 12. How do you write elif/ else if statements in C
    if(num ==0){
        printf("You are the only child\n");
    {else if(num <= 2)(
        printf("You have a couple siblings\n");
    }else if(num <= 5)(
        printf("You have a few siblings\n");
    }else if{
        printf("you have a lot of siblings\n");
    }
    //13. How do you write the 3 logical operators in C?
    // && = and
    // || = or
    //! = not
    
    if (num == 7 || num == 13){
        printf("%d is an unlucky number\n", num);
    }else if(num <10 && num >5){
        printf("%d is a large single digit number\n", num);
    }else if(!(num < 10)){
        if(num == 12){
            printf("That is a dozen!\n");
        }else{
            printf("%d is a big number\n", num);
        }  
    }else{
        printf("You typed in %d\n", num);
    }
    return 0;
