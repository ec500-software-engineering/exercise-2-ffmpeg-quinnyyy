from ffmpeg import encode
from probe import ffprobe_sync
from pytest import approx
import os

#Check if the files are the same duration
def test_encode():
    encode(file="bball.mp4")
    actual_time = float(ffprobe_sync("bball.mp4")['streams'][0]['duration'])
    new_time = float(ffprobe_sync("hd720bball.mp4")['streams'][0]['duration'])
    assert actual_time == approx(new_time,.1), "They're not the same time"
    #Delete the file after you're done
    os.remove("./hd720bball.mp4")

if __name__ =="__main__":
    test_encode()
