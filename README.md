# VideoCoding_P2
## Seminar 2 of Video Coding: Python & video

**Task 1:** Create a python script able to parse the ‘ffmpeg–i BBB.mp4’ file, which can mark at least 3 relevant data from the container.

**Task 2:** Create a python script able to rename the 5 quality outputs of the BBB that you did in last seminar.

**Task 3:** Create a python script able to resize (resolution change) of any input given.

**Task 4:** Create a python script able to transcode the input into an output with another codec that we’ve seen in the Theory class.

### Requirements
	ffmpeg, Python3

### Executing
Run Video_editor.py in the same folder as the video you want to edit, you can have several videos in the folder.

Before every edition it will show the .mp4 files in the folder, and will ask which file you want to edit. Enter the option via the number besides the video.

In the menu you can choose which of the tasks defined above you want to realize entering the number beside the option. In addition, '0' closes the program.

* Task 1: Get info about duration and bitrate, and the different streams inside the video.
* Task 2: Rename the video.
* Task 3: Asks for width and height and resize the video to the specified ones.
* Task 4: Transcode the video to MPEG1 and MPEG2.
