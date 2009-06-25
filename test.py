import sys
import time
import math
import random
import os

import openal

device = openal.Device()
contextlistener = device.ContextListener()
source = openal.Source()
source2 = openal.Source()
expsources = [openal.Source() for i in xrange(20)]
buffer = openal.Buffer('sound.wav')
buffer2 = openal.Buffer('water.wav')
expbuffers = [openal.Buffer(os.path.join('explodes', x)) for x in os.listdir('explodes') if x[0] != '.']

contextlistener.position = 0, 0, 0
contextlistener.velocity = 0, 0, 0
contextlistener.orientation = 0, 1, 0, 0, 0, 1

source2.buffer = buffer2
source2.looping = True
source2.gain = .5
source2.position = 3, 3, -3
source2.play()

source.buffer = buffer
source.looping = True
source.gain = 1
source.play()

t = 0
amplitude = 5
freq = 5
amplitude2 = 0
freq2 = 10
explodetime = 0
x = 0
while True:
    x = not x
    source2.position = 3, 3, 3*(2*x-1)
    while explodetime < 0:
        explodetime += random.uniform(1, 1.5)
        src = expsources.pop(0)
        expsources.append(src)
        src.buffer = random.choice(expbuffers)
        src.position = [random.gauss(0, 15) for i in xrange(2)] + [abs(random.gauss(0, 10))]
        src.velocity = [random.gauss(0, 5) for i in xrange(3)]
        src.gain = random.uniform(8,12)
        src.play()
    for src in expsources:
        p = src.position
        v = src.velocity
        src.position = p[0]+v[0]*.01, p[1]+v[1]*.01, p[2]+v[2]*.01
    source.position = amplitude*math.sin(t*freq), 10+amplitude*math.cos(t*freq), amplitude2*math.sin(t*freq2)
    source.velocity = amplitude*freq*math.cos(t*freq), -amplitude*freq*math.sin(t*freq), amplitude2*freq2*math.cos(t*freq2)
    time.sleep(.01)
    t += .01
    explodetime -= .01
