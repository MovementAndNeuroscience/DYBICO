# -*- coding: utf-8 -*-
"""
Created on Wed Dec  2 18:56:54 2020

@author: khm
"""

from __future__ import division

from psychopy import visual, event, core
import numpy as np
import numpy
import aReader_fast as aReader
import time
pico=aReader.aReader(debug=False,dump='dump.raw')

mywin = visual.Window([800, 800])

cres=50#defines visual feedback circle
cR=.5
p=-numpy.linspace(0,2*numpy.pi,cres)+numpy.pi/2
cc=numpy.vstack(((0,0),cR*numpy.array((numpy.cos(p),numpy.sin(p))).T))
p1=np.linspace(-.5*np.pi,.5*np.pi,256)
halfc1=np.vstack((np.cos(p1),np.sin(p1))).T
halfc2=np.vstack((-np.cos(p1),np.sin(p1))).T
interp=True
aspectrsc=float(mywin.size[0])/mywin.size[1]
circ1= visual.ShapeStim(win=mywin, units='norm', lineWidth=10.0, lineColor='white', lineColorSpace='rgb', fillColor=None,\
        fillColorSpace='rgb', vertices=halfc1, closeShape=False, pos=(0, 0), ori=0.0, opacity=1.0,\
        interpolate=interp)
lin1= visual.ShapeStim(win=mywin, units='norm', lineWidth=10.0, lineColor=None, lineColorSpace='rgb', fillColor=None,\
        fillColorSpace='rgb', vertices=halfc1[[0,-1],:], closeShape=False, pos=(0, 0), ori=0.0, opacity=1.0,\
        interpolate=interp)
circ2= visual.ShapeStim(win=mywin, units='norm', lineWidth=10.0, lineColor='green', lineColorSpace='rgb', fillColor=None,\
        fillColorSpace='rgb', vertices=halfc2, closeShape=False, pos=(0, 0), ori=0.0, opacity=1.0,\
        interpolate=interp)
lin2= visual.ShapeStim(win=mywin, units='norm', lineWidth=10.0, lineColor=None, lineColorSpace='rgb', fillColor=None,\
        fillColorSpace='rgb', vertices=halfc2[[0,-1],:], closeShape=False, pos=(0, 0), ori=0.0, opacity=1.0,\
        interpolate=interp)        
circ1l= visual.ShapeStim(win=mywin, units='norm', lineWidth=5.0, lineColor=(1.0, 0.0, 0.0), lineColorSpace='rgb', fillColor=None,\
        fillColorSpace='rgb', vertices=halfc1, closeShape=False, pos=(0, 0), ori=0.0, opacity=1.0,\
        interpolate=interp)
lin1l= visual.ShapeStim(win=mywin, units='norm', lineWidth=5.0, lineColor=(1.0, 0.0, 0.0), lineColorSpace='rgb', fillColor=None,\
        fillColorSpace='rgb', vertices=halfc1[[0,-1],:], closeShape=False, pos=(0, 0), ori=0.0, opacity=1.0,\
        interpolate=interp)        
circ2l= visual.ShapeStim(win=mywin, units='norm', lineWidth=5.0, lineColor=(1.0, 0.0, 0.0), lineColorSpace='rgb', fillColor=None,\
        fillColorSpace='rgb', vertices=halfc2, closeShape=False, pos=(0, 0), ori=0.0, opacity=1.0,\
        interpolate=interp)
lin2l= visual.ShapeStim(win=mywin, units='norm', lineWidth=5.0, lineColor=(1.0, 0.0, 0.0), lineColorSpace='rgb', fillColor=None,\
        fillColorSpace='rgb', vertices=halfc2[[0,-1],:], closeShape=False, pos=(0, 0), ori=0.0, opacity=1.0,\
        interpolate=interp)

c1=visual.Circle(mywin,lineColor='red')
c2=visual.Circle(mywin,lineColor='blue')
txt=visual.TextStim(mywin,pos=(0,.9))
t = 0
globalClock = core.Clock()
time.sleep(.5)
offset = np.mean(pico.getValues(10)[:,1:],axis=0)[None]
offset = np.array((1575,1575))[None]
while not event.getKeys():
    t = globalClock.getTime()
    v=pico.getValues(10)[:,1:]-offset
    v=v.mean(0)
    txt.setText('%i\n(%i,%i)'%(v.mean(),v[0],v[1]))
    txt.draw()
    circ1.setSize(v[0]/10*np.array([1,1]))
    circ1.draw()
    #c2.setSize(v[1]/800*np.array([1,1]))
    circ2.setSize(v[1]/10*np.array([1,1]))
    circ2.draw()
    mywin.flip()
pico.stop()
del pico
mywin.close()
core.quit()