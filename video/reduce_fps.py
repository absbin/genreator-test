import cv2
video = cv2.VideoCapture('totoro3.avi')

frame_width = int(video.get(3))
frame_height = int(video.get(4))
out = cv2.VideoWriter('totoro2.avi',cv2.VideoWriter_fourcc('M','J','P','G'),5, (frame_width,frame_height))
#out = cv2.VideoWriter('outpy.avi', cv2.VideoWriter_fourcc(*'PIM1'),10,(frame_width,frame_height))
success,image = video.read()
count = 0
while success:		
	print('Read a new frame: ', success)
	#cv2.imwrite("frame%d.jpg" % count, image)     # save frame as JPEG file      
	success, image = video.read()
	X=5
	if count%X==0:#keep one of X frmes
		out.write(image)
	count += 1
video.release()