from ffmpeg import encode
from probe import ffprobe_sync
from pytest import approx
import os

#Check if the files are the same duration
def test_encode():
    file_in = './bball.mp4'
    file_out = './hd720bball.mp4'
    encode(file=file_in)
    actual_time = float(ffprobe_sync(file_in)['streams'][0]['duration'])
    new_time = float(ffprobe_sync(file_out)['streams'][0]['duration'])
    assert actual_time == approx(new_time,.1), "They're not the same time"
    #Delete the file after you're done
    os.remove(file_out)

if __name__ =="__main__":
    test_encode()
