#include <fcntl.h>
#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <unistd.h>
#include <sys/time.h>
#include <time.h>

int main(int argc, char **argv) {
  system("echo foodbutton.c starting");
  FILE *hidrawptr;
  int c;
  //struct timeval last;
  time_t last, current;
  time(&last);
  hidrawptr = fopen("/dev/hidraw0", "r");
  if (!hidrawptr) {
    printf("unable to open the file");
  }

  while (1) {
    c = fgetc(hidrawptr);
    //time(&current);
    time(&current);
    if(c) {
      if (difftime(current, last) >= 10.00) {
        time(&last);
        system("echo button pressed >> /home/pi/Desktop/freefood/log.txt");
        system("sudo python /home/pi/Desktop/freefood/foodButton_edit.py &");
      }
      else {
      	system("echo email already sent less than 10 seconds ago >> /home/pi/Desktop/freefood/log.txt");
      }
    }
  }
  return 0;
}
