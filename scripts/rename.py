import os

def rename_file(input_name, output_name):
    # rename file...
    os.rename(input_name, output_name+'.mp4')
