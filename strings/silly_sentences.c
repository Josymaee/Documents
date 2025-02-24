# Joslynn Ramirez, Silly sentences c

#include <stdio.h>

int main(void){
char animal[20];
char place[20];
char verb[20];
char sentence[400]= "The ";
        
printf("Name an animal: ");
scanf("%s", animal);
printf("Name a place: ");
scanf("%s", place);
printf("Name a past tense verb: ");
scanf("%s", verb);
strcat(sentence, animal);
strcat(sentence, " went to the ");
strcat(sentence, place);
strcat(sentence, " and ");
strcat(sentence, verb);
strcat(sentence, " with his friend the mean dog. \n");
    printf("%s", sentence);
    return 0;
<<<<<<< HEAD
}
=======
}
>>>>>>> 022b2abba70bf4a2bbd8650d4c99b7c9649dc1fe
