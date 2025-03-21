import click
import logging

from pireplay.config import safe_update_config_from_string
from pireplay.config import config as config_func
from pireplay.consts import Config
from pireplay.web_server import server
from pireplay.network import refresh_cached_ssids
from pireplay.camera import setup_camera


@click.group()
def cli():
    pass


@cli.command(help="Starts the PiReplay server.")
@click.option("-c", "--config", type=click.File("r"), help="Provide YAML PiReplay custom config file.")
@click.option("--debug", is_flag=True, help="Enables debug mode. (for developers only)")
def run(config, debug):
    print("Starting PiReplay server...")

    if not debug:
        werkzeug_log = logging.getLogger("werkzeug")
        werkzeug_log.disabled = True
        click.secho = click.echo = lambda *_, **__: None

    config_content = config.read() if config else None
    # do it once first to get the correct "directory" element
    if config:
        safe_update_config_from_string(config.read())

    # get the current config from PiReplay directory
    # overwrite the passed directory
    with open(config_func(Config.config_location), "a+") as file:
        file.seek(0)
        safe_update_config_from_string(file.read())

    # do it a second time to overwrite current config with argument passed one
    if config_content:
        safe_update_config_from_string(config_content)

    refresh_cached_ssids()

    if not debug:
        setup_camera()

    print("PiReplay server started :)")

    server.run(debug=debug, host="0.0.0.0", port=80)
