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
- [X] Overwrite default config from web posts settings values routes
- [X] Pass yaml configuration file to CLI program to overwrite defaults
- [X] Delete replay web server endpoint + UI
- [X] Implement web page for settings
- [X] Implement the kept replays manager
- [X] 3D print case for the device
- [X] Configuration of RPI hotspot using python (separated from this project, see <https://github.com/gruvw/nmwifi>)
- [X] RPI camera module circular capture and video save on web button press
- [X] RPI camera working autofocus
- [X] RPI camera module circular capture configuration of duration change on the fly (using settings endpoints)
- [X] Add `ap_ssid_no_suffix` configuration option
- [X] Use video MP4 with standard video encoding (send through applications)
- [X] Delete all stored replays button
- [X] Take a snapshot (picture) button
- [X] Option in config for recording vertical videos (rotate the image), https://github.com/gruvw/pireplay/issues/1
- [ ] Add manual video download button (should work on Safari)
- [ ] Make auto-focus an option with three choices: focus on startup, focus on startup+refresh+capture, constant auto-focus
- [ ] Fix the slow response to capture requests in AP mode, https://github.com/gruvw/pireplay/issues/2
- [ ] HTTPS and SSL certificate offline locally hosted
- [ ] Switch recording to CircularOutput2 & PyavOutput (picamera2)
- [ ] RPI camera module on the fly configuration of resolution
- [ ] Add audio with mic
- [ ] On the fly new Wi-Fi network connection from local web server (list SSIDs and input password)
- [ ] Add a video cropping/zooming feature
- [ ] Slow motion mode with slow replay buttons
- [ ] Fix automatic workflow package publish (build dependency issues with libcap)

## Documentation

- [X] Document usage (user guide) on README
- [X] 3D print documentation and DIY instructions on README
- [X] Document final result (pictures of hardware + UI) on README
- [X] Document Web UI using screenshots
- [X] Document yaml config and link the default config as example on README
- [X] Document API usage for developers ("/capture" and "/raw-replay" + header and delete, integrate with another applications like streaming) on README
- [X] CLI click documentation (proper `--help`)
- [X] Build from source README instructions
