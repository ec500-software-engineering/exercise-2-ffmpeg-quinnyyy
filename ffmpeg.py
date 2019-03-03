import subprocess
from pathlib import Path
#import sys
#from time import time

def encode(file: Path) -> dict:
    vid_720p = "ffmpeg -i " + file[2:] + " -b:v 2M -r 30 -s hd720 hd720" + file[2:]
    print(file + " 720 is starting")
    subprocess.call(vid_720p, stdout=subprocess.DEVNULL, stderr=subprocess.STDOUT, shell=True)
    print(file + " 720 is finished")
#def encode(file):
#    vid_720p = "ffmpeg -i " + file + " -b:v 2M -r 30 -s hd720 hd720" + file
#    print(file + " 720 is starting")
#    subprocess.call(vid_720p, stdout=subprocess.DEVNULL, stderr=subprocess.STDOUT, shell=True)
#    print(file + " 720 is finished")

if __name__ == "__main__":
    #start = time()
    #encode("bball.mp4")
    #end = time()
    #print("It took ", end - start, " s")
    encode('./bball.mp4')
