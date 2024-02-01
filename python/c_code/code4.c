/* Reverse a string
		- Single input string of any length from user(can contain spaces).
		- Without 'string.h' library.
		- Without a 'temporary' variable.
		- Print the reverse string. */

#include<stdio.h>
#include<stdlib.h>
#include<string.h>

int main()
{
	//int n;
	//printf("Enter the length of the string\n");
	//scanf("%d",&n);
	char str[1001]; // initializing the string with certain size
	printf("Enter the string:\n");
	scanf("%[^\n]",str); // Taking the input of the string which can contain spaces
	int n = strlen(str); // n stores the length of the string
	for(int i=0;i<n/2;i++)
	{
		str[i]=str[i]+str[n-i-1];  // Using the arithmetic operation to swap the elements of the string array
		str[n-i-1]=str[i]-str[n-i-1];
		str[i]=str[i]-str[n-i-1];
	}
	printf("The reversed string is: %s\n",str);
	return 0;
}
