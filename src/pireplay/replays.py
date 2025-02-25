import os
from datetime import datetime

from pireplay.config import Config, config
from pireplay.consts import VIDEO_EXT, Option
from pireplay.camera import save_recording


def capture_new_replay():
    replays_location = config(Config.replays_location)

    # remove latest replay if maximum number of kept replays reached
    kept_replays = [
        path for f in os.listdir(replays_location)
        if os.path.isfile(path := os.path.join(replays_location, f)) and
        f.endswith(VIDEO_EXT)
    ]
    if len(kept_replays) >= int(config(Config.kept_replays)):
        oldest_replay = min(kept_replays, key=os.path.getctime)
        os.remove(oldest_replay)

    # save new replay
    replay_name = datetime.now().strftime(config(Config.replay_name))
    replay_path = os.path.join(replays_location, replay_name + VIDEO_EXT)
    replay_length = Option.capture_times_values[int(config(Config.capture_time_index))]

    save_recording(replay_path, replay_length)

    return replay_name


def get_past_replays():
    replays_location = config(Config.replays_location)

    kept_replays = [
        f[:-len(VIDEO_EXT)]
        for f in os.listdir(replays_location)
        if os.path.isfile(os.path.join(replays_location, f)) and
        f.endswith(VIDEO_EXT)
    ]

    def replay_time(replay):
        path = os.path.join(replays_location, replay + VIDEO_EXT)
        return os.path.getctime(path)

    kept_replays.sort(key=replay_time, reverse=True)

    return kept_replays


def remove_replay(replay):
    path = os.path.join(config(Config.replays_location), replay + VIDEO_EXT)
    if not os.path.isfile(path):
        return False

    os.remove(path)

    return True
