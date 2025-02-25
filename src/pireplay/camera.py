import os

from picamera2 import Picamera2, Preview
from picamera2.encoders import H264Encoder
from picamera2.outputs import CircularOutput

from pireplay.consts import Camera


ENCODER = H264Encoder(10 * 1000000, iperiod=Camera.FPS)

# FIXME make them non global
cam, output = None, None


def setup_camera():
    global cam, output

    if output is not None:
        output.stop()
        output.close()
        output = None
    if cam is not None:
        cam.stop_recording()
        cam.close()
        cam = None

    cam = Picamera2()

    mode0 = cam.sensor_modes[0]
    video_config = cam.create_video_configuration(
        main={"size": mode0["size"]},
        controls={"FrameRate": Camera.FPS}
    )
    cam.configure(video_config)
    cam.set_controls({"FrameRate": Camera.FPS})
    cam.set_controls({"AfMode": 2})
    cam.start_preview(Preview.NULL)


def start_recording():
    if cam is None:
        return

    global output

    output = CircularOutput(f"{Camera.TMP_DIR}buffer.h264", buffersize=Camera.BUFFER_LEN*Camera.FPS)
    cam.start_recording(ENCODER, output)


def save_recording(path, length):
    if cam is None or output is None:
        # running in debug without camera hardware, save fake file
        with open(path, "w") as file:
            file.write("")
        return

    output.start()
    output.stop()
    cam.stop_recording()

    os.system(f"ffmpeg -y -r {Camera.FPS} -i buffer.h264 -c:v copy -fps_mode passthrough {Camera.TMP_DIR}tmp.mp4")
    os.system(f"ffmpeg -y -r {Camera.FPS} -sseof -{length} -i {Camera.TMP_DIR}tmp.mp4 -c:v copy -fps_mode passthrough {path}")

    start_recording()
