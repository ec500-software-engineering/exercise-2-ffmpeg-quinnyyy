import queue
import threading
import subprocess
import os

def queue_vids(files, function):
    q = queue.Queue()
    for f in files:
        t = threading.Thread(target=function, args = (f,))
        t.daemon = True
        q.put(t)

    while not q.empty():
        t1 = q.get()
        t1.start()
        t2 = q.get()
        t2.start()
        t1.join()
        t2.join()

def encode2(file):
    vid_720p = "ffmpeg -i " + file + " -b:v 2M -r 30 -s hd720 hd720" + file
    print(file + " 720 is starting")
    subprocess.call(vid_720p, stdout=subprocess.DEVNULL, stderr=subprocess.STDOUT, shell=True)
    print(file + " 720 is finished")

if __name__ == "__main__":
    queue_vids(["bball.mp4", "bball2.mp4", "bball3.mp4", "bball4.mp4"],encode2)
