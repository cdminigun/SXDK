#include <string.h>
#include <stdlib.h>
#include <stdio.h>

int main(){
	char toBeOverflown[3] = "ls";
	char overflow[5];

	gets(overflow);
	printf("overflow: %s", overflow);
	
	
	system(toBeOverflown);
}
