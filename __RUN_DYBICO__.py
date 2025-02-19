#!usr/bin/env python3 
# -*- coding: utf-8 -*-
""" DYBICO SOFTWARE ANNO 2021
PLEASE REFER TO THE README.md FILE IN THE DYBICO FOLDER FOR INSTRUCTIONS. 
# note the game has manually been modified to only work with Featherweight!  
# changes are made in MaxForceTest and the two main exp files, but the 
# need for manual change comes from aReader not working to manually detect 
# between Featherweight/Applejack as their port names differ. 
# the scaling size in MaxForceTest also has to be adjusted. 

# calibration files are used in MaxForceCalc, and the two main experiments
# where we integrate the calibration into reading v

# Note, software is modified to not send triggers to EEG, has to be manually enabled.

"""

#%% 
if __name__ == '__main__':
    import sys
    import os
    #from pathlib import Path
    
    ####################################################################
    # get path to script 
    path = os.path.split(os.path.abspath(sys.argv[0]))[0]    
    os.chdir(path)
        
    #####################################################################
    from PyQt5.QtWidgets import QApplication
    app = QApplication(sys.argv)

    #####################################################################
    import adv_gui
    window = adv_gui.MainWindow()
    window.show()
    
    #####################################################################
    sys.exit(app.exec_())
    exit() 
  
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
#%% 
    #####################################################################
    # installations automatized  K pandas version 1.2.4 before update , lab computer had 1.3.4 
    # if not os.path.exists('C:\\Users\%USERNAME%\Anaconda3\Lib\site-packages\psychopy'): 
    #     import subprocess
    #     subprocess.check_call([sys.executable, '-m', 'pip', 'install', 'psychopy==2021.2.3'])
    #     subprocess.check_call([sys.executable, '-m', 'pip', 'install', 'pyqt5==5.12.1'])
    #     subprocess.check_call([sys.executable, '-m', 'pip', 'install', 'pyqtwebengine==5.12.1'])
    #     # pip install mkl??
    # else: 
    #     print('packages already installed')