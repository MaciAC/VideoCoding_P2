import os
import scripts.ffmpeg_parser as parser
import scripts.rename as rename
import scripts.resize as resize
import scripts.transcode as transcode


# Initialization
menu = open("menu.txt", "r").read()
exit = False

# Start infinite loop
while not exit:


    # Show files in dir and ask user to enter which wants to use
    files = os.listdir()
    count = 0
    videos = []
    for file in files:
        if file.endswith('.mp4'):
            print("{} - {}".format(count,file))
            videos.append(file)
            count += 1

    filename = videos[int(input("\nWhich video do you want to edit?\nEnter the number besides the option\n"))]

    # get the option

    option = int(input(menu))

    # exit option
    if option == 0:
        exit = True
        break

    # At each option run the correspondent ffmpeg command asking the user some input if is necessary

    if option == 1:
        parser.parse_input_file(filename)

    if option == 2:
        new_name = input("Enter a new name for the video:\n")
        rename.rename_file(filename, new_name)

    if option == 3:
        w = int(input("Enter output width value:\n"))
        h = int(input("Enter output height value:\n"))
        resize.resize_input(filename, w, h)

    if option == 4:
        transcode.transcode_video(filename)
