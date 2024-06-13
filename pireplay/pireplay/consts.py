VIDEO_EXT = ".mp4"


class Template:
    home = "index.html"
    replay = "replay.html"
    settings = "settings.html"


class Route:
    # GET
    index = "/"
    replay = "/replay/<string:replay>"
    raw_replay = f"/raw-replay/<string:replay>{VIDEO_EXT}"
    settings = "/settings"

    # POST
    capture = "/capture"
    settings_capture_time = "/settings/capture-time"
    settings_camera_resolution = "/settings/camera-resolution"

    # DELETE
    delete_replay = "/delete-replay"


class Header:
    raw_replay = "Raw-Replay"


class Option:

    _capture_times_values = [3, 5, 10, 20, 30, 60]
    capture_times = [(t, f"{t}s") for t in _capture_times_values]

    # TODO use real camera recording options
    camera_resolutions = [
        (0, "2304 × 1296, 30 FPS HDR"),
        (1, "2304 × 1296, 56 FPS"),
        (2, "1536 × 864, 120 FPS"),
    ]


class Config:
    # see `default_config.yaml` for fields documentation
    capture_time_index = "capture_time_index"
    camera_resolution_index = "camera_resolution_index"
    kept_replays = "kept_replays"
    replays_location = "replays_location"
    replay_name = "replay_name"

    # TODO wifi hotspot SSID and password

    config_options = [
        (capture_time_index, Option.capture_times),
        (camera_resolution_index, Option.camera_resolutions),
    ]


class Form:
    option_field = "index"
    delete_field = "replay"
