import os

from picamera2 import Picamera2, Preview
from picamera2.encoders import H264Encoder
from picamera2.outputs import CircularOutput

from pireplay.consts import Camera


_ENCODER = H264Encoder(4 * 1000000, iperiod=Camera.FPS)
_cam, _output = None, None


def setup_camera():
    global _cam, _output

    if _output is not None:
        _output.stop()
        _output.close()
        _output = None
    if _cam is not None:
        _cam.stop_recording()
        _cam.close()
        _cam = None

    _cam = Picamera2()

    video_config = _cam.create_video_configuration(
        main={"size": (1280, 720)},
        controls={"FrameRate": Camera.FPS, "AfMode": 2}
    )
    _cam.configure(video_config)

    _cam.start_preview(Preview.NULL)

    _output = CircularOutput(buffersize=Camera.BUFFER_LEN*Camera.FPS)
    _cam.start_recording(_ENCODER, _output)

    delete_snapshot()


def save_recording(path, length):
    if _cam is None or _output is None:
        # running in debug without camera hardware, save fake file
        with open(path, "w") as file:
            file.write("")
        return

    _output.fileoutput = f"{Camera.TMP_DIR}buffer.h264"
    _output.start()
    _output.stop()

    # convert to MP4 stream with metadata
    os.system(f"ffmpeg -y -r {Camera.FPS} -i {Camera.TMP_DIR}buffer.h264 -c copy {Camera.TMP_DIR}tmp.mp4")
    # trim to only keep the end of the video
    os.system(f"ffmpeg -y -r {Camera.FPS} -sseof -{length} -i {Camera.TMP_DIR}tmp.mp4 -c copy \"{path}\"")


def save_snapshot():
    if _cam is None:
        # running in debug without camera hardware, save fake file
        with open(Camera.SNAPSHOT_FILE, "w") as file:
            file.write("")
        return

    _cam.capture_file(Camera.SNAPSHOT_FILE)


def delete_snapshot():
    if os.path.isfile(Camera.SNAPSHOT_FILE):
        os.remove(Camera.SNAPSHOT_FILE)
