#!/bin/sh
sleep 5;
echo 'starting freefood_edit';
(sudo python /home/pi/Desktop/freefood/freefood_edit.py& sudo /home/pi/Desktop/freefood/food_edit)&
