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


def save_recording(path, length):
    if _cam is None or _output is None:
        # running in debug without camera hardware, save fake file
        with open(path, "w") as file:
            file.write("")
        return

    _output.fileoutput = f"{Camera.TMP_DIR}buffer.h264"
    _output.start()
    _output.stop()

    os.system(f"ffmpeg -y -r {Camera.FPS} -i {Camera.TMP_DIR}buffer.h264 -c copy -fps_mode passthrough {Camera.TMP_DIR}tmp.mp4")
    os.system(f"ffmpeg -y -r {Camera.FPS} -sseof -{length} -i {Camera.TMP_DIR}tmp.mp4 -c copy -fps_mode passthrough \"{path}\"")
