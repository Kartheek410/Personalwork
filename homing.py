# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'homing.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
import time
import RPi.GPIO as GPIO
from time import sleep

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
delay = 0.0010
delay1 = 0.0025
enable_z = 27
opto_z = 21
pull_z = 26
dir_z = 13
top_z = 23
bottom_z = 17
enable_tilt = 5
opto_tilt = 24
pull_tilt = 25
dir_tilt = 6
#projector = 20
#LED = 19
GPIO.setup(top_z,GPIO.IN, pull_up_down=GPIO.PUD_UP) 
GPIO.setup(bottom_z,GPIO.IN, pull_up_down=GPIO.PUD_UP)

class Ui_HomingWindow(object):
    def setupUi(self, HomingWindow):
        HomingWindow.setObjectName("HomingWindow")
        HomingWindow.setEnabled(True)
        HomingWindow.resize(1024, 600)
        HomingWindow.setMinimumSize(QtCore.QSize(1024, 600))
        HomingWindow.setMaximumSize(QtCore.QSize(1024, 600))
        HomingWindow.setStyleSheet("background-color: rgb(60, 181, 228);")
        HomingWindow.setIconSize(QtCore.QSize(24, 24))
        self.centralwidget = QtWidgets.QWidget(HomingWindow)
        self.centralwidget.setMinimumSize(QtCore.QSize(1024, 600))
        self.centralwidget.setMaximumSize(QtCore.QSize(1024, 600))
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(110, 190, 120, 120))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet("background-color: rgb(60, 181, 228);")
        self.pushButton.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/newPrefix/up-chevron.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton.setIcon(icon)
        self.pushButton.setIconSize(QtCore.QSize(70, 70))
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.tiltup)
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(0, 10, 1021, 81))
        self.label.setTextFormat(QtCore.Qt.RichText)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(110, 440, 120, 120))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setStyleSheet("background-color: rgb(60, 181, 228);")
        self.pushButton_2.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/newPrefix/down-chevron.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_2.setIcon(icon1)
        self.pushButton_2.setIconSize(QtCore.QSize(70, 70))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_2.clicked.connect(self.tiltdown)
        self.pushButton_6 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_6.setGeometry(QtCore.QRect(310, 330, 121, 81))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_6.setFont(font)
        self.pushButton_6.setStyleSheet("background-color: rgb(60, 181, 228);")
        self.pushButton_6.setIconSize(QtCore.QSize(16, 16))
        self.pushButton_6.setObjectName("pushButton_6")
        self.pushButton_7 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_7.setGeometry(QtCore.QRect(810, 140, 61, 61))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_7.setFont(font)
        self.pushButton_7.setStyleSheet("background-color: rgb(60, 181, 228);border: None;")
        self.pushButton_7.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/newPrefix/house-design.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_7.setIcon(icon2)
        self.pushButton_7.setIconSize(QtCore.QSize(50, 50))
        self.pushButton_7.setObjectName("pushButton_7")
        self.pushButton_7.clicked.connect(self.resetz)
        self.TiltA = QtWidgets.QLabel(self.centralwidget)
        self.TiltA.setGeometry(QtCore.QRect(110, 340, 120, 71))
        self.TiltA.setAlignment(QtCore.Qt.AlignCenter)
        self.TiltA.setObjectName("TiltA")
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(310, 440, 120, 120))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_3.setFont(font)
        self.pushButton_3.setStyleSheet("background-color: rgb(60, 181, 228);")
        self.pushButton_3.setText("")
        self.pushButton_3.setIcon(icon1)
        self.pushButton_3.setIconSize(QtCore.QSize(70, 70))
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_3.clicked.connect(self.bottomz)
        self.pushButton_4 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_4.setGeometry(QtCore.QRect(310, 190, 120, 120))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_4.setFont(font)
        self.pushButton_4.setStyleSheet("background-color: rgb(60, 181, 228);")
        self.pushButton_4.setText("")
        self.pushButton_4.setIcon(icon)
        self.pushButton_4.setIconSize(QtCore.QSize(70, 70))
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_4.clicked.connect(self.topz)
        HomingWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(HomingWindow)
        QtCore.QMetaObject.connectSlotsByName(HomingWindow)

    def retranslateUi(self, HomingWindow):
        _translate = QtCore.QCoreApplication.translate
        HomingWindow.setWindowTitle(_translate("HomingWindow", "MainWindow"))
        self.label.setText(_translate("HomingWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:36pt;\">Motor Homing</span></p></body></html>"))
        self.pushButton_6.setText(_translate("HomingWindow", "Z-home"))
        self.pushButton_7.setShortcut(_translate("HomingWindow", "Ctrl+H"))
        self.TiltA.setText(_translate("HomingWindow", "<html><head/><body><p><span style=\" font-size:12pt; font-weight:600;\">Tilt Action</span></p></body></html>"))

    def setGPIO(self):
        GPIO.setup(enable_z,GPIO.OUT) #ch1 heating element
        GPIO.setup(opto_z,GPIO.OUT) #ch2 fan
        GPIO.setup(pull_z,GPIO.OUT) ##Pulse(for step (pump))
        GPIO.setup(dir_z,GPIO.OUT) ##for direction (pump)
        GPIO.output(opto_z,GPIO.LOW)
        time.sleep(delay)
        GPIO.output(enable_z,GPIO.LOW)
        time.sleep(delay)
        GPIO.setup(enable_tilt,GPIO.OUT) #ch1 heating element
        GPIO.setup(opto_tilt,GPIO.OUT) #ch2 fan
        GPIO.setup(pull_tilt,GPIO.OUT) ##Pulse(for step (pump))
        GPIO.setup(dir_tilt,GPIO.OUT) ##for direction (pump)
        GPIO.output(opto_tilt,GPIO.LOW)
        time.sleep(delay)
        GPIO.output(enable_tilt,GPIO.LOW)
        time.sleep(delay)

    def bottomz(self):
        self.setGPIO()
        GPIO.output(opto_z,GPIO.HIGH)
        time.sleep(delay)
        GPIO.output(enable_z,GPIO.HIGH)
        time.sleep(delay)
        GPIO.output(dir_z,GPIO.LOW)
        time.sleep(delay)
        print("pumping")
        #counter = counter + 1
        for x in range(20000):
            GPIO.output(pull_z,GPIO.HIGH)
            time.sleep(delay)
            GPIO.output(pull_z,GPIO.LOW)
            time.sleep(delay)
            if (GPIO.input(bottom_z) == 1):
                print("movement")
                break

    def topz(self):
        self.setGPIO()
        GPIO.output(opto_z,GPIO.HIGH)
        time.sleep(delay)
        GPIO.output(enable_z,GPIO.HIGH)
        time.sleep(delay)
        GPIO.output(dir_z,GPIO.HIGH)
        time.sleep(delay)
        print("pumping")
        #counter = counter + 1
        for x in range(20000):
            GPIO.output(pull_z,GPIO.HIGH)
            time.sleep(delay)
            GPIO.output(pull_z,GPIO.LOW)
            time.sleep(delay)
            if (GPIO.input(top_z) == 1):
                print("movement 2")
                break
    def tiltup(self):
        self.setGPIO()
        GPIO.output(opto_tilt,GPIO.HIGH)
        time.sleep(delay1)
        GPIO.output(enable_tilt,GPIO.HIGH)
        time.sleep(delay1)
        GPIO.output(dir_tilt,GPIO.LOW)
        time.sleep(delay1)
        print("pumping")
        #counter = counter + 1
        for x in range(1600):
            GPIO.output(pull_tilt,GPIO.HIGH)
            time.sleep(delay1)
            GPIO.output(pull_tilt,GPIO.LOW)
            time.sleep(delay1)

    def tiltdown(self):
        self.setGPIO()
        GPIO.output(opto_tilt,GPIO.HIGH)
        time.sleep(delay1)
        GPIO.output(enable_tilt,GPIO.HIGH)
        time.sleep(delay1)
        GPIO.output(dir_tilt,GPIO.HIGH)
        time.sleep(delay1)
        print("pumping")
        #counter = counter + 1
        for x in range(1600):
            GPIO.output(pull_tilt,GPIO.HIGH)
            time.sleep(delay1)
            GPIO.output(pull_tilt,GPIO.LOW)
            time.sleep(delay1)
    def resetz(self):
        self.setGPIO()
        GPIO.output(opto_z,GPIO.LOW)
        time.sleep(delay)
        GPIO.output(enable_z,GPIO.LOW)
        time.sleep(delay)
        GPIO.output(opto_tilt,GPIO.LOW)
        time.sleep(delay)
        GPIO.output(enable_tilt,GPIO.LOW)
        time.sleep(delay)
        GPIO.cleanup()
        print("done")

import source_rc


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    HomingWindow = QtWidgets.QMainWindow()
    ui = Ui_HomingWindow()
    ui.setupUi(HomingWindow)
    HomingWindow.show()
    sys.exit(app.exec_())