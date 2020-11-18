import os

def resize_video(filename, width, height):
    out_name = str(width) + "_" + str(height) "_" + filename
    os.system("ffmpeg -i {} -vf scale={}:{} {}".format(filename, width, height, out_name))
