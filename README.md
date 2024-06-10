# PiReplay

Capture and instantly replay the last moments using a Raspberry Pi and a camera with a WEB application.

## Repository Structure

A short description of the project's structure for quick reference:

- `src`: the source code of the [Python](https://www.python.org/) `pireplay` package (using [Poetry](https://python-poetry.org/))
- `cad`: for 3D models files, 3D printing

## Do It Yourself

Here are the instructions (tutorial) for setting up a fully working **PiReplay** device, using a **Raspberry Pi Zero 2 W**.

### Requirements

- Raspberry Pi Zero 2 W board
- Micro SD card 64 GB
- Raspberry Pi Camera module 3 (NoIR wide 120FOV, black)
- Micro USB cable

### Raspberry Pi Zero Setup

1. Download and install the Raspberry Pi OS Imager: <https://www.raspberrypi.com/software/>
2. Connect the SD card to your computer and flash the OS on the card using Raspberry Pi OS Imager
    1. _Raspberry Pi Device_: `Raspberry Pi Zero 2 W`
    2. _Operating System_:  Raspberry Pi OS (other) > `Raspberry Pi OS Lite (64-bit)`
    3. _Storage_: Select SD card
    4. _Next_ > Edit Settings (additional configuration)
        - General > Set hostname: `pireplay.local`
        - General > Set username and **password**: `pireplay` (use a safe password)
        - General > Configure wireless LAN: use your current Wi-Fi network credentials (for setup purposes, we will use a Wi-Fi Hotspot later).
        - Services > Enable SSH (using password authentication)
    5. Flash the SD card and wait till it completes
3. Insert the SD card inside the Raspberry Pi and power it using the micro USB cable (wait a few seconds)
4. Connect to your Raspberry Pi using an SSH client
    - You can connect using [Putty](https://www.putty.org/), or simply running `ssh` from your terminal
    - Connect using `pireplay@pireplay.local` as the host (use port 22)
    - Enter the password you specified in Pi OS Imager during configuration

You are now connected via SSH to your brand new Raspberry Pi Zero.

### PiReplay Setup

TODO

## Contributions

Feel free to contribute by submitting pull requests, whether to add new features, improve existing functionality, or fix bugs :)

Before opening a new PR, make sure to open an issue to discuss it beforehand (first check if a similar issue does not already exist).
