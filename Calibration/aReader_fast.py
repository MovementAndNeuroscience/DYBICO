#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov  2 09:40:44 2017

@author: stoffer
"""

import serial
import threading
import numpy as np
import time
import scipy.interpolate as interp
import platform
import serial.tools.list_ports
import ctypes

# def getRv(x,R1=9.1e3,counts=1023):
#     #Vv=V0*x/(counts-1)
#     #Rv=V0*R1/Vv-R1
#     return (counts/x-1)*R1


# Rvm=np.array((np.inf,30e3,6e3,1e3,250)) #measured resistance across force sensor
# Fm=np.array((0.,0.2,1,10,100)) #measurements in N
# intF=interp.interp1d(1./Rvm,Fm,'cubic',fill_value='extrapolate')

# def Rv_to_force(Rv):
#     return(intF(1./Rv))

def readloop(port,obj):
    # import os 
    # path = os.getcwd() 
    # if not os.path.exists('DATA'): os.makedirs('DATA')
    # os.chdir(path+'\DATA')
    
    ser = serial.Serial(obj.port, 115200, timeout=0.) #obj.port, 115200, timeout=0.
    debug=obj.debug
    ser.flushInput()
    ser.flushOutput()
    buf = b''
    nsamp=np.uint64(1)
    if not obj.dump is None:
        dump = open(obj.dump,'wb')
        np.float64(time.time()).tofile(dump)
        np.uint64(2).tofile(dump)
    obj.i = 0
    t0=time.time()

    try:
        while not obj.stopev.is_set():
            buf += ser.read(ser.inWaiting())
            lines = buf.split(b'\n')
            for line in lines[:-1]:
                try:
                    x = np.fromstring(line,dtype=np.int16,sep=' ')
                    t = np.float64(time.time())
                    if x.shape[0] == obj.cache.shape[1]:
                        obj.lock.acquire()
                        if obj.i >= obj.cache.shape[0]:
                            obj.i = 0
                        obj.cache[obj.i,:] = x
                        obj.i += 1        
                        obj.lock.release()
                        if not obj.dump is None:
                            t.tofile(dump)
                            nsamp.tofile(dump)
                            x.tofile(dump)
                except:
                      pass
                        
            buf=lines[-1]
            if debug and (time.time()-t0)>1:
                print('%s, %i'%(lines,ser.isOpen()))
                t0=time.time()
    
    except: 
        pass 
    
    finally:
        print('closing serial port')
        ser.close()
        if not obj.dump is None:
            dump.close()

   # os.chdir(path)

class aReader:
    def __init__(self,port=None,nchannels=2,dump=None,ncache=500*60*20,debug=False):
        if port is None:
            ports=[list(i) for i in serial.tools.list_ports.comports()]
            print(ports)
            p=np.nonzero([i[1].find('CP210x')>0 for i in ports])[0]
            if len(p)>0:
                p=int(p[0])
                port=ports[p][0]
                print('Port identified %s'%port)
        self.port=port
        self.dump=dump
        self.debug=debug
        self.stopev = threading.Event()
        self.lock = threading.RLock()
        self.ncache = ncache
        self.cache = np.zeros((ncache,nchannels+1),dtype=np.int16)
        self.i = 0
        self.thread=threading.Thread(target=readloop,args=(port,self))
        self.thread.start()
        #self.calibration=np.load('calibration.npy')
    
    def getValues(self,hist=1):
        if hist>self.ncache:
            hist=self.ncache
        self.lock.acquire()
        wraparound=self.i-hist
        if wraparound<0:
            x=np.concatenate((self.cache[wraparound:],self.cache[:self.i]),axis=0).copy()
        else:
            x=self.cache[wraparound:self.i].copy()
        self.lock.release()
        return x
    
    def getNSamples(self,hist=1):
        if hist>self.ncache:
            hist=self.ncache
        self.lock.acquire()
        wraparound=self.i-hist
        if wraparound<0:
            x=np.concatenate((self.cache[wraparound:],self.cache[:self.i]),axis=0).copy()
        else:
            x=self.cache[wraparound:self.i].copy()
        self.lock.release()
        x=self.calibration[x[:,1:]]*2*9.815 #2mV/V (5V,Gain 1000, rated output 20kgm= 2kg/V*G=9.815) in Newton
        return x
    
    def stop(self):
        self.stopev.set()
        self.thread.join(1.)
    
    def __del__(self):
        self.stop()

# '''
# #Example:
if __name__ == "__main__":
    import time
    a=aReader(port='COM6',nchannels=2,dump=None,ncache=1000) # port='/dev/ttyUSB0'
    for i in range(1200):
        print(a.getValues(1))
        time.sleep(0.01)
        
#'''