import os
import subprocess

def parse_input_file(filename):
    os.system("ffmpeg -i {} > aux.txt 2>&1".format(filename))
    with open("aux.txt",'r') as file:
        line = file.readline()
        streams = []
        while line:
            if line.startswith("    creation_time"):
                creation_time = line.split(':', 1)[-1]
            elif "bitrate" in line:
                bitrate = line.split("bitrate:")[-1]
            elif line.startswith("    Stream"):
                streams.append(line.split(':', 2)[-1])

            line = file.readline()

    print("This video was created on {}and has a bitrate of {}".format(creation_time, bitrate))
    print("The file contains {} streams:".format(len(streams)))
    for stream in streams:
        print(stream)
