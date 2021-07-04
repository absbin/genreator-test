from moviepy.video.io.ffmpeg_tools import ffmpeg_extract_subclip
import os
import glob

cwd = os.getcwd()
t1=01:00:00
t2=01:00:05
file_name=glob.glob('*.avi')
fp = open(file_name[0])

ffmpeg_extract_subclip(fp.name, t1, t2, targetname="video {}-{}.avi".format(t1,t2))



