# musical-lights
RPi music controlled lights using [LightShow Pi](http://lightshowpi.org/), PWM controlled LED lights (n channels), and a variety of input methods:
- Playlist/single files
`sudo python py/synchronized_lights.py --file=[path]`
Read more here: http://lightshowpi.org/play-music/
- Network stream

- Audio input (USB soundcard)

Recommended settings for defaults.cfg:
- pin_modes = pwm (if too flickery, set to 'onoff')
