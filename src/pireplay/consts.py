VIDEO_EXT = ".mp4"
SNAPSHOT_EXT = ".jpg"


class Template:
    home = "index.html"
    replay = "replay.html"
    settings = "settings.html"
    network = "network.html"


class Route:
    # GET
    index = "/"
    replay = "/replay/<string:replay>"
    raw_replay = f"/raw-replay/<string:replay>{VIDEO_EXT}"
    settings = "/settings"
    network = "/network"
    raw_snapshot = f"/raw-snapshot{SNAPSHOT_EXT}"

    # POST
    capture = "/capture"
    snapshot = "/snapshot"
    settings_capture_time = "/settings/capture-time"
    settings_camera_resolution = "/settings/camera-resolution"
    refresh_network = "/network/refresh"
    register_network = "/network/register"

    # DELETE
    delete_replay = "/delete-replay"
    delete_all_replays = "/delete-all-replays"


class Header:
    raw_replay = "Raw-Replay"
    raw_snapshot = "Raw-Snapshot"


class Option:

    capture_times_values = [3, 5, 7, 10, 20, 30]
    capture_times = [(t, f"{t}s") for t in capture_times_values]

    camera_resolutions = [
        (0, "2304 × 1296, 30 FPS HDR"),
        (1, "2304 × 1296, 56 FPS"),
        (2, "1536 × 864, 120 FPS"),
    ]


class Camera:
    FPS = 60
    BUFFER_LEN = max(Option.capture_times_values)
    TMP_DIR = "/var/tmp/"
    SNAPSHOT_FILE = f"{TMP_DIR}snapshot{SNAPSHOT_EXT}"


class Config:
    # see `default_config.yaml` for fields documentation
    capture_time_index = "capture_time_index"
    camera_resolution_index = "camera_resolution_index"
    kept_replays = "kept_replays"
    directory = "directory"
    replays_location = "replays_location"
    config_location = "config_location"
    replay_name = "replay_name"

    network_interface = "network_interface"

    wifi_ssid = "wifi_ssid"
    wifi_password = "wifi_password"
    ap_ssid_prefix = "ap_ssid_prefix"
    ap_ssid_no_suffix = "ap_ssid_no_suffix"
    ap_password = "ap_password"

    config_options = [
        (capture_time_index, Option.capture_times),
        (camera_resolution_index, Option.camera_resolutions),
    ]


class Form:
    option_field = "index"
    delete_field = "replay"

    wifi_ssid = "ssid"
    wifi_password = "password"
