# PiReplay

Capture and instantly replay the last moments by using a web application controlling a [Raspberry Pi](https://www.raspberrypi.com) with a camera.

Take a look at the project's [roadmap](docs/roadmap.md) to see upcoming features (and all the work accomplished).

**Note** - Check out the `pireplay` [Python](https://www.python.org) package (CLI) on PyPI: <https://pypi.org/project/pireplay> (managed using [Poetry](https://python-poetry.org/)).

## Project Structure

A short description of the project's structure for quick reference:

- `cad`: for 3D models files, 3D printing
- `src`: the source code of the Python `pireplay` package

## Do It Yourself

Here are the instructions (tutorial) for setting up a fully working **PiReplay** device.

### Requirements

- Raspberry Pi board (recommended board: `Raspberry Pi 5 4GB`)
- Micro SD card 64 GB
- Raspberry Pi Camera module 3 (regular 75° sensor)
- CSI Camera FPC connector cable to Raspberry Pi (select the correct one depending on you Raspberry Pi board)
- Raspberry Pi alimentation (Micro USB/USB type C)
- PiReplay box (see below)

#### PiReplay box

<!-- TODO -->

### Quick Raspberry Pi Setup

1. Download and install the Raspberry Pi OS Imager: <https://www.raspberrypi.com/software/>
2. Connect the SD card to your computer and flash the OS on the card using Raspberry Pi OS Imager
    1. _Raspberry Pi Device_: select your correct device (`Raspberry Pi 5`, `Raspberry Pi Zero 2 W`, ...)
    2. _Operating System_:  Raspberry Pi OS (other) > `Raspberry Pi OS Lite (64-bit)`
    3. _Storage_: Select SD card
    4. _Next_ > Edit Settings (additional configuration)
        - General > Set hostname: `pireplay.local`
        - General > Set username and **password**: `pireplay` (use a secure password)
        - General > Configure wireless LAN: use your current Wi-Fi network credentials (only for setup purposes, we will use a Wi-Fi Hotspot configuration later).
        - Services > Enable SSH (using password authentication)
    5. Flash the SD card and wait till it completes
3. Insert the SD card inside the Raspberry Pi and power it using the micro USB cable (wait a few seconds)
4. Connect to your Raspberry Pi using an SSH client (on the same Wi-Fi network credentials used in the configuration)
    - You can connect using [Putty](https://www.putty.org/), or simply running `ssh` from your terminal
    - Connect using `pireplay@pireplay.local` as the host (use port 22)
    - Enter the password you specified in Pi OS Imager during configuration

You are now connected via SSH to your newly setup Raspberry Pi for PiReplay.

### PiReplay Setup

Once connected to the Raspberry Pi via SSH, you can install and set up the `pireplay` software to run on it.

<!-- TODO document PiReplay software install + setup -->
```sh
sudo apt update
sudo apt upgrade -y
sudo rpi-update

sudo apt install -y python3-picamera2 --no-install-recommends
sudo apt install -y ffmpeg

sudo apt install -y python3-pip
```
<!-- use sudo -H -E --break-system-packages to install -->
<!-- or maybe just sudo with break system -->

<!-- add to boot -->

(you might need to accept some installs if prompted)

INSTRUCTIONS NOT FINISHED

### Troubleshoot

If you run into network problems on you device, you might want to use SSH over USB to fix them.
Follow this tutorial to enable SSH over USB: <https://gist.github.com/etoxin/d96418f0732c0de36f0f3c22f9bdd75d>.

## Contributions

Feel free to contribute by submitting pull requests, whether to add new features, improve existing functionality, or fix bugs :)

Before opening a new PR, make sure to open an issue to discuss it beforehand (first check if a similar issue does not already exist).

## Powered by

This project would not be possible without the wonderful technologies below:

* [Python](https://www.python.org/)
* [Flask](https://github.com/pallets/flask/)
* [Raspberry Pi](https://www.raspberrypi.com/)
* [picamera2](https://github.com/raspberrypi/picamera2)
