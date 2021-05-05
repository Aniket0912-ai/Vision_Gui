from abcd import *
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import *
from PyQt5.QtGui import QMovie
from PyQt5.QtGui import *
from PyQt5.QtCore import QDate, QTime, QDateTime, Qt
from PyQt5.uic import loadUiType
import sys
import speech_recognition as sr
import pyttsx3
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice',voices[0].id)
engine.setProperty('rate',180)

# startExe = MainThread()
class Abcd(Ui_MainWindow):
        def __init__(self, window):
                self.setupUi(window)
                self.pushButton.clicked.connect(self.start)
                self.pushButton_2.clicked.connect(self.features)
                self.pushButton_3.clicked.connect(self.exit)
                # self.pushButton.clicked.connect(self.startAnimation)
        def start(self):
                engine.say("Good morning Sir I am start function")
                engine.runAndWait()

                t_ime = QTime.currentTime()
                time = t_ime.toString()
                d_ate = QDate.currentDate()
                date = d_ate.toString()
                label_time = "Time :" + time +" \n "+ "Date :" + date
                self.real_date_time.setText(label_time)

                self.label = QtGui.QMovie("listen.gif")
                self.Gif_1.setMovie(self.label)
                self.label.start()

        def features(self):
                engine.say("My features ae I can perform all system task, web browsing iand also data analysis and visualization and many more ")
                engine.runAndWait()
        def exit(self):
                engine.say("I am going sir bye")
                engine.runAndWait()

app = QtWidgets.QApplication(sys.argv)
MainWindow = QtWidgets.QMainWindow()

ui = Abcd(MainWindow)

MainWindow.show()
app.exec_()

