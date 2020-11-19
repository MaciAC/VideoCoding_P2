import os

def resize_input(filename, width, height):
    out_name = str(width) + "_" + str(height) + "_" + filename
    os.system("ffmpeg -i {} -vf scale={}:{},setsar=1:1 {}".format(filename, width, height, out_name))
