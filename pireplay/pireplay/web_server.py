from minify_html import minify
from flask import Flask, render_template, redirect, url_for, send_from_directory

import pireplay.data as data
from pireplay.consts import VIDEO_EXT, Route, Template, Header


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
def raw_replay(replay):
    # TODO serve video files

    return send_from_directory("dummy_video_path", replay + VIDEO_EXT)


@server.route(Route.settings)
def settings():
    return render_template(Template.settings)


@server.route(Route.capture, methods=["POST"])
def capture():
    # TODO save video to file and return replay name
    replay_name = data.get_new_replay_name()

    response = redirect(url_for(replay.__name__, replay=replay_name))
    response.headers.add(
        Header.raw_replay,
        url_for(raw_replay.__name__, replay=replay_name)
    )

    return response


@server.after_request
def response_minify(response):
    if "text/html" in response.content_type:
        response.set_data(minify(response.get_data(as_text=True)))

    return response
