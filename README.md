# Py 'N Cool

A python NVIDIA GPU dynamic fan controller for Linux.

This project is actually a self-taught attempt to master python development, good practices in python projects and programming in general.
For code style and projects guidelines, I'm following [Google's Python Style Guide](https://google.github.io/styleguide/pyguide.html) as primary source. PEP8 as a secondary one.

My plan is deploying a fully working CLI, later an GUI and additional features such as described below.

### Features (to be implemented - or not)
* Real-time temperature monitoring
* System Tray
* Profiles
* GUI
* Temperature x Speed graph


### About deprecated
The [deprecated](./deprecated/nvidia_fan_control-v1.sh) script is pretty much straightforward.
You can set the interval (seconds) to rerun the temperature check.
It works only for single GPU.
