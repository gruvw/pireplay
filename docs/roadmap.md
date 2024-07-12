# PiReplay Roadmap

## Features

- [X] Set up Repository with good structure
- [X] Python package `pireplay` poetry project + release CI to PyPI
- [X] Design the basic website on Figma (+ implement feedback from UI/UX designers)
- [X] Set up `Flask` server with common basic routes
- [X] Configure python CLI `click` program entrypoint (using poetry package)
- [X] Document installation and setup of RPI Zero on README
- [X] Basic web Flask templates (css + html)
- [X] Light and Dark theme (CSS)
- [X] Implement web page for home page + replay
- [X] Python config management module
- [X] Override default config from web posts settings values routes
- [X] Pass yaml configuration file to CLI program to override defaults
- [X] Delete replay web server endpoint + UI
- [X] Implement web page for settings
- [X] Implement the kept replays manager
- [X] 3D print case for the device
- [ ] Configuration of RPI hotspot using python (separated from this project, see <https://github.com/gruvw/nmwifi>)
- [ ] On the fly new Wi-Fi network connection from local web server (list SSIDs and input password)
- [ ] RPI camera module circular capture and video save on web button press (evaluate maximum capture time in-memory)
- [ ] RPI camera module circular capture configuration of resolution + duration change on the fly (using settings endpoints)
- [ ] Physical Wi-Fi reset button on RPI to force hotspot configuration (set dummy ssid and password on wifi connection)

## Documentation

- [ ] 3D print documentation and DIY instructions on README
- [ ] CLI click documentation (proper `--help`)
- [ ] Document usage (user guide) on README (document saved replay location)
- [ ] Document yaml config and link the default config as example on README
- [ ] Document API usage for developers ("/capture" and "/raw-replay" + header and delete, integrate with another applications like streaming) on README
- [ ] Document final result (pictures of hardware + UI) on README
