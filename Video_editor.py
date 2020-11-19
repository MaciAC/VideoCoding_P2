import os
import scripts.ffmpeg_parser as parser
import scripts.resize as resize
import scripts.transcode as transcode

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

    if option == 2:
        w = int(input("Enter output width value:\n"))
        h = int(input("Enter output height value:\n"))
        resize.resize_input(filename, w, h)

    if option == 3:
        transcode.transcode_video(filename)
