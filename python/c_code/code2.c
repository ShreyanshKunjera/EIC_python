//String reverse using pointers

#include <stdio.h>
#include <stdlib.h>

int main() {
    int n;
    printf("enter the size of the string\n");
    scanf("%d",&n);

    char str[n];
    printf("enter the string\n");
    scanf("%s",str);
    
    // Approach 1 
    
    for(int i=0;i<n/2;i++) // Take two pointers, 1 at start and 2nd at end and then traverse the half array and each time, swap the first and last position.
    {
        char temp=str[i]; // Store the value of first element so that we can replace it with last element
        str[i]=str[n-i-1];
        str[n-i-1]=temp;
    }
    printf("%s",str);
    
    // Approach 2
    
    // char *s,*e; 
    // s=str;      //starting pointer s which address to the first character of the string
    // e=str+n-1;  // ending pointer e which address to the last character of the string
    
    // for(int i=0;i<(n-1)/2;i++)
    // {
    //     char temp=*s;
    //     *s=*e;
    //     *e=temp;
    //     s++;
    //     e--;
    // }
    // printf("%s",str);

    return 0;
}
