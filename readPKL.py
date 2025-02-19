# -*- coding: utf-8 -*-
"""
Created on Wed Jun 28 15:04:35 2023

@author: dzn332

Read pkl files 
"""

filepath = "C:/Users/dzn332/DYBICO/Settings/__Andreas_Retention_NoUni__.pkl"

filepath = "C:/Users/dzn332/DYBICO/Settings/CRB__new7conditions__.pkl"


filepath = "C:/Users/dzn332/DYBICO/Settings/__RESCALE1settings__.pkl"

import pandas as pd 
file=pd.read_pickle(filepath) # load file 

settings = file#['settings'][0]
settings_cond = settings.loc[:, ['Baseline_force', 'Left_increase_force', 'Left_decrease_force',
   'Right_increase_force', 'Right_decrease_force', 'Sym_increase_force',
   'Sym_decrease_force', 'Asym_L_increase_R_decrease',
   'Asym_L_decrease_R_increase']]
settings_ = settings.loc[:, ['no_of_blocks', 'time_between_blocks',
   'trial_repetitions', 'trial_duration', 'jitter_time',
   'baseline_between_trials', 'percent_change_from_baseline',
   'percent_of_maxforce', 'smoothing']]





