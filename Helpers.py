# -*- coding: utf-8 -*-
"""
Created on Tue Sep 21 13:19:30 2021
@author: Keenie Ayla
HELPER FUNCTIONS 
"""

#import struct
import ctypes 
import time
import numpy as np 
import random 
from itertools import permutations


import Helpers as hrbd 

#%% ##########################################################################
# GUI for defining and saving experimental settings 
def define_settings_CRD(logdir):  
    from psychopy import gui, visual 
    mywin1 = visual.Window([512,512]) # create a window
    sets=gui.Dlg(title='DEFINE SETTINGS')
    sets.addText('Conditions to include: (baseline is always included)')
    sets.addField('Left-hand increase force',initial=False)
    sets.addField('Left-hand decrease force',initial=False)
    sets.addField('Right-hand increase force',initial=True)
    sets.addField('Right-hand decrease force',initial=True)
    sets.addField('Symmetrical increase force',initial=True)
    sets.addField('Symmetrical decrease force',initial=True)
    sets.addField('Left increase + Right decrease',initial=True)
    sets.addField('Left decrease + Right increase',initial=True)
    
    sets.addText('Define experimental settings:')
    sets.addField('Number of blocks: [1<]', 5)
    sets.addField('Time between blocks: [seconds]', 5)
    sets.addField('Trial repetitions within block:', 4)
    sets.addField('Trial duration: [seconds]', 2)
    sets.addField('Jitter time: [seconds]', 0.1)
    sets.addField('Baseline duration between trials: [seconds]', 2) 
    
    sets.addText('Visual feedback:')
    sets.addField('Percent change from baseline:',0.5)
    sets.addField('Percent of maxforce to reach baseline:',0.05)
    sets.addField('Sample smoothing:',10)
        
    sets.show()
    if gui.OK:
        import pandas as pd
        tasks = pd.DataFrame()
        tasks['Baseline_force'] = ['Y']
        if sets.data[0]==True: tasks['Left_increase_force'] = ['Y'] 
        elif sets.data[0]!=True: tasks['Left_increase_force'] = [''] 
        if sets.data[1]==True: tasks['Left_decrease_force'] = ['Y']
        elif sets.data[1]!=True: tasks['Left_decrease_force'] = ['']
        if sets.data[2]==True: tasks['Right_increase_force'] = ['Y']
        elif sets.data[2]!=True: tasks['Right_increase_force'] = ['']
        if sets.data[3]==True: tasks['Right_decrease_force'] = ['Y']
        elif sets.data[3]!=True: tasks['Right_decrease_force'] = ['']
        if sets.data[4]==True: tasks['Sym_increase_force'] = ['Y']
        elif sets.data[4]!=True: tasks['Sym_increase_force'] = ['']
        if sets.data[5]==True: tasks['Sym_decrease_force'] = ['Y']
        elif sets.data[5]!=True: tasks['Sym_decrease_force'] = ['']
        if sets.data[6]==True: tasks['Asym_L_increase_R_decrease'] = ['Y']
        elif sets.data[6]!=True: tasks['Asym_L_increase_R_decrease'] = ['']
        if sets.data[7]==True: tasks['Asym_L_decrease_R_increase'] = ['Y']
        elif sets.data[7]!=True: tasks['Asym_L_decrease_R_increase'] = ['']
        
        settings_ = pd.DataFrame()
        settings_= tasks
        settings_['no_of_blocks']=sets.data[8]
        settings_['time_between_blocks']=sets.data[9]
        settings_['trial_repetitions']=sets.data[10]
        settings_['trial_duration']=sets.data[11]
        settings_['jitter_time']=sets.data[12]
        settings_['baseline_between_trials']=sets.data[13]
        settings_['percent_change_from_baseline']=sets.data[14]
        settings_['percent_of_maxforce']=sets.data[15]
        settings_['smoothing']=sets.data[16]
        settings_.to_pickle(gui.fileSaveDlg(initFilePath=logdir, initFileName="__CRDsettings__.pkl"))
        
    else:
        print('user cancelled')
        settings_="Not defined"
    mywin1.close()
    
    return settings_


#%% ##########################################################################
def trigger(trigger_state, send_trigger=True):
    #version = struct.calcsize("P")*8
    par = ctypes.windll.inpoutx64 #if python runs in 64 bit mode
    port=0x3FF8 #port number
    offstate = 0
    
    state=int(trigger_state)
    on_time=0.01
    global_time = time.time()
    while time.time()-global_time<on_time:
        par.Out32(port, state)
        #print(par.Inp32(port))
    par.Out32(port, offstate)
    print('Trigger being sent: %s'%state)
        


#%% ##########################################################################
def get_CRD_block(no_of_blocks, trial_repetitions, targets, jitter_time, trial_duration, baseline_between_trials, initial_dur, time_between_blocks):
    blocks, onsets_blocked, durations_blocked=[],[],[]
    for j in range(no_of_blocks): 
        block = []
        for i in range(trial_repetitions): 
            block.append(np.arange(len(targets)-1)+1)
        block=np.concatenate(block)
        
        # First block starts with pause followed by baseline 
        block_p=np.insert(np.random.permutation(block), 0, (0,1)) # conditions [1:] are in randomized order
        blocks.append(block_p)
        
        # introducing jitter on both duration [+-sec] and onset [+sec]        
        jitter_durations_blocked = 2*jitter_time*(np.random.rand(len(block_p))-0.5)
        jitter_onsets_blocked = abs(2*jitter_time*(np.random.rand(len(block_p))-0.5))

        dur_blocked = (trial_duration + jitter_durations_blocked) * np.ones(len(block_p)) # seconds duration
        ons_blocked = dur_blocked + jitter_onsets_blocked + baseline_between_trials

        dur_blocked[0]=initial_dur
        dur_blocked[1]=initial_dur
        if j==0: ons_blocked[0]=0
        ons_blocked[1]=dur_blocked[0]
        ons_blocked[2]=dur_blocked[0]
        
        durations_blocked.append(dur_blocked)
        onsets_blocked.append(ons_blocked)
        if j>=1:
            # introduce time to seperate blocks
            durations_blocked[j][0] = time_between_blocks # the pause condition 
            onsets_blocked[j][1] += durations_blocked[j][0] # the baseline that follows
        
    onsets_blocked=np.cumsum(onsets_blocked)
    conditions = np.concatenate(blocks)
    durations = np.concatenate(durations_blocked)
    onsets = onsets_blocked 
    print(conditions)
    return (conditions, durations, onsets)



#%% ##########################################################################
def get_CRD_targets(tasks, LH, RH, percent_change_from_baseline, pause_target):
    # DEFINE CIRCLE GOAL/TARGET SIZES - DEPENDING ON CONDITIONS SELECTED
    targets = []
    targets_names = []
    
    incr = 1+percent_change_from_baseline # increasing size 
    decr = 1-percent_change_from_baseline # decreased size 
     
    targets.append(pause_target)
    targets_names.append('Pause_between_blocks')
    if tasks['Baseline_force'][0] == 'Y': 
        targets.append((LH,RH))
        targets_names.append('Baseline_force')
    if tasks['Left_increase_force'][0] == 'Y': 
        targets.append((LH*incr,RH))
        targets_names.append('Left_increase_force')
    if tasks['Left_decrease_force'][0] == 'Y': 
        targets.append((LH*decr,RH))
        targets_names.append('Left_decrease_force')  
    if tasks['Right_increase_force'][0] == 'Y': 
        targets.append((LH,RH*incr))
        targets_names.append('Right_increase_force')
    if tasks['Right_decrease_force'][0] == 'Y': 
        targets.append((LH,RH*decr))
        targets_names.append('Right_decrease_force')
    if tasks['Sym_increase_force'][0] == 'Y': 
        targets.append((LH*incr,RH*incr))
        targets_names.append('Sym_increase_force')
    if tasks['Sym_decrease_force'][0] == 'Y': 
        targets.append((LH*decr,RH*decr))
        targets_names.append('Sym_decrease_force')
    if tasks['Asym_L_increase_R_decrease'][0] == 'Y': 
        targets.append((LH*incr,RH*decr))
        targets_names.append('Asym_L_increase_R_decrease')
    if tasks['Asym_L_decrease_R_increase'][0] == 'Y': 
        targets.append((LH*decr,RH*incr))
        targets_names.append('Asym_L_decrease_R_increase')
    
    return (targets, targets_names)  




#%%
def send_trigger_by_name(current_target_name, send_trigger=True):
    if current_target_name == "Baseline_block": 
        triggers_to_send = 0
        trigger_RBD(trigger_state=int(triggers_to_send), send_trigger=True)
    elif current_target_name == "Pause_target": 
        triggers_to_send = 255
        trigger_RBD(trigger_state=int(triggers_to_send), send_trigger=True)
    
    else : 
        triggers_to_send = np.zeros(3)
        if current_target_name[0] == 'A' : triggers_to_send[0]=7
        if current_target_name[0] == 'S' : triggers_to_send[0]=8
        if current_target_name[0] == 'D' : triggers_to_send[0]=9
        
        if current_target_name[3] == '1' : triggers_to_send[1]=1
        if current_target_name[3] == '2' : triggers_to_send[1]=2
        if current_target_name[3] == '3' : triggers_to_send[1]=3
        if current_target_name[3] == '4' : triggers_to_send[1]=4
        if current_target_name[3] == '5' : triggers_to_send[1]=5
        if current_target_name[5] == '1' : triggers_to_send[2]=1
        if current_target_name[5] == '2' : triggers_to_send[2]=2
        if current_target_name[5] == '3' : triggers_to_send[2]=3
        if current_target_name[5] == '4' : triggers_to_send[2]=4
        if current_target_name[5] == '5' : triggers_to_send[2]=5
    
        for i in range(len(triggers_to_send)):
            trigger_RBD(trigger_state=int(triggers_to_send[i]), send_trigger=True)
    
    
#%% ##########################################################################
def trigger_RBD(trigger_state, send_trigger=True):
    #version = struct.calcsize("P")*8
    par = ctypes.windll.inpoutx64 #if python runs in 64 bit mode
    port=0x3FF8 #port number
    offstate = 0
    
    state=int(trigger_state)
    on_time=0.01
    global_time = time.time()
    while time.time()-global_time<on_time:
        par.Out32(port, state)
        #print(par.Inp32(port))
    par.Out32(port, offstate)
    #print('Trigger being sent: %s'%state)
    

#%%
def get_RBD_block(no_of_blocks, sort_blocks, baseline_target, trial_repetitions_in_block, 
                  percent_change_from_baseline, max_step, no_of_levels, jitter_time, trial_duration, 
                  baseline_block_duration, initial_dur, time_between_blocks):
    # import Helpers_RBD as hrbd
    [no_of_B_blocks, no_of_S_blocks, no_of_A_blocks, no_of_D_blocks] = no_of_blocks
     
    ## We make the sequence of blocks, either "interleaved" or completely random
    def interleave_blocks(no_of_blocks):
        [no_of_B_blocks, no_of_S_blocks, no_of_A_blocks, no_of_D_blocks] = no_of_blocks
        
        from itertools import chain, zip_longest
        l1=["Symmetry_block" for i in range(no_of_S_blocks)]
        l2=["Asymmetry_block" for i in range(no_of_A_blocks)]
        l3=["Decoupled_block" for i in range(no_of_D_blocks)]
        list_ = [x for x in chain(*zip_longest(l1, l2, l3)) if x is not None]
        
        import random
        randomstart = random.randint(0, 2)
        list_r = list_[randomstart:] + list_[:randomstart] # we randomize blocks
        
        list_blocks = list_r.copy()
        if no_of_B_blocks > 0 : 
            list_blocks = np.insert(list_, 0, "Baseline_block")
            
            if no_of_B_blocks > 1 :
                list_blocks = np.insert(list_blocks, (len(list_blocks)), "Baseline_block")

            if no_of_B_blocks > 2 :
                half_wayBs = round(len(list_)/(no_of_B_blocks-1))
                for i in range(1,no_of_B_blocks-1):
                    list_blocks = np.insert(list_blocks, i*(half_wayBs+1), "Baseline_block")
        return list_blocks
        
    def random_perm_blocks(no_of_blocks):
        [no_of_B_blocks, no_of_S_blocks, no_of_A_blocks, no_of_D_blocks] = no_of_blocks
        list_blocks = []
        for i in range(no_of_B_blocks): list_blocks.append("Baseline_block")
        for i in range(no_of_S_blocks): list_blocks.append("Symmetry_block")
        for i in range(no_of_A_blocks): list_blocks.append("Asymmetry_block")
        for i in range(no_of_D_blocks): list_blocks.append("Decoupled_block")
        list_blocks_p = np.random.permutation(list_blocks)
        return list_blocks_p
    
    if sort_blocks == "Interleave" : list_blocks = interleave_blocks(no_of_blocks)
    else : list_blocks = random_perm_blocks(no_of_blocks)
    
    pause_target = 0.01 
    targets_L, targets_R, durations_, target_names = [], [], [], []    
    for i in range(len(list_blocks)):
        # we start with a countdown 
        targets_L.append([pause_target])
        targets_R.append([pause_target])
        if i == 0 : time_ = initial_dur
        else : time_ = time_between_blocks
        durations_.append([time_])
        target_names.append('Pause_target')
        
        targets_L.append([0.013])
        targets_R.append([0.013])
        durations_.append([1])
        target_names.append('Pause_target')
        targets_L.append([0.012])
        targets_R.append([0.012])
        durations_.append([1])
        target_names.append('Pause_target')
        targets_L.append([0.011])
        targets_R.append([0.011])
        durations_.append([1])
        target_names.append('Pause_target')
        
        block_type = str(list_blocks[i])   # block_type = "Symmetry_block"   
        [targets_LH, targets_RH] = biman_targets_block(block_type, baseline_target, percent_change_from_baseline, trial_repetitions_in_block, max_step, no_of_levels)
        if block_type == "Baseline_block": 
            targets_L.append([targets_LH])
            targets_R.append([targets_RH])
            durations_.append([baseline_block_duration])
            target_names.append('Baseline_block')
        else:      
            targets = np.array([targets_LH, targets_RH])
            targets_L.append(targets[0])
            targets_R.append(targets[1])
            durations_.append(np.ones(len(targets_LH))*[trial_duration])
            
            cons = np.unique(targets)
            for k in range(len(targets_LH)): 
                target_names.append(get_target_name(targets_LH[k], targets_RH[k], cons, block_type))
    
    targets_LEFT = np.concatenate(targets_L)
    targets_RIGHT = np.concatenate(targets_R)
    conditions = np.transpose([targets_LEFT, targets_RIGHT])
    
    jitter_durations_blocked = 2*jitter_time*(np.random.rand(len(targets_LEFT))-0.5)
    durations = np.concatenate(durations_)+jitter_durations_blocked
    onsets = np.insert(np.cumsum(durations),0,0)[:-1]
    
    print('\n_____________________\n \n BLOCK SEQUENCE:  \n_____________________\n')
    print(list_blocks)
    return (conditions, durations, onsets, target_names)



#%%
def get_target_name(L,R,cons,block_type):
    block_name = block_type[0]
    if len(cons) == 3: names = ["2", "3", "4"]
    if len(cons) == 4: names = ["2", "3", "4", "5"]
    if len(cons) == 5: names = ["1","2", "3", "4", "5"]
    for i in range(len(names)): 
        if L == cons[i]: Ln = names[i]
        if R == cons[i]: Rn = names[i]
    target_name = str(block_name)+'_L'+str(Ln)+'R'+str(Rn)
    return target_name
    


#%%
def biman_targets_block(block_type, baseline_target, percent_change_from_baseline, trial_repetitions_in_block, max_step, no_of_levels): 
    #import Helpers_RBD as hrbd
    # we define LH sequence first, the RH will then be defined according to the block
    seq_LH = hrbd.make_sequence(trial_repetitions_in_block, max_step, no_of_levels)
    targets_LH = hrbd.translate_to_target(seq_LH, baseline_target, percent_change_from_baseline)
    
    if block_type == 'Baseline_block':
        targets_LH = baseline_target
        targets_RH = baseline_target
    if block_type == 'Symmetry_block': 
        targets_RH = targets_LH
    if block_type == 'Asymmetry_block': 
        seq_RH = abs(seq_LH-max(seq_LH))
        targets_RH = hrbd.translate_to_target(seq_RH, baseline_target, percent_change_from_baseline)        
    if block_type == 'Decoupled_block': 
          seq_RH = hrbd.make_sequence(trial_repetitions_in_block, max_step, no_of_levels)
          targets_RH = hrbd.translate_to_target(seq_RH, baseline_target, percent_change_from_baseline)
    
    return [targets_LH, targets_RH]



#%%
def make_sequence(trial_repetitions_in_block, max_step, no_of_levels):
    # automatic 
    levels_ = [0, 1, 2, 3, 4] # only 3,4,or 5
    if no_of_levels == 3 : levels = [1,2,3]
    else : levels = levels_[:no_of_levels] # if 4 levels then = [1,2,3,4] ->the lowest is left out 
    #trials_in_block = len(levels)*trial_repetitions_in_block
    
    # generating combinations of numbers 
    combos = list(permutations(levels))
    combos_sorted = []
    combos_jump = []
    for i in range(len(combos)):
        seq = combos[i] 
        save, jump = [], []
        for j in range(1,len(seq)):
            diff = abs(seq[j-1] - seq[j])
            if diff <= max_step :
                save.append(True)
                jump.append(diff)
        if sum(save)==(len(seq)-1): 
            combos_sorted.append(seq)
            combos_jump.append((jump))
    
    # if we decide to remove 0-1-2-3 sequences 
    #combos_sorted = combos_sorted[1:len(combos_sorted)-1]
    #combos_jump = combos_jump[1:len(combos_jump)-1]
    
    # function for calculating jumps 
    def count_steps(sequence):
        jump = []
        for j in range(1,len(sequence)):
            diff = abs(sequence[j-1]-sequence[j])
            jump.append(diff)
        return jump
                       
    # making a block of sequences 
    seqs = [combos_sorted[random.randint(0,len(combos_sorted)-1)]]
    seqs_jumps = [count_steps(seqs[0])]
    for i in range(trial_repetitions_in_block-1): 
        latest_seq = seqs[-1]
        seqs_end = latest_seq[-1]
        
        usable_combos = []
        for k in range(len(combos_sorted)):
            if combos_sorted[k] != seqs[-1]: 
                seqs_first = combos_sorted[k][0]
                if seqs_first!=seqs_end and abs(seqs_first-seqs_end)<=max_step:
                    usable_combos.append(combos_sorted[k])  
        
        # specify further rules to equal step jumps 
        if max_step > 1 :  
            jump_2s = len(np.concatenate(seqs_jumps)[np.concatenate(seqs_jumps) == 2])
            jump_1s = len(np.concatenate(seqs_jumps)[np.concatenate(seqs_jumps) == 1])
            
            if abs(jump_2s - jump_1s) >= 2 :
                u_combos = []
                for k in range(len(usable_combos)):
                    seqs_first = usable_combos[k][0]
                    u_comb_jumps = count_steps(usable_combos[k])
                    if (jump_2s - jump_1s) >= 2 : # if true, then most 2s 
                        jump_to_new = abs(seqs_first-seqs_end) 
                        if jump_to_new == 1 : u_combos.append(usable_combos[k])
                        elif sum(u_comb_jumps) <= 4 : u_combos.append(usable_combos[k])
                    
                    if (jump_1s - jump_2s) >= 2 : # if true, then most 1s
                        jump_to_new = abs(seqs_first-seqs_end) 
                        if jump_to_new == 2 : u_combos.append(usable_combos[k])
                        elif sum(u_comb_jumps) >= 5 : u_combos.append(usable_combos[k])
                        
                random_choice = u_combos[random.randint(0,len(u_combos)-1)]
                #print('used jumps to choose')
                #print(u_combos)
            else : 
                random_choice = usable_combos[random.randint(0,len(usable_combos)-1)]
                #print('random choice')
                
        seqs.append(random_choice)
        seqs_jumps.append([abs(seqs_end-random_choice[0])])
        seqs_jumps.append(count_steps(seqs[-1]))
    
    return np.concatenate(seqs)



#%%
def translate_to_target(seq, baseline_target, percent_change_from_baseline):
    change_factor = (percent_change_from_baseline/100)*baseline_target 
    targets = np.zeros(len(seq))
    unique_target = np.unique(seq)
    for i in range(len(seq)):
        if len(unique_target) == 3 :
            if seq[i] == 0 :  targets[i] = baseline_target - change_factor
            if seq[i] == 1 :  targets[i] = baseline_target 
            if seq[i] == 2 :  targets[i] = baseline_target + change_factor
    
        if len(unique_target) == 4 :
            if seq[i] == 0 :  targets[i] = baseline_target - change_factor
            if seq[i] == 1 :  targets[i] = baseline_target 
            if seq[i] == 2 :  targets[i] = baseline_target + change_factor
            if seq[i] == 3 :  targets[i] = baseline_target + change_factor*2
        
        if len(unique_target) == 5 :
            if seq[i] == 0 :  targets[i] = baseline_target - change_factor*2
            if seq[i] == 1 :  targets[i] = baseline_target - change_factor
            if seq[i] == 2 :  targets[i] = baseline_target 
            if seq[i] == 3 :  targets[i] = baseline_target + change_factor
            if seq[i] == 4 :  targets[i] = baseline_target + change_factor*2
    return targets 

     
#%%

# we have to start making it compatible to 9 triggers, so it must max be 4 levels
# and we cannot do decoupled blocks
# we should just send 2 triggers  
# # B A S D P 
# V: 1 2 3 4 5 
# H: 1 2 3 4 5  

# # settings things: 
# trial_repetitions_in_block = 5
# max_step = 2 # only 1 or 2
# no_of_levels = 5 # only 3,4,or 5
# baseline_target = 0.5
# percent_change_from_baseline = 0.33

# block_type = 'Symmetry_block'
# block_type = 'Asymmetry_block'
# block_type = 'Decoupled_block'

# sort_blocks = "Interleave" # OR "Random"

# jitter_time = 0.1
# trial_duration = 4.0
# baseline_block_duration = trial_repetitions_in_block*trial_duration
# initial_dur = 1
# time_between_blocks = 10
# no_of_blocks = [3,1,1,1] #  [no_of_B_blocks, no_of_S_blocks, no_of_A_blocks, no_of_D_blocks] 



# (conditions, durations, onsets, target_names) = get_RBD_block(no_of_blocks, sort_blocks, trial_repetitions_in_block, baseline_target, percent_change_from_baseline, max_step, no_of_levels, 
#                   jitter_time, trial_duration, baseline_block_duration, initial_dur, time_between_blocks)
    







#%% ##########################################################################
class CircleScene:
    ''' 
    @author: stoffer 
    modified by @author: Keenie Ayla
    '''
    def __init__(self,mywin):
        #import numpy,datetime,scipy.io,os,time
        import numpy as np
        from psychopy import visual
        #Draw vars
        self.textcol=(1,1,1)
        self.targetcol=(-1,-1,1) #(0.5,0.5,-1)
        self.forcecol= (0.7,0.3,-1) # (0.7,0.3,-1)
        self.forcecol0=(0.,0.,.0) # color when no-force 
        self.no_force_limit = 0.1
        self.forcecol1= (0.7,0.3,-1) #(1,1,-0.5) for colorshift close to target
        self.close_to_target_limit = 0.05
        self.mixcol=(0.6,0.4,-1)
        self.backcol=(0.,0.,.0)
        self.forceWidth=13 # linewidth of circle
        self.targetWidth=7 # linewidth of circle
        self.aspectrsc=float(mywin.size[0])/mywin.size[1]#scaling of the screen
        #Objects
        cres=50#defines visual feedback circle, KAA: changes nothing?
        cR=.5
        p=-np.linspace(0,2*np.pi,cres)+np.pi/2
        cc=np.vstack(((0,0),cR*np.array((np.cos(p),np.sin(p))).T))
        p1=np.linspace(-.5*np.pi,.5*np.pi,256)
        halfc1=np.vstack((np.cos(p1),np.sin(p1))).T*np.array((1./self.aspectrsc,1))[None,:]
        halfc2=np.vstack((-np.cos(p1),np.sin(p1))).T*np.array((1./self.aspectrsc,1))[None,:]
        interp=True
        aspectrsc=float(mywin.size[0])/mywin.size[1]
        self.circ1= visual.ShapeStim(win=mywin, units='norm', lineWidth=10.0, lineColor=None, lineColorSpace='rgb', fillColor=None,\
                fillColorSpace='rgb', vertices=halfc1, closeShape=False, pos=(0, 0), ori=0.0, opacity=1.0,\
                interpolate=interp)
        self.lin1= visual.ShapeStim(win=mywin, units='norm', lineWidth=10.0, lineColor=None, lineColorSpace='rgb', fillColor=None,\
                fillColorSpace='rgb', vertices=halfc1[[0,-1],:], closeShape=False, pos=(0, 0), ori=0.0, opacity=1.0,\
                interpolate=interp)
        self.circ2= visual.ShapeStim(win=mywin, units='norm', lineWidth=10.0, lineColor=None, lineColorSpace='rgb', fillColor=None,\
                fillColorSpace='rgb', vertices=halfc2, closeShape=False, pos=(0, 0), ori=0.0, opacity=1.0,\
                interpolate=interp)
        self.lin2= visual.ShapeStim(win=mywin, units='norm', lineWidth=10.0, lineColor=None, lineColorSpace='rgb', fillColor=None,\
                fillColorSpace='rgb', vertices=halfc2[[0,-1],:], closeShape=False, pos=(0, 0), ori=0.0, opacity=1.0,\
                interpolate=interp)
        self.fixation=visual.TextStim(mywin,text='+',color=(1,-1,-1),alignHoriz='center', alignVert='center')
        self.circle=visual.Circle(mywin,radius=(1./aspectrsc,1.),edges=512,lineColor=None,interpolate=False)
        self.circleline=visual.Circle(mywin,radius=(1./aspectrsc,1.),edges=512,lineColor=(0,0,0),interpolate=False,fillColor=None,lineWidth=3.)
        interp=False
        P1=.1*np.array(((-1, -1), (1, -1), (0, 1)))
        self.targetLeft=0.5
        self.targetRight=0.5
        self.left=0.5
        self.right=0.5
        
        self.txt=visual.TextStim(mywin,pos=(0,.9))
        
    
    def draw(self, sizes=None, targets=None):
        self.circ1.setLineWidth(self.forceWidth)
        self.circ1.setSize((self.right,self.right))
        self.lin1.setLineWidth(self.forceWidth)
        self.lin1.setSize((self.right,self.right))
        if self.right<self.no_force_limit :
            self.circ1.setColor(self.forcecol0,'rgb')
            self.lin1.setColor(self.forcecol0,'rgb')
        # elif abs(self.right-self.targetRight)<self.close_to_target_limit: 
        #     self.circ1.setColor(self.forcecol1,'rgb')
        #     self.lin1.setColor(self.forcecol1,'rgb')
        else : 
            self.circ1.setColor(self.forcecol,'rgb')
            self.lin1.setColor(self.forcecol,'rgb')
        self.circ1.draw()
        self.lin1.draw()

        self.circ2.setLineWidth(self.forceWidth)
        self.circ2.setSize((self.left,self.left))
        self.lin2.setLineWidth(self.forceWidth)
        self.lin2.setSize((self.left,self.left))
        if self.left<self.no_force_limit :
            self.circ2.setColor(self.forcecol0,'rgb')
            self.lin2.setColor(self.forcecol0,'rgb')
        # elif abs(self.left-self.targetLeft)<self.close_to_target_limit: 
        #     self.circ2.setColor(self.forcecol1,'rgb')
        #     self.lin2.setColor(self.forcecol1,'rgb')
        else :
            self.circ2.setColor(self.forcecol,'rgb')
            self.lin2.setColor(self.forcecol,'rgb')
        self.circ2.draw()
        self.lin2.draw()
        
        self.circ1.setLineWidth(self.targetWidth)
        self.circ1.setColor(self.targetcol,'rgb')
        self.circ1.setSize((self.targetRight,self.targetRight))
        self.circ1.draw()
        self.circ2.setLineWidth(self.targetWidth)
        self.circ2.setColor(self.targetcol,'rgb')
        self.circ2.setSize((self.targetLeft,self.targetLeft))
        self.circ2.draw()
        self.lin1.setLineWidth(self.targetWidth)
        self.lin1.setColor(self.targetcol,'rgb')
        self.lin1.setSize((self.targetRight,self.targetRight))
        self.lin1.draw()
        self.lin2.setLineWidth(self.targetWidth)
        self.lin2.setColor(self.targetcol,'rgb')
        self.lin2.setSize((self.targetLeft,self.targetLeft))
        self.lin2.draw()
        
        if self.targetRight == 0.01 :
            self.txt.setText('Pause')
            self.txt.draw()
            
        if self.targetRight == 0.013 :
            self.txt.setText('--- 3 ---')
            self.txt.draw()
            
        if self.targetRight == 0.012 :
            self.txt.setText('--- 2 ---')
            self.txt.draw()
            
        if self.targetRight == 0.011 :
            self.txt.setText('--- 1 ---')
            self.txt.draw()




