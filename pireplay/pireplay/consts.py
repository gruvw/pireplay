VIDEO_EXT = ".mp4"


class Header:
    raw_replay = "Raw-Replay"


class Template:
    home = "index.html"
    replay = "replay.html"
    settings = "settings.html"


class Route:
    index = "/"
    replay = "/replay/<string:replay>"
    raw_replay = f"/raw-replay/<string:replay>{VIDEO_EXT}"
    settings = "/settings"
    capture = "/capture"
    # TODO settings value routes


class Config:
    # see `default_config.yaml` for fields documentation

    capture_time = "capture_time"
    kept_replays = "kept_replays"
    replays_location = "replays_location"
    replay_name = "replay_name"
    # TODO resolution + frame rate
    # TODO wifi hotspot SSID and password


class Option:
    capture_times = [60, 30, 20, 10, 5, 3]
