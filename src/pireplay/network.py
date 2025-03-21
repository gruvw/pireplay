import time

import nmwifi
from pireplay.config import Config, config


# FIXME make this not global
# global near SSIDs cache
cached_ssids = []


def get_ap_ssid():
    mac = nmwifi.get_mac_address(config(Config.network_interface))
    mac = mac.replace(":", "")
    mac_suffix = mac[-4:]

    suffix = "" if config(Config.ap_ssid_no_suffix) else f"-{mac_suffix}"

    return config(Config.ap_ssid_prefix) + suffix


def setup_network():
    nmwifi.setup(
        config(Config.network_interface),
        config(Config.wifi_ssid) or None,
        config(Config.wifi_password) or None,
        get_ap_ssid() or None,
        config(Config.ap_password) or None,
    )


def refresh_cached_ssids():
    nmwifi.clean()

    time.sleep(5) # wait successful disconnect before rescan

    cached_ssids.clear()
    cached_ssids.extend(
        nmwifi.available_networks(config(Config.network_interface))
    )

    setup_network()


def connected_to():
    return nmwifi.is_wifi_active() and config(Config.wifi_ssid)
