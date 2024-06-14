import click
import logging

from pireplay.config import safe_update_config_from_string
from pireplay.web_server import server


@click.group()
def cli():
    pass


@cli.command()
@click.option("-c", "--config", type=click.File("r"))
@click.option("--debug", is_flag=True)
def run(config, debug):
    print("Starting PiReplay Server")

    if config:
        safe_update_config_from_string(config.read())

    if not debug:
        # TODO network config

        werkzeug_log = logging.getLogger("werkzeug")
        werkzeug_log.disabled = True
        click.secho = click.echo = lambda *_, **__: None

    server.run(debug=debug, host="0.0.0.0", port=80)
