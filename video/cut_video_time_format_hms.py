#from moviepy.video.io.ffmpeg_tools import ffmpeg_extract_subclip
import os
import glob

cwd = os.getcwd()
file_name=glob.glob('*.avi')
fp = open(file_name[0])


def runBash(command):
	os.system(command)

def crop(start,end,input,output):
	str = 'ffmpeg -i ' + input + ' -ss  ' + start + ' -to ' + end + ' -c copy ' + output
	print (str)
	runBash(str)

crop('01:49:50','01:50:25',fp.name,(''.join(os.path.splitext(fp.name)[0])+'2.avi'))
