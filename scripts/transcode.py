import os

def transcode_video(filename):
    # transcode to mpg
    os.system("ffmpeg -i {} {}.mpg".format(filename, filename.split('.')[0]))
