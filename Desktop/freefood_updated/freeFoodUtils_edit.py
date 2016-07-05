import os
import time
import sys
import threading

global email, intervalPicture, intervalRemove, emailContent, picturesPath

file = open("/home/pi/Desktop/freefood/settings.txt").readlines()
#print file
email = ""
intervalPicture = ""
intervalRemove = ""
for x in file:
	param = x.split("=")[0]
	setting = x.split("=")[1][:-1]
	if param == "email":
		email = setting
	elif param == "intervalPicture":
		intervalPicture = setting
	elif param == "intervalRemove":
		intervalRemove = setting
	elif param == "emailContent":
		emailContent = setting
	elif param == "picturesPath":
		picturesPath = setting
text="welcome to DGP"

def takepicture():
	global picturesPath
        pic =picturesPath + str(time.time())
	os.system("echo '%s taking a picture' >> /home/pi/Desktop/freefood/log.txt" %time.strftime("%a, %d %b %Y %H:%M:%S", time.gmtime()))
	os.system("sudo fswebcam -r 640x480 -q --no-banner --no-timestamp %s.jpeg" %(pic))
	return pic
	
def removeOldPictures():
	global picturesPath
	os.system("echo '%s removing pictures' >> /home/pi/Desktop/freefood/log.txt" %time.strftime("%a, %d %b %Y %H:%M:%S", time.gmtime()))
	os.system("sudo rm %s*" %picturesPath)

def sendEmail(pic):
	global email
	print "picture path= %s" %pic 
	os.system("echo '%s sending email' >> /home/pi/Desktop/freefood/log.txt" %time.strftime("%a, %d %b %Y %H:%M:%S", time.gmtime()))
	os.system("(cat test.txt; uuencode %s.jpeg Food-Picture.jpeg)  | mail -s 'FreeFood' %s" %(pic, email))
	
def takePictureLoop():
	global intervalPicture
	val=takepicture()
	picTimer = threading.Timer(int(intervalPicture), takePictureLoop)
	picTimer.start()
	return picTimer

def removeOldPicturesLoop():
	global intervalRemove
	removeOldPictures()
	rmTimer = threading.Timer(int(intervalRemove), removeOldPictures)
	rmTimer.start()
	return rmTimer


