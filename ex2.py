from queuevids import queue_vids
from ffmpeg import encode

if __name__ == "__main__":
    files = ["bball.mp4", "bball2.mp4", "bball3.mp4", "bball4.mp4"]
    queue_vids(files, encode)
