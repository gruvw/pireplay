from flask import Flask, render_template, redirect, url_for, send_from_directory

import pireplay.data as data


class Template:
    home = "index.html"
    replay = "replay.html"
    settings = "settings.html"


class Route:
    index = "/"
    replay = "/replay/<string:replay>"
    raw_replay = "/raw-replay/<path:replay_path>"
    settings = "/settings"
    capture = "/capture"
    # TODO settings value routes


server = Flask(__name__)


def render_replay(replay=None):
    return render_template(
        Template.replay if replay else Template.home,
        past_replays=data.get_past_replays(),
        replay=replay,
    )


@server.route(Route.index)
def home():
    return render_replay()


@server.route(Route.replay)
def replay(replay):
    return render_replay(replay)


@server.route(Route.raw_replay)
def raw_replay(replay_path):
    # TODO serve video files

    return send_from_directory("dummy_video_path", replay_path)


@server.route(Route.settings)
def settings():
    return render_template(Template.settings)


@server.route(Route.capture, methods=["POST"])
def capture():
    # TODO save video to file and return replay name
    replay_name = "dummy_replay_name"

    return redirect(url_for(replay.__name__, replay=replay_name))
