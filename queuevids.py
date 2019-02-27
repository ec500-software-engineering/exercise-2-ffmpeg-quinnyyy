import queue
import threading
from ffmpeg import encode

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

    print("Finished processing!")

if __name__ == "__main__":
    queue_vids(["bball.mp4", "bball2.mp4", "bball3.mp4", "bball4.mp4"],encode)
