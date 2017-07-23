import sys



import os
folder = 'videoFrames7'  

os.mkdir(folder)
# use opencv to do the job
sys.path.append('/usr/local/lib/python2.7/site-packages')
import cv2
print(cv2.__version__)  # my version is 3.1.0
vidcap = cv2.VideoCapture('recipeVideo.mp4')
vidcap.set(0,2000)
count = 0
inc = 100000
while True:
	count +=1
	success,image = vidcap.read()
	if not success:
	    break
	if (count%100)==0:
		cv2.imwrite(os.path.join(folder,"frame{:d}.jpg".format(count)), image)     # save frame as JPEG file
print("{} images are extacted in {}.".format(count,folder))