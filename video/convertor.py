import subprocess
import os
import glob

#cwd = os.getcwd()

def convert_video(video_input, video_output):
    pass
def convert_video(video_input, video_output):
    cmds = ['ffmpeg', '-i', video_input, video_output]

def convert_video(video_input, video_output):
    cmds = ['ffmpeg', '-i', video_input, video_output]
    subprocess.Popen(cmds)
	
file_name=glob.glob('*.avi')
for ii in range(len(file_name)):
	fp = open(file_name[ii])
	convert_video(fp.name,os.path.splitext(fp.name)[0]+'.mp4')