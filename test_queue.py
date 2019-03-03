from queuevids import queue_vids
from ffmpeg import encode
from probe import ffprobe_sync
from pytest import approx
import os

#Check if all the files are the same duration
def test_queue():
    files = ["./bball.mp4","./bball2.mp4","./bball3.mp4","./bball4.mp4"]
    out_files = ["./hd720bball.mp4","./hd720bball2.mp4","./hd720bball3.mp4","./hd720bball4.mp4"]
    queue_vids(files, encode)
    for i in range(4):
        actual_time = float(ffprobe_sync(files[i])['streams'][0]['duration'])
        new_time = float(ffprobe_sync(out_files[i])['streams'][0]['duration'])
        assert actual_time == approx(new_time,.1), "They're not the same time"
        os.remove(out_files[i])

if __name__ == "__main__":
    test_queue()
