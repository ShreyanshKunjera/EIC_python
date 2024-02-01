//add any number to any location in array , delete any number from given array

#include <stdio.h>
#include <stdlib.h>

int main() {
    int capacity;
    printf("enter the size of the array that you want\n");
    scanf("%d",&capacity);

    int n;
    printf("enter the initial number of elements you want to add in the array\n");
    scanf("%d",&n);

	if(n>capacity)
	{
		printf("You can't add more numbers than capacity, please select the number less than the size of an array\n");
	}

    int arr[capacity]; // creating an array of size of given capacity

    printf("Enter the elements:\n");
    for(int i=0;i<n;i++)   // Take input of elements
    {
        scanf("%d",&arr[i]);
    }

    int lastele=n; // Tracking the last element's location
    int choice;    // variable which decide which operation we need to do, add or delete.

    printf("If you want to add a number, select 1 and if you want to delete an element, select 2\n");
    scanf("%d",&choice);

    int add_loc,del_loc,ele_to_add; // initializing the variables to store the adding location, deleting location and the element that want to add.
    if(choice==1)
    {
        if(n==capacity)  // Checking if array is already full or not, if yes then we can't add any additional number
        {
            printf("The array is full\n");
        }
        else
        {
            printf("Enter the location at which you want to add a number\n");
            scanf("%d",&add_loc);
            printf("Enter the element that you want to add\n");
            scanf("%d",&ele_to_add);
            for(int i=capacity-1;i>=add_loc;i--) // Shifting the elements to the right side so that we can add the number to given location.
            {
                arr[i+1]=arr[i];
            }
            arr[add_loc]=ele_to_add;
            n++;
        }
    }
    
    if(choice==2)
    {
	if(n==0)
	{
		printf("The array is already empty\n");
	}
	else
	{
        printf("Enter the location at where you want to delete the element\n");
        scanf("%d",&del_loc);
        for(int i=del_loc-1;i<n;i++) // shifting the elements to the left side so that there will be no space inbetween after deleting the element
        {
            arr[i]=arr[i+1];
        }
        arr[n]=0; // making the last element as o which shows there is no element at that location
        n--; // pointing to the last element in array
	}
    }
    
	printf("The updated array is:\n");
    for(int i=0;i<n;i++)
{
	printf("%d ",arr[i]);
}
		
    return 0;
}
