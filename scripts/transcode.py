import os

def transcode_video(filename):
    os.system("ffmpeg -i {} {}.mpg".format(filename, filename.split('.')[0]))
