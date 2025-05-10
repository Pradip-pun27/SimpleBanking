#include<graphics.h> //For using graphics related functions like initgraph
#include <conio.h> //For using the getch function 
#include<dos.h> //For controlling the speed of formation of new circle(to show Animation simple)
int main(){
	int gmode=DETECT,gdriver; // gmode and gdriver are simply normal variable and DETECT is a predefined word
	int i;
	initgraph(&gmode,&gdriver,(char*)""); //3rd Parameter is for auto detection of file path (directory)
	for(i=5;i<=240;i+=10){
		circle(300,240,i); // Circle with center's coordinate(300,240) and radius of i(Radius starts with 5, increases by 10 till 240
		delay(100); // For making delay in the new circle's fomation (time in miliseconds)
	}
	getch(); // For catching the screen(avoiding the blinking or vanishing  of a screen(console)) defined under conio.h header file
	closegraph(); // For closing the graphics mode after finishing of program
	return 0;
}
