import click

from pireplay.config import safe_update_config_from_string
from pireplay.web_server import server


config_option = click.option("-c", "--config", type=click.File("r"))


@click.group()
def cli():
    pass

# TODO setup command to setup RPI as hotspot
# TODO reset command to setup RPI back on WiFi (dev), reverse of setup

# TODO basic CLI documentation


@cli.command()
@config_option
def serve(config):
    if config:
        safe_update_config_from_string(config.read())

    # FIXME remove debug
    server.run(debug=True, host="0.0.0.0", port=80)
