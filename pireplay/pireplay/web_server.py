import functools
from minify_html import minify
from flask import (
    Flask,
    render_template,
    redirect,
    url_for,
    send_from_directory,
    request,
    abort
)

from pireplay import replays
from pireplay.consts import (
    VIDEO_EXT,
    Route,
    Template,
    Header,
    Option
)
from pireplay.config import (
    Config,
    config,
    update_config_field,
    validate_config_option
)


server = Flask(__name__)


def render_replay(replay=None):
    return render_template(
        Template.replay if replay else Template.home,
        past_replays=replays.get_past_replays(),
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
    return send_from_directory(
        config(Config.replays_location),
        replay + VIDEO_EXT,
    )


@server.route(Route.settings)
def settings():
    return render_template(Template.settings)


@server.route(Route.capture, methods=["POST"])
def capture():
    # TODO save video to file and return replay name
    replay_name = replays.get_new_replay_name()

    response = redirect(url_for(replay.__name__, replay=replay_name))
    response.headers.add(
        Header.raw_replay,
        url_for(raw_replay.__name__, replay=replay_name)
    )

    return response


# Helper decorator to wrap settings route with form argument (index) validation
def settings_route(route, options):
    def decorator(func):
        @server.route(route, methods=["POST"])
        @functools.wraps(func)
        def wrapper():
            value = request.form[Option.form_field]
            valid, index = validate_config_option(options, value)

            if not valid:
                abort(400)

            func(index)

            return redirect(url_for(settings.__name__))
        return wrapper
    return decorator


@settings_route(Route.settings_capture_time, Option.capture_times)
def settings_capture_time(index):
    update_config_field(Config.capture_time_index, index)


@settings_route(Route.settings_camera_resolution, Option.camera_resolutions)
def settings_camera_resolution(index):
    update_config_field(Config.camera_resolution_index, index)


@server.after_request
def response_minify(response):
    if "text/html" in response.content_type:
        response.set_data(minify(response.get_data(as_text=True)))

    return response
