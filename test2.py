import sys
import time
import math
import random
import os

import openal

device = openal.Device()
contextlistener = device.ContextListener()
source = contextlistener.get_source()
buffer = openal.Buffer(os.path.join('sounds', '440.wav'))

contextlistener.position = 0, 0, 0
contextlistener.velocity = 0, 0, 0
contextlistener.orientation = 0, 1, 0, 0, 0, 1

source.buffer = buffer
source.looping = True
source.gain = 1
source.play()

t = 0
amplitude = 1
freq = 1
while True:
    source.position = amplitude*math.sin(t*freq), amplitude*math.cos(t*freq), 0
    source.velocity = amplitude*freq*math.cos(t*freq), -amplitude*freq*math.sin(t*freq), 0
    print (t*180/math.pi)%360
    time.sleep(.01)
    t += .01
