import subprocess
from time import time

def encode(file):
    vid_720p = "ffmpeg -i " + file + " -b:v 2M -r 30 -s hd720 hd720" + file
    print(file + " 720 is starting")
    subprocess.call(vid_720p, stdout=subprocess.DEVNULL, stderr=subprocess.STDOUT, shell=True)
    print(file + " 720 is finished")

if __name__ == "__main__":
    start = time()
    encode("bball.mp4")
    end = time()
    print("It took ", end - start, " s")
