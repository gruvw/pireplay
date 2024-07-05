import nmwifi
from pireplay.config import Config, config


def get_ap_ssid():
    mac = nmwifi.get_mac_address(config(Config.network_interface))
    mac = mac.replace(":", "")
    suffix = mac[-4:]

    return config(Config.ap_ssid_prefix) + f"-{suffix}"


def setup_network():
    nmwifi.setup(
        config(Config.network_interface),
        config(Config.wifi_ssid),
        config(Config.wifi_password),
        get_ap_ssid(),
        config(Config.ap_password),
    )