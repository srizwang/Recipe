import sys

import os

# use opencv to do the job
sys.path.append('/usr/local/lib/python2.7/site-packages')
import cv2
print(cv2.__version__)  # my version is 3.1.0
vidcap = cv2.VideoCapture('lasagna.mp4')
count = 0
inc = 100000
while True:
	count +=1
	success,image = vidcap.read()
	if not success:
	    break
	if (count%50)==0:
		cv2.imwrite(os.path.join('lasagna',"frame{:d}.jpg".format(count)), image)     # save frame as JPEG file
#print("{} images are extacted in {}.".format(count,folder))