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
