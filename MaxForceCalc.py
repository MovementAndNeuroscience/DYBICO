# -*- coding: utf-8 -*-
"""
Created on Fri Oct  1 11:39:02 2021
@author: dzn332

MaxForceCalc

The global time for a maxforce_test is also saved in the pkl under 'GlobalTime', 
and can be read by: _readable=datetime.datetime.fromtimestamp(GlobalTime).strftime('%Y%m%d_%H-%M-%S')

"""

#%% ##########################################################################
def calc_perc_raw(rawL,rawR,upper,t_remove):
    import numpy as np 
    t_end = 30 # remove last second of datapoints 
    QL1=np.quantile(rawL[0][t_remove:-t_end], [0.5, upper])
    QL2=np.quantile(rawL[1][t_remove:-t_end], [0.5, upper])
    QL3=np.quantile(rawL[2][t_remove:-t_end], [0.5, upper])
    QR1=np.quantile(rawR[0][t_remove:-t_end], [0.5, upper])
    QR2=np.quantile(rawR[1][t_remove:-t_end], [0.5, upper])
    QR3=np.quantile(rawR[2][t_remove:-t_end], [0.5, upper])
    MaxL=np.mean([QL1[1],QL2[1],QL3[1]])
    MaxR=np.mean([QR1[1],QR2[1],QR3[1]])
    maxforce=[MaxR, MaxL] # should not be in newton
    return (QL1,QL2,QL3,QR1,QR2,QR3,MaxL,MaxR,maxforce)
 
    
 
#%% ##########################################################################
def load_maxes(mfdir):
    import pandas as pd
    import numpy as np 
    import os 
    
    # loading the data only for the task ON period 
    ONidx= [i for i, e in enumerate((pd.read_pickle(os.path.join(mfdir,'.\\maxforceL1'))['TrialType'][0])) if e == 1]    
    L1=np.array(pd.read_pickle(os.path.join(mfdir,'.\\maxforceL1'))['Left'][0][ONidx[0]:ONidx[-1]])
    tL1=np.array(pd.read_pickle(os.path.join(mfdir,'.\\maxforceL1'))['Fliptime'][0][ONidx[0]:ONidx[-1]])
    
    ONidx= [i for i, e in enumerate((pd.read_pickle(os.path.join(mfdir,'.\\maxforceL2'))['TrialType'][0])) if e == 1]    
    L2=np.array(pd.read_pickle(os.path.join(mfdir,'.\\maxforceL2'))['Left'][0][ONidx[0]:ONidx[-1]])
    tL2=np.array(pd.read_pickle(os.path.join(mfdir,'.\\maxforceL2'))['Fliptime'][0][ONidx[0]:ONidx[-1]])

    ONidx= [i for i, e in enumerate((pd.read_pickle(os.path.join(mfdir,'.\\maxforceL3'))['TrialType'][0])) if e == 1]    
    L3=np.array(pd.read_pickle(os.path.join(mfdir,'.\\maxforceL3'))['Left'][0][ONidx[0]:ONidx[-1]])
    tL3=np.array(pd.read_pickle(os.path.join(mfdir,'.\\maxforceL3'))['Fliptime'][0][ONidx[0]:ONidx[-1]])
    
    ONidx= [i for i, e in enumerate((pd.read_pickle(os.path.join(mfdir,'.\\maxforceR1'))['TrialType'][0])) if e == 1]    
    R1=np.array(pd.read_pickle(os.path.join(mfdir,'.\\maxforceR1'))['Right'][0][ONidx[0]:ONidx[-1]])
    tR1=np.array(pd.read_pickle(os.path.join(mfdir,'.\\maxforceR1'))['Fliptime'][0][ONidx[0]:ONidx[-1]])

    ONidx= [i for i, e in enumerate((pd.read_pickle(os.path.join(mfdir,'.\\maxforceR2'))['TrialType'][0])) if e == 1]    
    R2=np.array(pd.read_pickle(os.path.join(mfdir,'.\\maxforceR2'))['Right'][0][ONidx[0]:ONidx[-1]])
    tR2=np.array(pd.read_pickle(os.path.join(mfdir,'.\\maxforceR2'))['Fliptime'][0][ONidx[0]:ONidx[-1]])

    ONidx= [i for i, e in enumerate((pd.read_pickle(os.path.join(mfdir,'.\\maxforceR3'))['TrialType'][0])) if e == 1]        
    R3=np.array(pd.read_pickle(os.path.join(mfdir,'.\\maxforceR3'))['Right'][0][ONidx[0]:ONidx[-1]])
    tR3=np.array(pd.read_pickle(os.path.join(mfdir,'.\\maxforceR3'))['Fliptime'][0][ONidx[0]:ONidx[-1]])
    return (L1, tL1, L2, tL2, L3, tL3, R1, tR1, R2, tR2, R3, tR3)




#%% ##########################################################################
def calc_maxforce(logdir, mfdir, FW):
    import numpy as np
    import os     
    import sys 
    (L1, tL1, L2, tL2, L3, tL3, R1, tR1, R2, tR2, R3, tR3) = load_maxes(mfdir)
    
    # all values below lim [native units] are 0grams, so we exclude dem from the calculations
    lim=1 ### 
    rawL=[np.array(L1[L1>lim]), np.array(L2[L2>lim]), np.array(L3[L3>lim])]
    rawR=[np.array(R1[R1>lim]), np.array(R2[R2>lim]), np.array(R3[R3>lim])]
    
    # we adjust the time, to only look at the task ON period
    tL=[np.array(tL1[L1>lim])-min(tL1), np.array(tL2[L2>lim])-min(tL2), np.array(tL3[L3>lim])-min(tL3)]
    tR=[np.array(tR1[R1>lim])-min(tR1), np.array(tR2[R2>lim])-min(tR2), np.array(tR3[R3>lim])-min(tR3)]
    
    # calculate 75th percentile 
    upper = 0.75
    t_remove = int(60*0.5) # remove initial 500ms
    (QL1,QL2,QL3,QR1,QR2,QR3,MaxL,MaxR,maxforce) = calc_perc_raw(rawL,rawR,upper,t_remove)
    
    # introduce calibration/gram newton 
    # sensors L1 and R1, array of grams matching adc units [0-1022]
    calipath = os.path.join(os.path.split(os.path.abspath(sys.argv[0]))[0],'Calibration',FW) # type of featherweight 
    conv_L_MM = np.loadtxt(os.path.join(calipath, 'L1MM.csv'))
    conv_R_MM = np.loadtxt(os.path.join(calipath, 'R1MM.csv'))
    MF_int = np.round(maxforce,2).astype(int)
    R_gram = conv_R_MM[MF_int[0]]
    L_gram = conv_L_MM[MF_int[1]]
    maxforceGram = np.round([R_gram, L_gram],0) 
    
    return (maxforceGram, MaxL, MaxR, tL, rawL, tR, rawR, QL1, QL2, QL3, QR1, QR2, QR3, upper)




#%% ##########################################################################
# def calc_maxforce_raw(logdir, mfdir):
#     import numpy as np
#     import os 
#     os.chdir(mfdir)
    
#     (L1, tL1, L2, tL2, L3, tL3, R1, tR1, R2, tR2, R3, tR3) = load_maxes()

#     # all values below 10 [native units] are 0grams, so we exclude dem from the calculations
#     lim=10 ### 
#     rawL=[np.array(L1[L1>lim]), np.array(L2[L2>lim]), np.array(L3[L3>lim])]
#     rawR=[np.array(R1[R1>lim]), np.array(R2[R2>lim]), np.array(R3[R3>lim])]
    
#     # we adjust the time, to only look at the task ON period
#     tL=[np.array(tL1[L1>lim])-min(tL1), np.array(tL2[L2>lim])-min(tL2), np.array(tL3[L3>lim])-min(tL3)]
#     tR=[np.array(tR1[R1>lim])-min(tR1), np.array(tR2[R2>lim])-min(tR2), np.array(tR3[R3>lim])-min(tR3)]
    
#     # calculate 75th percentile 
#     upper = 0.75
#     # remove initial 400ms
#     t_remove = int(60*0.4) 
#     (QL1,QL2,QL3,QR1,QR2,QR3,MaxL,MaxR,maxforce) = calc_perc_raw(rawL,rawR,upper,t_remove)
   
#     return (maxforce, MaxL, MaxR, tL, rawL, tR, rawR, QL1, QL2, QL3, QR1, QR2, QR3, upper)






