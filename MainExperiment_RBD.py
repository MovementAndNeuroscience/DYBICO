# -*- coding: utf-8 -*-
"""
Created on Tue Sep 21 13:24:50 2021
@author: Keenie Ayla
MAIN EXPERIMENT
"""

# import pandas as pd 
# settings = pd.read_pickle('C:/Users/dzn332/Documents/DYBICO/DATA/test_20211221/__RBDsettings__.pkl')
# logdir = 'C:/Users/dzn332/Documents/DYBICO/DATA/test_20211221'
# maxforce = [700,600]


##########################################################################
def run_it(settings, path, logdir, maxforce, offset, FW):
    import Helpers as kaah # helper functions import 
    #import Helpers_RBD as hrbd
    
    ##########################################################################
    # file for saving 
    import os
    import pandas as pd 
    import datetime, time 
    timestamp=time.time()
    timestamp_readable=datetime.datetime.fromtimestamp(timestamp).strftime('%Y%m%d_%H%M')
    save_it = pd.DataFrame()
    save_it_as_pkl = os.path.join(logdir,str("output_file_"+timestamp_readable+".pkl"))
    #save_it_as_csv = str(logdir+"\output_file2_"+timestamp_readable+".csv")


    ##########################################################################
    import numpy as np
    path = os.getcwd() 
    print('\n_____________________\n \n RUNNING IN: %s  \n_____________________\n' %logdir)
    
    tasks = settings[['Baseline_blocks', 'Symmetry_blocks', 'Asymmetry_blocks', 'Decoupled_blocks', 'Interleaved']]
    sets = settings[['max_step','no_of_levels','percent_of_maxforce', 'percent_change_from_baseline', 
                     'trial_duration', 'baseline_block_duration' ,'jitter_time', 'time_between_blocks', 
                     'trial_repetitions_in_block', 'sort_blocks', 'no_of_B_blocks', 'no_of_S_blocks',  
                     'no_of_A_blocks','no_of_D_blocks', 'smoothing','baseline_target']]
    
    # change variable types to match 
    all_vars=np.array(sets).flatten()
    for i in range(len(all_vars)):
        if type(all_vars[i]) == str:
            if all_vars[i] == 'Interleave' or all_vars[i] == 'Random':
                all_vars[i] = all_vars[i] 
            else : all_vars[i] = float(all_vars[i]) 
        if type(all_vars[i]) != str:
            if (all_vars[i] - int(all_vars[i]) == 0) == True : all_vars[i] = int(all_vars[i]) 
                # if isinstance(all_vars[i], int) == True: all_vars[i] = int(all_vars[i]) 
                # elif isinstance(all_vars[i], float) == True: all_vars[i] = float(all_vars[i]) 
                
    [max_step, no_of_levels, percent_of_maxforce, percent_change_from_baseline, 
     trial_duration, baseline_block_duration, jitter_time, time_between_blocks, 
     trial_repetitions_in_block, sort_blocks, no_of_B_blocks, no_of_S_blocks, no_of_A_blocks, 
     no_of_D_blocks, smoothing, baseline_target] = all_vars 
 
    no_of_blocks = [no_of_B_blocks, no_of_S_blocks, no_of_A_blocks, no_of_D_blocks]

    
    # save figures with information
    save_sets = os.path.join(logdir,str("table_of_settings"+timestamp_readable+".png"))
    save_conds = os.path.join(logdir,str("table_of_conditions"+timestamp_readable+".png"))
    # import dataframe_image as dfi # pip install dataframe_image
    # df_styled = sets.style.background_gradient() #adding a gradient based on values in cell
    # dfi.export(df_styled,save_sets)
    # df_styled = tasks.style.background_gradient() #adding a gradient based on values in cell
    # dfi.export(df_styled,save_conds)
    
    
    ##########################################################################
    # # DEFINE CIRCLE GOAL/TARGET SIZES - DEPENDING ON CONDITIONS SELECTED 
    pause_target = 0.01 # size of pause between blocks
    count3_target = 0.013
    count2_target = 0.012 
    count1_target = 0.011 
    inter_target = baseline_target
    # (targets, targets_names) = kaah.get_CRD_targets
    
    
    ##########################################################################
    # DEFINE ONSETS AND DURATIONS IN BLOCK STRUCTURE
    initial_dur = 0.1 # duration of baseline before experiment start # does not seem to have effect 
    (conditions, durations, onsets, target_names) = kaah.get_RBD_block(no_of_blocks, sort_blocks, baseline_target, trial_repetitions_in_block, percent_change_from_baseline, max_step, no_of_levels, jitter_time, trial_duration, baseline_block_duration, initial_dur, time_between_blocks)
    
    
    ##########################################################################
    # open inititation GUI interface 
    import sys
    from PyQt5 import QtWidgets
    from psychopy import event
    QtWidgets.QApplication(sys.argv)
    msgBox2 = QtWidgets.QMessageBox(text="READY TO INITIATE EXPERIMENT?")
    msgBox2.setStandardButtons(QtWidgets.QMessageBox.Yes )#| QtWidgets.QMessageBox.Cancel)
    res = msgBox2.exec_()  
    keys=event.getKeys()
    #if res == QtWidgets.QMessageBox.Cancel:
    #    msgBox2.hide()
    if res == QtWidgets.QMessageBox.Yes or len(keys)>0 and keys[0] == 'y':
        print(' ')
    log_ID = os.path.split(logdir)[1] 
    
    
    ##########################################################################
    # variables for saving
    save_it['log'] = [logdir]
    save_it['maxforceRL'] = [maxforce] 
    save_it['settings']=[settings] 
    save_it['set_conditions']=[conditions]
    save_it['set_durations']=[durations]
    save_it['set_onsets']=[onsets]
    
    # keenie=np.zeros(round(max(onsets)+2*max(durations))*70)
    save_forceL = []
    save_forceR = []
    save_time = []
    save_fliptime = []
    save_targetname = []
    save_target_ = []
    save_trialshift = []
    save_trial = []
    ## igen drop append 
    
    
    ##########################################################################
    # DEFINE EXP WINDOW
    from psychopy import visual, event 
    mywin=visual.Window(fullscr=True, screen=0) # fullscr=False, size=[1000,1000] changed from 800, 600
    mywin.setMouseVisible(False)
    scene=kaah.CircleScene(mywin)
    
    # trigger for fMRI 
    event.waitKeys(keyList=['5'])
    
    
    ##########################################################################
    # SAVE DATA UNDER LOG_ID
    import datetime, time 
    timestamp=time.time()
    timestamp_readable=datetime.datetime.fromtimestamp(timestamp).strftime('%Y%m%d_%H-%M-%S')
    filename=log_ID+'_%s.raw'%timestamp_readable
    
    
    ##########################################################################
    # READ FROM APPLEJACK DEVICE AND CORRECT OFFSET
    import aReader_KAA as aReader 
    import os 
    pico=aReader.aReader(debug=False,dump=os.path.join(logdir,filename)) # Specify port
        
    # sensors L1 and R1, array of grams matching adc units [0-1022]
    calipath = os.path.join(os.path.split(os.path.abspath(sys.argv[0]))[0],'Calibration',FW) # type of featherweight 
    conv_L_GM = np.loadtxt(os.path.join(calipath,'L1GM.csv'))
    conv_R_GM = np.loadtxt(os.path.join(calipath,'R1GM.csv'))
    
    
    ##########################################################################
    # Triggers to EEG system 
    send_trigger = False
    trigger_state = 0
    
    
    ##########################################################################
    # LIVE READING OF DEVICE INPUT 
    stop = False
    from psychopy import core, event
    trial = 0
    #baseline_break = 0
    globalClock = core.Clock()
    t0 = globalClock.getTime()
    global_time = time.time()
    
    while not stop:
        send_trigger = False
        t = globalClock.getTime()-t0
        save_time.append(t)
        if trial<len(onsets)-1 and t>=onsets[trial+1]:
            trial += 1
            print('Trial %s of %s - ' %(trial, len(onsets)-1) +target_names[trial])
            save_trialshift.append([trial, target_names[trial], onsets[trial], durations[trial], t])
            #kaah.send_trigger_by_name(target_names[trial], send_trigger=True) # reintroduce this line if EEG 
            #send_trigger = False
            
        if trial<len(onsets) and t-onsets[trial]<durations[trial]:
            scene.targetLeft,scene.targetRight = conditions[trial]
            save_targetname.append(target_names[trial])
            save_target_.append(conditions[trial])
            
        elif t>(onsets[-1]+durations[-1]):
            scene.targetLeft, scene.targetRight = [pause_target,pause_target]
            save_targetname.append(target_names[trial])
            save_target_.append([pause_target,pause_target])
            if t>(onsets[-1]+durations[-1]+2): # stop experiment after 2 sec 
                stop=True 
        else:
            scene.targetLeft, scene.targetRight = [inter_target,inter_target]
            save_targetname.append(target_names[trial])
            save_target_.append([inter_target, inter_target])

        save_trial.append(trial)
        
        
    ##########################################################################
    # READ INPUT WITH SPECIFIED SMOOTHING + SET MAXFORCE
        [maxR, maxL] = maxforce 
        v0=pico.getValues(smoothing)[:,1:] #-offset 
        
        # CALIBRATION INTEGRATION 'Right:v[0]'
        v_int = np.round(v0.mean(0),2).astype(int)
        R_gram = conv_R_GM[v_int[0]]
        L_gram = conv_L_GM[v_int[1]]
        v = np.round([R_gram, L_gram],2) 
        v_mean = v.copy()  
        
        # scaling is unified between L and R 
        mean_max = np.mean([maxL, maxR])
        scalingL=mean_max*((percent_of_maxforce/100)/baseline_target)
        scalingR=mean_max*((percent_of_maxforce/100)/baseline_target)
        
        scene.left = v_mean[1]/(scalingL)
        scene.right = v_mean[0]/(scalingR)
        save_forceL.append(v_mean[1]/(scalingL))
        save_forceR.append(v_mean[0]/(scalingR))
       
    ##########################################################################
    # CALL CircleScene Class DEFINITION TO DRAW
        scene.draw()
        mywin.flip()    
        save_fliptime.append(globalClock.getTime()-t0)    
    # SEND TRIGGER 
    #trigger(trigger_state, send_trigger, trigger_time, )
    
    
        
    #########################################################################
    # MANUALLY END EXPERIMENT
        keys=event.getKeys()
        if len(keys)>0:
            if keys[0] == 'q':
                stop = True
                #os.chdir(path)
                print('\n_____________________\n \n EXPERIMENT CANCELLED BY USER  \n_____________________\n')


    # SAVE IT 
    save_it['GlobalTime']=[global_time]
    save_it['target_name'] = [save_targetname]
    save_it['target'] = [save_target_]
    save_it['trial'] = [save_trial]
    save_it['left_force'] = [save_forceL]
    save_it['right_force'] = [save_forceR]
    save_it['time'] = [save_time]
    save_it['fliptime'] = [save_fliptime]
    save_it['save_trialshift']=[save_trialshift]
    
    save_it.to_pickle(save_it_as_pkl)
    print('\n_____________________\n \n DATA SAVED IN : %s  \n_____________________\n' %logdir)
    pico.stop()
    del pico
    mywin.close()
    #core.quit()
    
    # print out session duration 
    timestamp_session_end = time.time() 
    print("Session duration %.2f seconds"%(timestamp_session_end-timestamp))
    print("Session duration %.2f minutes"%((timestamp_session_end-timestamp)/60))

    
    #%% Making another dataframe 
    #kaah.reshape_data(save_it_as_pkl)



#%% 

# run_it(settings, logdir, maxforce)

