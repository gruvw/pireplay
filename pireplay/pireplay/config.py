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


def update_config_from_string(config):
    try:
        update_config(yaml.safe_load(config))
    except:
        print("Config loading error: invalid config.")
        exit(1)

    print(_config)


def update_key(key, value):
    update_config({key, value})


def config(key):
    if key not in config:
        return None

    value = _config[key]

    if key == Config.replays_location:
        value = os.path.expanduser(value)

    return value
