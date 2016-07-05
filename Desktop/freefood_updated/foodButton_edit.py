import os
import time
import sys
import freeFoodUtils_edit

os.system("echo '%s button pressed' >> /home/pi/Desktop/freefood/log.txt" %time.strftime("%a, %d %b %Y %H:%M%S", time.gmtime()))

freeFoodUtils_edit.removeOldPictures()
path=freeFoodUtils_edit.takepicture()
print "Picture path is = %s" %path
freeFoodUtils_edit.sendEmail(path)	
