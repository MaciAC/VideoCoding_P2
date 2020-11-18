import os
import scripts.ffmpeg_parser as parser

menu = open("menu.txt", "r").read()
exit = False

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
        parser.parse_input_file(filename)
