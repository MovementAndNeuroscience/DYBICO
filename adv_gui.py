# -*- coding: utf-8 -*-
"""
Created on Mon Oct  4 12:26:06 2021
@author: dzn332
"""
from PyQt5.QtWidgets import QMainWindow, QDialog, QSizePolicy
from PyQt5 import QtCore, QtWidgets
#from PyQt5.QtWidgets import QApplication
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
import os 
import sys 

class Ui_MainWindow:
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setGeometry(600, 200, 730, 290+40) # left, top, width, height
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setObjectName("label")  
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setObjectName("lineEdit")
        
        self.labelFW = QtWidgets.QLabel(self.centralwidget)
        self.labelFW.setObjectName("labelFW")  
        self.lineEditFW = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEditFW.setObjectName("lineEditFW")
        self.pushButtonFW = QtWidgets.QPushButton(self.centralwidget)
        self.pushButtonFW.setObjectName("pushButtonFW")
        self.label0FW = QtWidgets.QLabel(self.centralwidget)
        self.label0FW.setObjectName("label0FW") 
        
        self.pushButton1 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton1.setObjectName("pushButton1")
        self.label1 = QtWidgets.QLabel(self.centralwidget)
        self.label1.setObjectName("label1") 
        self.pushButton2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton2.setObjectName("pushButton2")
        self.label2 = QtWidgets.QLabel(self.centralwidget)
        self.label2.setObjectName("label2") 
        self.pushButton3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton3.setObjectName("pushButton3")
        self.label3 = QtWidgets.QLabel(self.centralwidget)
        self.label3.setObjectName("label3") 
        self.pushButton4 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton4.setObjectName("pushButton3")
        self.label4 = QtWidgets.QLabel(self.centralwidget)
        self.label4.setObjectName("label4") 
        self.pushButton5 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton5.setObjectName("pushButton5")
        self.label5 = QtWidgets.QLabel(self.centralwidget)
        self.label5.setObjectName("label5") 
        self.pushButton6 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton6.setObjectName("pushButton6")

        
        self.labelFW.setGeometry(QtCore.QRect(25, 30, 50, 30)) # left, top, width, height
        self.lineEditFW.setGeometry(QtCore.QRect(75, 30, 100, 30))
        self.pushButtonFW.setGeometry(QtCore.QRect(195+30, 30, 200, 30))
        self.label0FW.setGeometry(QtCore.QRect(405+30, 30, 200, 30))
        
        self.label.setGeometry(QtCore.QRect(25, 30+40, 50, 30)) # left, top, width, height
        self.lineEdit.setGeometry(QtCore.QRect(75, 30+40, 100, 30))
        
        self.pushButton1.setGeometry(QtCore.QRect(195+30, 30+40, 200, 30))
        self.pushButton2.setGeometry(QtCore.QRect(195+30, 70+40, 200, 30))
        self.pushButton3.setGeometry(QtCore.QRect(195+30, 110+40, 200, 30))
        self.pushButton4.setGeometry(QtCore.QRect(195+30, 150+40, 200, 30))
        self.pushButton5.setGeometry(QtCore.QRect(195+30, 190+40, 200, 30))
        self.pushButton6.setGeometry(QtCore.QRect(195+30, 230+40, 200, 30))
        self.label1.setGeometry(QtCore.QRect(405+30, 30+40, 200, 30))
        self.label2.setGeometry(QtCore.QRect(405+30, 70+40, 200, 30))
        self.label3.setGeometry(QtCore.QRect(405+30, 110+40, 200, 30))
        self.label4.setGeometry(QtCore.QRect(405+30, 150+40, 200, 30))
        self.label5.setGeometry(QtCore.QRect(405+30, 190+40, 200, 30))

        MainWindow.setCentralWidget(self.centralwidget)
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)


    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "DYBICO"))
        self.labelFW.setText(_translate("MainWindow", "Device:"))
        self.lineEditFW.setText(_translate("MainWindow", "Tom"))
        self.pushButtonFW.setText(_translate("MainWindow", "Get offset"))
        
        self.label.setText(_translate("MainWindow", "Log ID:"))
        self.lineEdit.setText(_translate("MainWindow", "test"))
        self.pushButton1.setText(_translate("MainWindow", "Create Log"))
        
        self.pushButton2.setText(_translate("MainWindow", "Run Maxforce Test"))
        self.pushButton3.setText(_translate("MainWindow", "Calculate Maxforce"))
        self.pushButton4.setText(_translate("MainWindow", "Run CRD Experiment"))
        self.pushButton5.setText(_translate("MainWindow", "Run RBD Experiment"))
        self.pushButton6.setText(_translate("MainWindow", "Exit"))
        
        self.label0FW.setText(_translate("MainWindow", "Offset must be calibrated"))
        self.label1.setText(_translate("MainWindow", "Log ID must be defined"))
        self.label2.setText(_translate("MainWindow", " "))
        self.label3.setText(_translate("MainWindow", "Must be measured or loaded"))
        self.label4.setText(_translate("MainWindow", " "))
        self.label5.setText(_translate("MainWindow", " "))

        
        

#%%
class Ui_Dialog1:
    def setupUi(self, Dialog1):
        Dialog1.setObjectName("Dialog1")
        Dialog1.setGeometry(700,200,550,290)  # left, top, width, height
        
        self.maxforceBox = QtWidgets.QWidget(Dialog1)
        self.maxforceBox.setObjectName("maxforceBox")
        self.maxforceBox.setWindowTitle("Calibrate Maxforce")
        
        self.label_mf0 = QtWidgets.QLabel(self.maxforceBox)
        self.label_mf0.setObjectName("label_mf0") 
        self.label_mf0.setText("Specify settings for maxforce testing:") 
        self.label_mf0.setGeometry(QtCore.QRect(25, 30, 350, 30))

        self.label_mf1 = QtWidgets.QLabel(self.maxforceBox)
        self.label_mf1.setObjectName("label_mf1")  
        self.lineEdit_mf1 = QtWidgets.QLineEdit(self.maxforceBox)
        self.lineEdit_mf1.setObjectName("lineEdit_mf1")       
    
        self.label_mf2 = QtWidgets.QLabel(self.maxforceBox)
        self.label_mf2.setObjectName("label_mf2")  
        self.lineEdit_mf2 = QtWidgets.QLineEdit(self.maxforceBox)
        self.lineEdit_mf2.setObjectName("lineEdit_mf2") 
    
        self.label_mf3 = QtWidgets.QLabel(self.maxforceBox)
        self.label_mf3.setObjectName("label_mf3")  
        self.lineEdit_mf3 = QtWidgets.QLineEdit(self.maxforceBox)
        self.lineEdit_mf3.setObjectName("lineEdit_mf3") 
    
        self.label_FSCR = QtWidgets.QLabel(self.maxforceBox)
        self.label_FSCR.setObjectName("label_5")
        self.lineEdit_FSCR = QtWidgets.QCheckBox(self.maxforceBox)
        self.lineEdit_FSCR.setObjectName("lineEdit_5") 
    
        self.label_mf1.setText("Trial duration: [seconds]") 
        self.lineEdit_mf1.setText("2") 
        self.label_mf1.setGeometry(QtCore.QRect(25, 70, 200, 30))
        self.lineEdit_mf1.setGeometry(QtCore.QRect(225, 70, 100, 30))
        
        self.label_mf2.setText("Scaling:") 
        self.lineEdit_mf2.setText("950") 
        self.label_mf2.setGeometry(QtCore.QRect(25, 110, 200, 30))
        self.lineEdit_mf2.setGeometry(QtCore.QRect(225, 110, 100, 30))
        
        self.label_mf3.setText("Smoothing") 
        self.lineEdit_mf3.setText("10") 
        self.label_mf3.setGeometry(QtCore.QRect(25, 150, 200, 30))
        self.lineEdit_mf3.setGeometry(QtCore.QRect(225, 150, 100, 30))
        
        self.label_FSCR.setText("fullscr?")
        self.lineEdit_FSCR.setChecked(True)
        self.label_FSCR.setGeometry(QtCore.QRect(25, 190, 50, 30))
        self.lineEdit_FSCR.setGeometry(QtCore.QRect(225, 190, 50, 30))
        
        self.pushButton_mf = QtWidgets.QPushButton(self.maxforceBox)
        self.pushButton_mf.setObjectName("pushButton_mf")
        self.pushButton_mf.setText("Calibrate Maxforce!")
        self.pushButton_mf.setGeometry(QtCore.QRect(110+80, 230, 150, 30)) # left, top, width, height
        
        # self.pushButton_Cancel = QtWidgets.QPushButton(self.maxforceBox)
        # self.pushButton_Cancel.setObjectName("pushButton_Cancel")
        # self.pushButton_Cancel.setText("Cancel")
        # self.pushButton_Cancel.setGeometry(QtCore.QRect(270, 190, 150, 30))
        
        QtCore.QMetaObject.connectSlotsByName(Dialog1)


class Ui_Dialog2:
    def setupUi(self, Dialog2):
        Dialog2.setObjectName("Dialog2")
        Dialog2.setGeometry(700,200,550,250)
        self.maxforceBox2 = QtWidgets.QMessageBox(Dialog2)
        self.maxforceBox2.setObjectName("maxforceBox2")
        self.maxforceBox2.setWindowTitle("Calculate Maxforce")
        self.maxforceBox2.setText("Continue in current log? y / n")
        self.maxforceBox2.setStandardButtons(QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No | QtWidgets.QMessageBox.Cancel)
        self.res=self.maxforceBox2.exec_()
        QtCore.QMetaObject.connectSlotsByName(Dialog2)


class Ui_Dialog3:
    def setupUi(self, Dialog3):
        Dialog3.setObjectName("Dialog3")
        Dialog3.setGeometry(650, 100, 1008, 720)
        self.maxforceBox3 = QtWidgets.QWidget(Dialog3)
        self.maxforceBox3.setObjectName("maxforceBox3")
        self.maxforceBox3.setWindowTitle("Maxforce")
        
        QtCore.QMetaObject.connectSlotsByName(Dialog3)
        
        
class Ui_Dialog4:
    def setupUi(self, Dialog4):
        Dialog4.setObjectName("Dialog4")
        Dialog4.setGeometry(700,200,550,250)
        self.maxforceBox4 = QtWidgets.QMessageBox(Dialog4)
        self.maxforceBox4.setObjectName("maxforceBox4")
        self.maxforceBox4.setWindowTitle("Maxforce is calculated")
        self.maxforceBox4.setText("Current maxforce calculations are plotted and saved. If unsatisfactory, delete selected files and re-collect maxforce files")
        self.maxforceBox4.setStandardButtons(QtWidgets.QMessageBox.Ok)
        res=self.maxforceBox4.exec_()
        if res == QtWidgets.QMessageBox.Ok:
                print('\n_____________________\n \n CURRENT MAXFORCE CALCULATIONS ARE PLOTTED AND SAVED. IF UNSATISFACTORY, DELETE SELECTED FILES AND RE-COLLECT MAXFORCE FILES  \n_____________________\n')
                self.maxforceBox4.close()
        QtCore.QMetaObject.connectSlotsByName(Dialog4)
        
        
# here one might insert Dialog5 with settings for CRD experiment
# class Ui_Dialog5: 
#     def setupUi(self, Dialog5): 
#         Dialog5.setObjectName("Dialog5")
#         Dialog5.setGeometry(700,200,550,250)
 

class Ui_Dialog6: 
    def setupUi(self, Dialog6):
        Dialog6.setObjectName("Dialog6")
        Dialog6.setGeometry(700,150,567,820)  # left, top, width, height
        self.settingsBox = QtWidgets.QWidget(Dialog6)
        self.settingsBox.setObjectName("settingsBox")
        self.settingsBox.setWindowTitle("Define RBD Experimental Settings")

        self.label_i0 = QtWidgets.QLabel(self.settingsBox)
        self.label_i0.setObjectName("label_i0") 
        self.label_i0.setText("The DYnamic BImanual COordination Game: Randomized Block Design ")       
        self.label_i1 = QtWidgets.QLabel(self.settingsBox)
        self.label_i1.setObjectName("label_i1") 
        self.label_i1.setText("Three ACTIVE tasks/movement contexts can be chosen: Symmetry, Inverted Asymmetry,") 
        self.label_i2 = QtWidgets.QLabel(self.settingsBox)
        self.label_i2.setObjectName("label_i2") 
        self.label_i2.setText("Decoupled Asymmetry, supplemented by a STATIONARY Baseline force on both hands.") 
        self.label_i3 = QtWidgets.QLabel(self.settingsBox)
        self.label_i3.setObjectName("label_i3") 
        self.label_i3.setText("These are denoted >conditions< and presented in >trials<. There are several trial-types") 
        self.label_i4 = QtWidgets.QLabel(self.settingsBox)
        self.label_i4.setObjectName("label_i4") 
        self.label_i4.setText("per condition, e.g. Symmetric force-level A, force-level B, ect.") 
        self.label_i5 = QtWidgets.QLabel(self.settingsBox)
        self.label_i5.setObjectName("label_i5") 
        self.label_i5.setText("No. of force levels can be 5 [A<B<C<D<E], 4 [B<C<D<E] or 3 [B<C<D]. Force level [C] ")   
        self.label_i6 = QtWidgets.QLabel(self.settingsBox)
        self.label_i6.setObjectName("label_i6") 
        self.label_i6.setText("represents baseline force, and can be adjusted to a given percentage of the MaxForce.") 
        self.label_i7 = QtWidgets.QLabel(self.settingsBox)
        self.label_i7.setObjectName("label_i7") 
        self.label_i7.setText("The difference between force levels is adjusted as a percentage of the baseline level")
        self.label_i8 = QtWidgets.QLabel(self.settingsBox)
        self.label_i8.setObjectName("label_i7") 
        self.label_i8.setText("The size of target circle at baseline level is relative to the window (recommended 0.45).") 
        self.label_i9 = QtWidgets.QLabel(self.settingsBox)
        self.label_i9.setObjectName("label_i7") 
        self.label_i9.setText("Settings are saved and can be re-loaded for replication.")
        
        ##
        self.label_0 = QtWidgets.QLabel(self.settingsBox)
        self.label_0.setObjectName("label_0") 
        self.label_0.setText("Define Movement Context Blocks") 
        self.label_1 = QtWidgets.QLabel(self.settingsBox)
        self.label_1.setObjectName("label_1")  
        self.label_1.setText("Number of Active Symmetric Blocks:") 
        self.lineEdit_1 = QtWidgets.QLineEdit(self.settingsBox)
        self.lineEdit_1.setObjectName("lineEdit_1")    
        self.lineEdit_1.setText("6") 
        self.label_2 = QtWidgets.QLabel(self.settingsBox)
        self.label_2.setObjectName("label_2")  
        self.label_2.setText("Number of Active Mirror-Asym Blocks:") 
        self.lineEdit_2 = QtWidgets.QLineEdit(self.settingsBox)
        self.lineEdit_2.setObjectName("lineEdit_2") 
        self.lineEdit_2.setText("6") 
        self.label_3 = QtWidgets.QLabel(self.settingsBox)
        self.label_3.setObjectName("label_3")  
        self.label_3.setText("Number of Active Decoupled Blocks:") 
        self.lineEdit_3 = QtWidgets.QLineEdit(self.settingsBox)
        self.lineEdit_3.setObjectName("lineEdit_3") 
        self.lineEdit_3.setText("0") 
        self.label_4 = QtWidgets.QLabel(self.settingsBox)
        self.label_4.setObjectName("label_4")  
        self.label_4.setText("Number of Baseline Blocks:") 
        self.lineEdit_4 = QtWidgets.QLineEdit(self.settingsBox)
        self.lineEdit_4.setObjectName("lineEdit_4") 
        self.lineEdit_4.setText("2") 
        self.label_5 = QtWidgets.QLabel(self.settingsBox)
        self.label_5.setObjectName("label_5")  
        self.label_5.setText("Interleave w. Random Initial Active Block:") 
        self.lineEdit_5 = QtWidgets.QCheckBox(self.settingsBox)
        self.lineEdit_5.setObjectName("lineEdit_5") 
        self.lineEdit_5.setChecked(True)
        self.label_5b = QtWidgets.QLabel(self.settingsBox)
        self.label_5b.setObjectName("label_5b") 
        self.label_5b.setText("(if disabled, the sequence will be permuted amongst all four conditions)") 
        
        ## 
        self.label_00 = QtWidgets.QLabel(self.settingsBox)
        self.label_00.setObjectName("label_00") 
        self.label_00.setText("Define Target Force Levels")   
        self.label_11 = QtWidgets.QLabel(self.settingsBox)
        self.label_11.setObjectName("label_11")  
        self.label_11.setText("Target circle size at baseline [0-1]:") 
        self.lineEdit_11 = QtWidgets.QLineEdit(self.settingsBox)
        self.lineEdit_11.setObjectName("lineEdit_11")    
        self.lineEdit_11.setText("0.45") 
        self.label_22 = QtWidgets.QLabel(self.settingsBox)
        self.label_22.setObjectName("label_22")  
        self.label_22.setText("Number of force levels [3, 4 or 5]:") 
        self.lineEdit_22 = QtWidgets.QLineEdit(self.settingsBox)
        self.lineEdit_22.setObjectName("lineEdit_22") 
        self.lineEdit_22.setText("4") 
        self.label_33 = QtWidgets.QLabel(self.settingsBox)
        self.label_33.setObjectName("label_33")  
        self.label_33.setText("Percent of maxforce to reach baseline [%]:") 
        self.lineEdit_33 = QtWidgets.QLineEdit(self.settingsBox)
        self.lineEdit_33.setObjectName("lineEdit_33") 
        self.lineEdit_33.setText("5") 
        self.label_44 = QtWidgets.QLabel(self.settingsBox)
        self.label_44.setObjectName("label_44")  
        self.label_44.setText("Force-level change [% of baseline]:") 
        self.lineEdit_44 = QtWidgets.QLineEdit(self.settingsBox)
        self.lineEdit_44.setObjectName("lineEdit_44") 
        self.lineEdit_44.setText("50") 
        self.label_55 = QtWidgets.QLabel(self.settingsBox)
        self.label_55.setObjectName("label_55")  
        self.label_55.setText("Maximum jump between force levels [int 1-3]:") 
        self.lineEdit_55 = QtWidgets.QLineEdit(self.settingsBox)
        self.lineEdit_55.setObjectName("lineEdit_55") 
        self.lineEdit_55.setText("3") 
        self.label_66 = QtWidgets.QLabel(self.settingsBox)
        self.label_66.setObjectName("label_66")  
        self.label_66.setText("Smoothing of visual feedback [samples]:") 
        self.lineEdit_66 = QtWidgets.QLineEdit(self.settingsBox)
        self.lineEdit_66.setObjectName("lineEdit_66") 
        self.lineEdit_66.setText("10") 
        
        ## 
        self.label_000 = QtWidgets.QLabel(self.settingsBox)
        self.label_000.setObjectName("label_000") 
        self.label_000.setText("Define Session Composition")   
        self.label_111 = QtWidgets.QLabel(self.settingsBox)
        self.label_111.setObjectName("label_111")  
        self.label_111.setText("Repetitions of unique conditions within block:") 
        self.lineEdit_111 = QtWidgets.QLineEdit(self.settingsBox)
        self.lineEdit_111.setObjectName("lineEdit_111")    
        self.lineEdit_111.setText("5") 
        self.label_222 = QtWidgets.QLabel(self.settingsBox)
        self.label_222.setObjectName("label_222")  
        self.label_222.setText("Trial duration [seconds]:") 
        self.lineEdit_222 = QtWidgets.QLineEdit(self.settingsBox)
        self.lineEdit_222.setObjectName("lineEdit_222") 
        self.lineEdit_222.setText("2") 
        self.label_333 = QtWidgets.QLabel(self.settingsBox)
        self.label_333.setObjectName("label_333")  
        self.label_333.setText("Jitter time [seconds]:") 
        self.lineEdit_333 = QtWidgets.QLineEdit(self.settingsBox)
        self.lineEdit_333.setObjectName("lineEdit_333") 
        self.lineEdit_333.setText("0.1") 
        self.label_444 = QtWidgets.QLabel(self.settingsBox)
        self.label_444.setObjectName("label_444")  
        self.label_444.setText("Pause between blocks [seconds]:") 
        self.lineEdit_444 = QtWidgets.QLineEdit(self.settingsBox)
        self.lineEdit_444.setObjectName("lineEdit_444") 
        self.lineEdit_444.setText("5") # plus 3 sec dountdown 
        self.label_555 = QtWidgets.QLabel(self.settingsBox)
        self.label_555.setObjectName("label_555")  
        self.label_555.setText("Baseline block duration [seconds]:") 
        self.lineEdit_555 = QtWidgets.QLineEdit(self.settingsBox)
        self.lineEdit_555.setObjectName("lineEdit_555") 
        self.lineEdit_555.setText("20") 
    
        self.pushButton_RUN = QtWidgets.QPushButton(self.settingsBox)
        self.pushButton_RUN.setObjectName("pushButton_RUN")
        self.pushButton_RUN.setText("Run Experiment!")
        #self.pushButton_Cancel = QtWidgets.QPushButton(self.settingsBox)
        #self.pushButton_Cancel.setObjectName("pushButton_Cancel")
        #self.pushButton_Cancel.setText("Cancel")
        
        ## define postions 
        self.label_i0.setGeometry(QtCore.QRect(15, 10, 535, 15))
        self.label_i1.setGeometry(QtCore.QRect(15, 30, 535, 15))
        self.label_i2.setGeometry(QtCore.QRect(15, 45, 535, 15))
        self.label_i3.setGeometry(QtCore.QRect(15, 60, 535, 15))
        self.label_i4.setGeometry(QtCore.QRect(15, 75, 535, 15))
        self.label_i5.setGeometry(QtCore.QRect(15, 90, 535, 15))
        self.label_i6.setGeometry(QtCore.QRect(15, 105, 535, 15))
        self.label_i7.setGeometry(QtCore.QRect(15, 120, 535, 15))
        self.label_i8.setGeometry(QtCore.QRect(15, 135, 535, 15))
        self.label_i9.setGeometry(QtCore.QRect(15, 150, 535, 15))

        ## # left, top, width, height
        i=160
        j=70
        self.label_0.setGeometry(QtCore.QRect(5+j, 15+i, 350, 25))
        self.label_1.setGeometry(QtCore.QRect(25+j, 40+i, 270, 25))
        self.lineEdit_1.setGeometry(QtCore.QRect(295+j, 40+i, 100, 25))
        self.label_2.setGeometry(QtCore.QRect(25+j, 70+i, 270, 25))
        self.lineEdit_2.setGeometry(QtCore.QRect(295+j, 70+i, 100, 25))
        self.label_3.setGeometry(QtCore.QRect(25+j, 100+i, 270, 25))
        self.lineEdit_3.setGeometry(QtCore.QRect(295+j, 100+i, 100, 25))
        self.label_4.setGeometry(QtCore.QRect(25+j, 130+i, 270, 25))
        self.lineEdit_4.setGeometry(QtCore.QRect(295+j, 130+i, 100, 25))
        self.label_5.setGeometry(QtCore.QRect(25+j, 160+i, 270, 25))
        self.lineEdit_5.setGeometry(QtCore.QRect(295+j, 160+i, 100, 25))
        self.label_5b.setGeometry(QtCore.QRect(25+j, 180+i, 500+100, 25))
        ##
        self.label_00.setGeometry(QtCore.QRect(5+j, 215+i, 350, 25))
        self.label_11.setGeometry(QtCore.QRect(25+j, 240+i, 270, 25))
        self.lineEdit_11.setGeometry(QtCore.QRect(295+j, 240+i, 100, 25))
        self.label_22.setGeometry(QtCore.QRect(25+j, 270+i, 270, 25))
        self.lineEdit_22.setGeometry(QtCore.QRect(295+j, 270+i, 100, 25))
        self.label_33.setGeometry(QtCore.QRect(25+j, 300+i, 270, 25))
        self.lineEdit_33.setGeometry(QtCore.QRect(295+j, 300+i, 100, 25))
        self.label_44.setGeometry(QtCore.QRect(25+j, 330+i, 270, 25))
        self.lineEdit_44.setGeometry(QtCore.QRect(295+j, 330+i, 100, 25))
        self.label_55.setGeometry(QtCore.QRect(25+j, 360+i, 270, 25))
        self.lineEdit_55.setGeometry(QtCore.QRect(295+j, 360+i, 100, 25))
        self.label_66.setGeometry(QtCore.QRect(25+j, 390+i, 270, 25))
        self.lineEdit_66.setGeometry(QtCore.QRect(295+j, 390+i, 100, 25))
        ##
        self.label_000.setGeometry(QtCore.QRect(5+j, 425+i, 350, 25))
        self.label_111.setGeometry(QtCore.QRect(25+j, 450+i, 270, 25))
        self.lineEdit_111.setGeometry(QtCore.QRect(295+j, 450+i, 100, 25))
        self.label_222.setGeometry(QtCore.QRect(25+j, 480+i, 270, 25))
        self.lineEdit_222.setGeometry(QtCore.QRect(295+j, 480+i, 100, 25))
        self.label_333.setGeometry(QtCore.QRect(25+j, 510+i, 270, 25))
        self.lineEdit_333.setGeometry(QtCore.QRect(295+j, 510+i, 100, 25))
        self.label_444.setGeometry(QtCore.QRect(25+j, 540+i, 270, 25))
        self.lineEdit_444.setGeometry(QtCore.QRect(295+j, 540+i, 100, 25))
        self.label_555.setGeometry(QtCore.QRect(25+j, 570+i, 270, 25))
        self.lineEdit_555.setGeometry(QtCore.QRect(295+j, 570+i, 100, 25))
        
        self.pushButton_RUN.setGeometry(QtCore.QRect(150+70, 610+i, 130, 30))
        #self.pushButton_Cancel.setGeometry(QtCore.QRect(290, 610+i, 130, 30))
                
        QtCore.QMetaObject.connectSlotsByName(Dialog6)
        # left, top, width, height


#%% 
class RBSSettingsDialog(QDialog):
    def __init__(self, parent=None):
        super(RBSSettingsDialog, self).__init__(parent)
        self.ui = Ui_Dialog6()
        self.ui.setupUi(self)
        self.ui.pushButton_RUN.clicked.connect(self.return_input)
        #self.ui.pushButton_Cancel.clicked.connect(self.close)
        
    def return_input(self):
        import pandas as pd
        self.tasks = pd.DataFrame()
        self.tasks['Symmetry_blocks'] = [self.ui.lineEdit_1.text()]
        self.tasks['Asymmetry_blocks'] = [self.ui.lineEdit_2.text()]
        self.tasks['Decoupled_blocks'] = [self.ui.lineEdit_3.text()]
        self.tasks['Baseline_blocks'] = [self.ui.lineEdit_4.text()]
        if self.ui.lineEdit_5.isChecked()==True: self.tasks['Interleaved'] = ['Y']
        elif self.ui.lineEdit_5.isChecked()!=True: self.tasks['Interleaved'] = ['N']
        
        self.settings_ = pd.DataFrame()
        self.settings_ = self.tasks.copy()
        self.settings_['no_of_S_blocks'] = [self.ui.lineEdit_1.text()]
        self.settings_['no_of_A_blocks'] = [self.ui.lineEdit_2.text()]
        self.settings_['no_of_D_blocks'] = [self.ui.lineEdit_3.text()]
        self.settings_['no_of_B_blocks'] = [self.ui.lineEdit_4.text()]
        if self.ui.lineEdit_5.isChecked()==True: self.settings_['sort_blocks'] = ["Interleave"]
        elif self.ui.lineEdit_5.isChecked()!=True: self.settings_['sort_blocks'] = ["Random"]
        
        self.settings_['baseline_target'] = [self.ui.lineEdit_11.text()]
        self.settings_['no_of_levels'] = [self.ui.lineEdit_22.text()]
        self.settings_['percent_of_maxforce'] = [self.ui.lineEdit_33.text()]
        self.settings_['percent_change_from_baseline'] = [self.ui.lineEdit_44.text()]
        self.settings_['max_step'] = [self.ui.lineEdit_55.text()]
        self.settings_['smoothing'] = [self.ui.lineEdit_66.text()]
        
        self.settings_['trial_repetitions_in_block'] = [self.ui.lineEdit_111.text()]
        self.settings_['trial_duration'] = [self.ui.lineEdit_222.text()]
        self.settings_['jitter_time'] = [self.ui.lineEdit_333.text()]
        self.settings_['time_between_blocks'] = [self.ui.lineEdit_444.text()]
        self.settings_['baseline_block_duration'] = [self.ui.lineEdit_555.text()]

        self.hide()
        return self.settings_
           



class MaxforceDialog(QDialog):
    def __init__(self, parent=None):
        super(MaxforceDialog, self).__init__(parent)
        self.ui = Ui_Dialog1()
        self.ui.setupUi(self)
        self.ui.pushButton_mf.clicked.connect(self.return_input)

    def return_input(self):
        self.test_duration = self.ui.lineEdit_mf1.text()
        self.scaling_size = self.ui.lineEdit_mf2.text()
        self.smoothing = self.ui.lineEdit_mf3.text()
        if self.ui.lineEdit_FSCR.isChecked()==True: self.dofullscr = True
        elif self.ui.lineEdit_FSCR.isChecked()!=True: self.dofullscr = False
        self.hide()
        
        return [self.test_duration, self.scaling_size, self.smoothing, self.dofullscr]
    

    

class MaxforceCalcDialog(QDialog):
    def __init__(self, parent=None):
        super(MaxforceCalcDialog, self).__init__(parent)
        self.ui = Ui_Dialog2()
        self.ui.setupUi(self)
        
    def run_it(self):
        import os 
        res = self.ui.res
        from psychopy import event
        keys=event.getKeys()
        if res == QtWidgets.QMessageBox.Yes or len(keys)>0 and keys[0] == 'y': run="this"
        if res == QtWidgets.QMessageBox.No or len(keys)>0 and keys[0] == 'n': run="new"
        if res == QtWidgets.QMessageBox.Cancel or len(keys)>0 and keys[0] == 'q': run="none"
            # self.hide()
        print('\n_____________________\n \n WORKING IN: %s  \n_____________________\n' %os.getcwd()) # fix path
        self.hide() 
        return run 
    
    
class MaxforcePlot(QDialog):
    def __init__(self, parent=None):
        super(MaxforcePlot, self).__init__(parent)
        self.ui = Ui_Dialog3()
        self.ui.setupUi(self)
        m = PlotCanvas(self)
        m.move(0,0)
        self.ui = Ui_Dialog4()
        self.ui.setupUi(self)
        #self.show()


class PlotCanvas(FigureCanvas):
    def __init__(self, parent=None, dpi=100):
        import matplotlib
        matplotlib.use('Qt5Agg')
        import matplotlib.pyplot as plt
        self.fig, self.axs = plt.subplots(2)
        self.fig.set_size_inches(14, 10)
        FigureCanvas.__init__(self, self.fig)
        self.setParent(parent)
        FigureCanvas.setSizePolicy(self,QSizePolicy.Expanding,QSizePolicy.Expanding)
        FigureCanvas.updateGeometry(self)
        self.plot()  
        
    def plot(self):
        import numpy as np 
        import pickle    
        (maxforce, MaxL, MaxR, tL, rawL, tR, rawR, QL1, QL2, QL3, QR1, QR2, QR3, upper)=pickle.load(open('maxforce.pkl', "rb"), encoding="latin1")  # fix path
        
        Q=upper*100
        styles=['-','--',':']
        colors=['r','y']
        LW=2
        lw=3 
        remove = 0.5 # remove initial 500ms
        #t_remove = int(60*0.4)
        xmin = remove/max(tL[0])
        xmax = 2.5/max(tL[0])
        
        self.axs[0].axhspan(0, MaxL,xmin,xmax, color='0.2', alpha=0.1)
        self.axs[0].plot(tL[0],rawL[0],label="Test 1",color=colors[1],linestyle=styles[0],linewidth=lw)
        self.axs[0].axhline(QL1[1],xmin,xmax, label=".%.f Upper Quantile"%Q, color='k', alpha=0.5,linewidth=LW,linestyle=styles[0])
        self.axs[0].plot(tL[1],rawL[1],label="Test 2",color=colors[1],linestyle=styles[1],linewidth=lw)
        self.axs[0].axhline(QL2[1],xmin,xmax, label=".%.f Upper Quantile"%Q,color='k', alpha=0.5,linewidth=LW,linestyle=styles[1])
        self.axs[0].plot(tL[2],rawL[2],label="Test 3",color=colors[1],linestyle=styles[2],linewidth=lw)
        self.axs[0].axhline(QL3[1],xmin,xmax, label=".%.f Upper Quantile"%Q,color='k', alpha=0.5,linewidth=LW,linestyle=styles[2])
        self.axs[0].axhline(MaxL,xmin,xmax, label="Maxforce", color=colors[1], alpha=0.5,linewidth=lw,linestyle=styles[0])
        self.axs[0].set_title('Left hand max force [%.2f kg]'%(maxforce[1]/1000)) #*0.009807 # made to newton
        self.axs[0].legend(loc='lower right', ncol=4)
        self.axs[0].set_ylabel('[a.u.]')
        
        self.axs[1].axhspan(0, MaxR,xmin,xmax, color='0.2', alpha=0.1)
        self.axs[1].plot(tR[0],rawR[0],label="Test 1",color=colors[0],linestyle=styles[0],linewidth=lw)
        self.axs[1].axhline(QR1[1],xmin,xmax, label=".%.f Upper Quantile"%Q, color='k', alpha=0.5,linewidth=LW,linestyle=styles[0])
        self.axs[1].plot(tR[1],rawR[1],label="Test 2",color=colors[0],linestyle=styles[1],linewidth=lw)
        self.axs[1].axhline(QR2[1],xmin,xmax, label=".%.f Upper Quantile"%Q, color='k', alpha=0.5,linewidth=LW,linestyle=styles[1])
        self.axs[1].plot(tR[2],rawR[2],label="Test 3",color=colors[0],linestyle=styles[2],linewidth=lw)
        self.axs[1].axhline(QR3[1],xmin,xmax, label=".%.f Upper Quantile"%Q, color='k', alpha=0.5,linewidth=LW,linestyle=styles[2])
        self.axs[1].axhline(MaxR,xmin,xmax, label="Maxforce", color=colors[0], alpha=0.5,linewidth=lw,linestyle=styles[0])
        self.axs[1].set_title('Right hand max force [%.2f kg]'%(maxforce[0]/1000)) 
        self.axs[1].legend(loc='lower right',ncol=4)
        self.axs[1].set_ylabel('[a.u.]')
        
        self.axs[0].set_xlabel('Seconds')
        self.axs[1].set_xlabel('Seconds')
        
        maxT=max([max([max(i) for i in tL]),max([max(i) for i in tR])])
        self.axs[0].set_xlim(0,maxT) # min([min(i) for i in tL])-0.1, max([max(i) for i in tL])+0.1
        self.axs[1].set_xlim(0,maxT) # min([min(i) for i in tR])-0.1, max([max(i) for i in tR])+0.1
        self.axs[0].set_xticks(np.arange(0,maxT,1)) 
        self.axs[1].set_xticks(np.arange(0,maxT,1)) 
        
        #self.fig.set_size_inches(14, 10)
        self.fig.savefig('MaxForces.png', dpi=100) # fix path
        self.fig.tight_layout()
        
        self.draw()





#%%
class helpers:
    def __init__(self, parent=None):
        super(helpers, self).__init__(parent)
        
    def save_log(logno): 
        import os 
        import sys
        path = os.path.split(os.path.abspath(sys.argv[0]))[0]
        
        import datetime, time 
        timestamp=time.time()
        timestamp_readable=datetime.datetime.fromtimestamp(timestamp).strftime('%Y%m%d')
        print('\n_____________________\n \n LOG CREATED: %s %s \n_____________________\n' %(logno, timestamp_readable))    
     
        datapath=os.path.join(path,'DATA') 
        if not os.path.exists(datapath): os.makedirs(datapath) 
        
        log_ID = str(timestamp_readable+'_'+logno)
        logdir=os.path.join(datapath,log_ID) 
        if not os.path.exists(logdir): os.makedirs(logdir)
        
        mfdir=os.path.join(logdir,'Maxforce')
        if not os.path.exists(mfdir): os.makedirs(mfdir)
        
        print('\n_____________________\n \n FOLDERS CREATED: %s  \n_____________________\n' %logdir)
        return logdir
        ############################
    
    
    def loop_maxforce(logdir, test_duration, scaling_size, smoothing, dofullscr, offset):
        import os 
        import fnmatch 
        import MaxForceTest as MFT 
        from psychopy import event 
    
        L_reps=len(fnmatch.filter(os.listdir(os.path.join(logdir,'Maxforce')), 'maxforceL*'))
        R_reps=len(fnmatch.filter(os.listdir(os.path.join(logdir,'Maxforce')), 'maxforceR*'))
                        
        stoploop = False 
        keys=event.getKeys()
        while not stoploop:
            L_reps=len(fnmatch.filter(os.listdir(os.path.join(logdir,'Maxforce')), 'maxforceL*'))
            R_reps=len(fnmatch.filter(os.listdir(os.path.join(logdir,'Maxforce')), 'maxforceR*'))
            
            if L_reps<3 :  
                print('\n_____________________\n \n COLLECTING LEFT-HAND MAXFORCE FILES  \n_____________________\n')
                hand='L'
                MFT.run_maxforce(logdir, hand, test_duration, scaling_size, smoothing, dofullscr, offset) 
            if R_reps<3 :  
                print('\n_____________________\n \n COLLECTING RIGHT-HAND MAXFORCE FILES  \n_____________________\n')
                hand='R'
                MFT.run_maxforce(logdir, hand, test_duration, scaling_size, smoothing, dofullscr, offset) 
            if L_reps>=3 and R_reps>=3:
                print('\n_____________________\n \n MAXFORCE CALIBRATION FILES EXISTS IN FOLDER  \n_____________________\n')
                stoploop=True 
            
            # MANUALLY END EXPERIMENT
            keys=event.getKeys()
            if len(keys)>0:
                if keys[0] == 'q':
                    stoploop = True   
    
    
    def calc_max(logdir, FW, run):  
        import os 
        import fnmatch
        import MaxForceCalc as MFCalc
        import numpy as np
        import pickle
        
        if run == 'this':
            print('\n_____________________\n \n WORKING IN: %s  \n_____________________\n' %logdir) 
            mfdir = os.path.join(logdir,'Maxforce')
        if run == 'new':
            logdir = QtWidgets.QFileDialog.getExistingDirectory(None,'Select LOG Folder')
            print('\n_____________________\n \n WORKING IN: %s  \n_____________________\n' %logdir)
            mfdir = os.path.join(logdir,'Maxforce')
        
        print(mfdir)
        L_reps=len(fnmatch.filter(os.listdir(mfdir), 'maxforceL*'))
        R_reps=len(fnmatch.filter(os.listdir(mfdir), 'maxforceR*'))
        if L_reps<3 and R_reps<3:
            print('\n_____________________\n \n NOT ENOUGH MAXFORCE CALIBRATION FILES  \n_____________________\n')
            (maxforce, MaxL, MaxR, tL, rawL, tR, rawR, QL1, QL2, QL3, QR1, QR2, QR3, upper) = [] 
            
        else:
            (maxforce, MaxL, MaxR, tL, rawL, tR, rawR, QL1, QL2, QL3, QR1, QR2, QR3, upper) = MFCalc.calc_maxforce(logdir, mfdir, FW) # to save or not to save 
            save_it=np.array((maxforce, MaxL, MaxR, tL, rawL, tR, rawR, QL1, QL2, QL3, QR1, QR2, QR3, upper), dtype=object)
            pickle.dump(save_it,open(os.path.join(mfdir,'maxforce.pkl'),"wb"))

        return maxforce 
    
    
   


#%% 
# file main.py

class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self) 
        self.ui.pushButtonFW.clicked.connect(self.activate_tab_0FW)
        self.ui.pushButton1.clicked.connect(self.activate_tab_1)
        self.ui.pushButton2.clicked.connect(self.activate_tab_2)
        self.ui.pushButton3.clicked.connect(self.activate_tab_3)
        self.ui.pushButton4.clicked.connect(self.activate_tab_4)
        self.ui.pushButton5.clicked.connect(self.activate_tab_5)
        self.ui.pushButton6.clicked.connect(self.close)
        #import sys
        #self.ui.pushButton5.clicked.connect(sys.exit)
    
    def activate_tab_0FW(self):
        #self.hide()
        self.FWchoice = self.ui.lineEditFW.text()
        self.FW = str(self.FWchoice) 
        ############################
        from  psychopy import core
        import numpy as np
        import aReader_KAA as aReader 
        pico=aReader.aReader(debug=False,dump=None)
        
        t0offset=core.Clock()
        while t0offset.getTime() < 3 : 
            print('offset calibration, please wait...')
        offset = np.mean(pico.getValues(10)[:,1:],axis=0)[None]
        print('offset set to :')
        print(offset)   
        pico.stop()
        del pico
        self.offset = offset
        
        ############################
        self.ui.label0FW.setText("Device and offset registered!")
        self.show()

    def activate_tab_1(self):
        import numpy as np 
        import pickle 
        #self.hide()
        self.loginput = self.ui.lineEdit.text()
        ############################
        logno = str(self.loginput)
        self.logdir = helpers.save_log(logno)
        
        save_offset=np.array(self.offset, dtype=object)
        pickle.dump(save_offset,open(os.path.join(self.logdir,'offset.pkl'),"wb"))
        ############################
        self.ui.label1.setText("Log is defined!")
        self.show()
        

    def activate_tab_2(self):
        self.hide() 
        #####################
        mfd = MaxforceDialog(parent=self)
        mfd.exec_()
        [self.test_duration, self.scaling_size, self.smoothing, self.dofullscr] = mfd.return_input()                
        helpers.loop_maxforce(self.logdir, int(self.test_duration), int(self.scaling_size), int(self.smoothing), self.dofullscr, self.offset)  
        
        #####################
        self.ui.label2.setText("Maxforce files exists in folder!")
        self.show()
    

    def activate_tab_3(self):
        self.hide()
        ######################
        mfd2 = MaxforceCalcDialog(parent=self)
        run = mfd2.run_it()
        import os 
        import sys 
        if run != "none": 
            self.maxforce = helpers.calc_max(self.logdir, self.FW, run)
            os.chdir(os.path.join(self.logdir,'Maxforce')) # gotta keep this chdir bc of plot
            MaxforcePlot(parent=self)
            self.ui.label3.setText("Maxforce is calculated!")
            self.path = os.path.split(os.path.abspath(sys.argv[0]))[0]    
            os.chdir(self.path) # gotta keep this chdir as well, but now set to go back proper.
        self.show()
    
    
    def activate_tab_4(self):
        self.hide()
        self.path = os.path.split(os.path.abspath(sys.argv[0]))[0] 
        ######################
        import pandas as pd
        from PyQt5 import QtWidgets
        from psychopy import event
        QtWidgets.QApplication(sys.argv)
        msgBox = QtWidgets.QMessageBox(text="Load experimental CRD settings from a file?")
        msgBox.setStandardButtons(QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.Cancel)
        msgBox.addButton("Define new", QtWidgets.QMessageBox.AcceptRole)
        msgBox.setDefaultButton(QtWidgets.QMessageBox.StandardButton.Yes)
        res = msgBox.exec_()  
        keys=event.getKeys()
        
        if res == QtWidgets.QMessageBox.Yes or len(keys)>0 and keys[0] == 'y':
            filedir = QtWidgets.QFileDialog.getOpenFileName(None,'Select .pkl file with CRD experimental settings')
            self.settings = pd.read_pickle(filedir[0])
            
        if res == QtWidgets.QMessageBox.AcceptRole:
            import Helpers as kaah
            self.settings = kaah.define_settings_CRD(self.logdir)
            
        if res == QtWidgets.QMessageBox.Cancel or len(keys)>0 and keys[0] == 'q':
            msgBox.hide()
            self.settings="none"
        
        
        print(type(self.settings))
        if type(self.settings) != 'str':
            import MainExperiment_CRD as MainExperiment_CRD
            MainExperiment_CRD.run_it(self.settings, self.path, self.logdir, self.maxforce, self.FW)
            ######################
            self.ui.label4.setText("CRD Experiment is done!")
        self.show()
        
        
    def activate_tab_5(self):
        self.hide()
        self.path = os.path.split(os.path.abspath(sys.argv[0]))[0] 
        ######################
        import pandas as pd
        from PyQt5 import QtWidgets
        from psychopy import event
        QtWidgets.QApplication(sys.argv)
        msgBox = QtWidgets.QMessageBox(text="Load experimental RBD settings from a file?")
        msgBox.setStandardButtons(QtWidgets.QMessageBox.Yes )#| QtWidgets.QMessageBox.Cancel)
        msgBox.addButton("Define new", QtWidgets.QMessageBox.AcceptRole)
        msgBox.setDefaultButton(QtWidgets.QMessageBox.StandardButton.Yes)
        res = msgBox.exec_()  
        keys=event.getKeys()
    
        if res == QtWidgets.QMessageBox.Yes or len(keys)>0 and keys[0] == 'y':
            filedir = QtWidgets.QFileDialog.getOpenFileName(None,'Select .pkl file with RBD experimental settings')
            self.settings = pd.read_pickle(filedir[0])
            
        if res == QtWidgets.QMessageBox.AcceptRole:
            rbsSets = RBSSettingsDialog(parent=self)
            rbsSets.exec()
            self.settings = rbsSets.return_input()  
            from psychopy import gui
            self.settings.to_pickle(gui.fileSaveDlg(initFilePath=self.logdir, initFileName="__RBDsettings__.pkl"))

        # rbsSets = RBSSettingsDialog(parent=self)
        # rbsSets.exec()
        # self.settings = rbsSets.return_input()  
        # from psychopy import gui
        # self.settings.to_pickle(gui.fileSaveDlg(initFilePath=self.logdir, initFileName="__RBDsettings__.pkl"))
        
        print(type(self.settings))
        if type(self.settings) != 'str':
            import MainExperiment_RBD as MainExperiment_RBD
            MainExperiment_RBD.run_it(self.settings, self.path, self.logdir, self.maxforce, self.offset, self.FW)
            ######################
            self.ui.label5.setText("Ready to run another RBD session")
        self.show()
        
    
    
    
    
    
#%% 

# if __name__ == '__main__':
#     # get path to script 
#     import os 
#     import sys
#     path = os.path.split(sys.argv[0])[0]
#     os.chdir(path)
    
#     app = QApplication(sys.argv)
#     window = MainWindow()
#     window.show()
    
#     sys.exit(app.exec_())
#     exit() 
    
    
    
    