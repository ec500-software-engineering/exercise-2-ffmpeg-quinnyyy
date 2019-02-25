import subprocess
import os
import time
import Queue

def encode(file):
    vid_720p = "ffmpeg -i " + file + " -b:v 2M -r 30 -s hd720 hd720" + file
    vid_480p = "ffmpeg -i " + file + " -b:v 1M -r 30 -s hd480 hd480" + file
    print(file + " 720 is starting")
    subprocess.call(vid_720p, stdout=subprocess.DEVNULL, stderr=subprocess.STDOUT, shell=True)
    print(file + " 720 is finished")

    print(file + " 480 is starting")
    subprocess.call(vid_480p, stdout=subprocess.DEVNULL, stderr=subprocess.STDOUT, shell=True)
    print(file + " 480 is finished")

if __name__ == "__main__":
    start = time.time()
    encode("bball.mp4")
    end = time.time()
    print("It took ", end - start, " s")
