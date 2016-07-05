import signal
import time
import freeFoodUtils_edit

global rmTimer, picTimer	

def signal_handler(signal, frame):
	global picTimer, rmTimer
	picTimer.cancel()
	rmTimer.cancel()
	sys.exit(0)

rmTimer = freeFoodUtils_edit.removeOldPicturesLoop()

picTimer = freeFoodUtils_edit.takePictureLoop()



signal.signal(signal.SIGINT, signal_handler)

while(1):
	time.sleep(0.1)
