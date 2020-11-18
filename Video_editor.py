import os
from scripts import ffmpeg_parser

menu = open("menu.txt", "r").read()
exit = False
current_dir = os.getcwd()
while not exit:
    files = os.listdir()
    count = 0
    videos = []
    for file in files:
        if file.endswith('.mp4'):
            print("{} - {}".format(count,file))
            videos.append(file)
            count += 1

    filename = videos[int(input("\nWhich video do you want to edit?\nEnter the number besides the option\n"))]

    option = int(input(menu))

    if option == 0:
        exit = True
        break
    if option == 1:
        ffmpeg_parser.parse_input_file(current_dir, filename)
