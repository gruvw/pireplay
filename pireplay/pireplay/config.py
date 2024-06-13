import os
import copy
import yaml
from importlib import resources

from pireplay.consts import Config


_default_config_path = "default_config.yaml"

with resources.open_text(__package__, _default_config_path) as file:
    _default_config = yaml.safe_load(file)

_config = copy.deepcopy(_default_config)


def update_config(new_config):
    _config.update(copy.deepcopy(new_config))


def validate_config_option(options, value):
    try:
        index = int(value)
    except:
        return False, None

    if 0 > index or index >= len(options):
        return False, None

    return True, index


def safe_update_config_from_string(config_string):
    try:
        update_config(yaml.safe_load(config_string))
    except:
        print("Config loading error: invalid config.")
        exit(1)

    valid_options = [
        validate_config_option(options, config(config_field))[0]
        for config_field, options in Config.config_options
    ]

    if not all(valid_options):
        index = valid_options.index(False)
        config_field = Config.config_options[index][0]
        print(f"Config error: invalid index for option `{config_field}`.")
        exit(1)


def update_config_field(key, value):
    update_config({key: value})


def config(key):
    if key not in _config:
        return ""

    value = _config[key]

    if key == Config.replays_location:
        username = os.environ.get("SUDO_USER", os.environ.get("USERNAME"))
        value = os.path.expanduser(value.replace("~", "~" + username))
        if not os.path.exists(value):
            # FIXME should use user's permissions
            os.makedirs(value)

    return value
