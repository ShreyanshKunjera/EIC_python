/* Angle between hands of an analog clock.
		- Two inputs from use: minutes (0 - 59) and hours (0 - 11).
		- Print the (smaller) angle formed by them. */

#include<stdio.h>
#include<stdlib.h>

// There are total 60 points in the clock and between two points, the angle is 6 degree so if we know how many points are there between hour and minute, we can calculate the angle.
int main()
{
	int minute,hour; // variables to store the values of hour and minute
	printf("Enter the value of the minute\n");
	scanf("%d",&minute);
	printf("Enter the value of the hour\n");
	scanf("%d",&hour);

	int angle_1, angle_2, angle_org; // angle_1 and angle_2 will store the values of the smaller and bigger angle between given hour and minute
	angle_1 = abs((hour*5)-minute)*6; // (hour*5) will convert the hour into the minute and then subtract it with given minute will give the difference between the location of minute and hour stick. Now multiply it with 6 will give one of the bigger or smaller angle
	angle_2 = 360-angle_1; // we will subtract the angle_1 with 360 to get another angle and then we will see which angle is samller and which one is bigger
	if(angle_1<angle_2)  // To find the min(angle_1,angle_2)
	{
		angle_org=angle_1;
	}
	else
	{
		angle_org=angle_2;
	}

	printf("The small angle between given hour and minute is : %d \n",angle_org);
}
