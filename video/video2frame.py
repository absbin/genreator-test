import cv2
import glob
#vidcap = cv2.VideoCapture('*.avi')

vidcap = cv2.VideoCapture(glob.glob('*.avi')[0])
#vidcap = cv2.VideoCapture('totoro2.avi')

success,image = vidcap.read()
count = 1
while success:
  cv2.imwrite("frame%d.jpg" % count, image)     # save frame as JPEG file      
  print('Read a new frame: %d'%count , success)
  success,image = vidcap.read()

  count += 1