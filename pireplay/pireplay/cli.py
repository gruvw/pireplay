import click

from pireplay.web_server import server


@click.group()
def cli():
    pass

# TODO Add a config.yaml that we pass as argument
# configures the default replay time, number of kept replays,
# resolution and frame rate, replays default location path,
# wifi hotspot SSID and password, default replay name (strftime)

# TODO setup command to setup RPI as hotspot
# TODO reset command to setup RPI back on WiFi (dev), reverse of setup

# TODO basic CLI documentation

@cli.command()
def serve():
    # FIXME remove debug
    server.run(debug=True, host="0.0.0.0", port=80)
