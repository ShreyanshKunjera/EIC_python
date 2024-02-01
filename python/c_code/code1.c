//Find a Non Repetitive char from string - "asdfgasdfglkjhgesdsdadsa" ( this is just a sample string )

#include <stdio.h>
#include <stdlib.h>

int main() {

    int n;
    printf("Enter the size of the string\n");
    scanf("%d",&n);

    printf("Enter the string:\n");
    char str[n];
    scanf("%s",str);

    int arr[26]={0}; // created an array to store the frequency of the characters

    for(int i=0;i<n;i++)  // Calculating the frequncies of the character and storing it in the arr
    {
        arr[str[i]-'a']++; // Since array is of type int, we need to use "str[i]-'a'" to convert the character to integer
    }

    for(int i=0;i<26;i++) // find the character with 1 frequency to print them in the output
    {
        if(arr[i]==1)
        {
            printf("%c\n",i+'a');
        }
    }

    return 0;
}
