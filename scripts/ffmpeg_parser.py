import os
import subprocess

def parse_input_file(file_dir, filename):
    proc = os.popen("ffmpeg -i {}".format(filename)).read()
