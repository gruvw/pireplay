import click
import logging

from pireplay.config import safe_update_config_from_string
from pireplay.consts import Config
from pireplay.web_server import server
from pireplay.network import refresh_cached_ssids


@click.group()
def cli():
    pass


@cli.command()
@click.option("-c", "--config", type=click.File("r"))
@click.option("--debug", is_flag=True)
def run(config, debug):
    if not debug:
        werkzeug_log = logging.getLogger("werkzeug")
        werkzeug_log.disabled = True
        click.secho = click.echo = lambda *_, **__: None

    print("Starting PiReplay server")

    # do it once first to get the correct "directory" element
    if config:
        safe_update_config_from_string(config.read())

    # get the current config from PiReplay directory
    with open(config(Config.config_location), "r") as file:
        safe_update_config_from_string(file.read())

    # do it a second time to override current config with argument passed one
    if config:
        safe_update_config_from_string(config.read())

    refresh_cached_ssids()

    server.run(debug=debug, host="0.0.0.0", port=80)
