import os
import subprocess

def parse_input_file(filename):
    # execute command and save output in a file
    os.system("ffmpeg -i {} > aux.txt 2>&1".format(filename))

    # open info file
    with open("aux.txt",'r') as file:
        line = file.readline()
        streams = []
        # read the file line by line checking if contains certain info
        while line:
            if "Duration" in line:
                duration = line.split(':', 1)[-1].split(',')[0]
            if "bitrate" in line:
                bitrate = line.split("bitrate:")[-1]
            if line.startswith("    Stream"):
                streams.append(line.split(':', 2)[-1])

            line = file.readline()

    # print info
    print("Video duration: {} \nVideo bitrate: {}".format(duration, bitrate))
    print("The file contains {} streams:".format(len(streams)))
    for stream in streams:
        print(stream)
