from __future__ import division

import time
import math
import openal
import sys
import pygame

def po(o):
  print
  print o
  for k in dir(o):
   if k[0] == '_': continue
   print "   ", k, repr(getattr(o, k))
  print

d = openal.Device()
po(d)
cl = d.ContextListener()
po(cl)
cl.position = 0,0,0
cl.velocity = 0,0,0
cl.orientation = 1,0,0 , 0,0,1 # forward, up

b = openal.Buffer(sys.argv[1])
po(b)

s = cl.get_source()
po(s)

s.buffer = b
s.looping = True
s.gain = 1
#s.position=10,10,0

t = 0
clock = pygame.time.Clock()
s.play()
while True:
    t += clock.tick()/1000
    #s.position = 15*math.sin(t), 15*math.cos(t), 15*math.sin(t*5)*0
    #s.velocity = 15*math.cos(t), 15*-math.sin(t), 15*math.cos(t*5)*5*0
    #s.position = 10,10,t**2
    #s.velocity = 0,0,t*2
