# APP Imports
import sys
import os
import platform

from os import path
project_root = path.abspath(path.join(path.dirname(path.abspath(__file__)), '..'))
sys.path.append(project_root)
from PySide2 import QtCore, QtGui, QtWidgets
from PySide2.QtCore import (QCoreApplication, QPropertyAnimation, QDate, QDateTime, QMetaObject, QObject, QPoint, QRect, QSize, QTime, QUrl, Qt, QEvent)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont, QFontDatabase, QIcon, QKeySequence, QLinearGradient, QPalette, QPainter, QPixmap, QRadialGradient)
from PySide2.QtWidgets import *
from PySide2.QtMultimedia import *
from PySide2.QtMultimediaWidgets import *

# Import user interface file
from main_window import *

from _main.pitch_harmonic import initInterface
from harmonic_algorithm.transcription.score import MiditoScore
from harmonic_algorithm.io import AudioLoader
from PySide2extn.RoundProgressBar import roundProgressBar
import time
import midi2audio
import webbrowser



# Global value for the windows status
WINDOW_SIZE = 0
porcentaje = 0
audioduration = 0
# This will help us determine if the window is minimized or maximized

# Main class

class MainWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # Set window Icon
        self.setWindowIcon(QtGui.QIcon(":/images/images/logo.png"))
        self.setWindowTitle("Harmonic Algorithm App")

        # remover titulo windows
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint) 

        # background transparente
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
      
        # shadow effect
        self.shadow = QGraphicsDropShadowEffect(self)
        self.shadow.setBlurRadius(20)
        self.shadow.setXOffset(0)
        self.shadow.setYOffset(0)
        self.shadow.setColor(QColor(0, 92, 157, 150))
        
        self.ui.centralwidget.setGraphicsEffect(self.shadow)

        
        #Minimize window
        self.ui.minimizeButton.clicked.connect(lambda: self.showMinimized())
        #Close window
        self.ui.closeButton.clicked.connect(lambda: self.close())
        #Restore/Maximize window
        self.ui.restoreButton.clicked.connect(lambda: self.restore_or_maximize_window())
        


        def moveWindow(e):
             
            if self.isMaximized() == False: #Not maximized
                if e.buttons() == Qt.LeftButton:  
                    self.move(self.pos() + e.globalPos() - self.clickPosition)
                    self.clickPosition = e.globalPos()
                    e.accept()

        
        self.ui.main_header.mouseMoveEvent = moveWindow
        self.ui.left_menu_toggle_btn.clicked.connect(lambda: self.slideLeftMenu())
        self.ui.stackedWidget.setCurrentWidget(self.ui.home_page)


        self.ui.home_button.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.home_page))
        self.ui.accounts_button.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.accounts_page))
        self.ui.settings_button.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.settings_page))
    

        for w in self.ui.left_side_menu.findChildren(QPushButton):
            # Add click event listener
            w.clicked.connect(self.applyButtonStyle)
            

        #################################################################################
        # PASO 1
        #################################################################################
        self.ui.loadWavButton.clicked.connect(lambda: self.loadMusicalPiece())
        self.audioduration = 100
        self.constant_conversion = 0
        self.ui.scoreGenerateButton.clicked.connect(lambda: self.createScore())
        
        self.ui.progress.rpb_setMaximum(100)
        self.ui.progress.rpb_setBarStyle("Pizza")
        self.ui.progress.rpb_setTextRatio(6)
        self.ui.progress.rpb_setValue(0)
        
  

        #################################################################################
        # PASO 2
        #################################################################################
        output = sys.path[-1] + "/samples/output/"
        self.ui.generarMIDIButton.clicked.connect(lambda: os.startfile(output))
        self.ui.generarPDFButton.clicked.connect(lambda: os.startfile(output + "/PDFcreate.pdf"))
        
        
        
        
        #################################################################################
        # PLAYER MEDIA
        #################################################################################
        
        self.ui.url = QUrl.fromLocalFile(output+"/9 Perpetual Motion.wav")
        self.ui.content = QMediaContent(self.ui.url)
        self.ui.player = QMediaPlayer()
        self.ui.player.setMedia(self.ui.content)
        
        
        self.ui.playButton.clicked.connect(lambda: self.ui.player.play())
        self.ui.pauseButton.clicked.connect(lambda: self.ui.player.pause())
        self.ui.stopButton.clicked.connect(lambda: self.ui.player.stop())
        

        self.ui.player.durationChanged.connect(lambda: self.update_duration(self.ui.player.duration()))
        self.ui.player.positionChanged.connect(lambda: self.update_position(self.ui.player.position()))
        self.ui.timestampSlider.valueChanged.connect(lambda: self.ui.player.position())
        
        #################################################################################
        # GITHUB BUTTON
        #################################################################################
        self.ui.githubButton.clicked.connect(lambda: self.open_webbrowser())
        
        
        #################################################################################
        # Window Size grip
        #################################################################################
        QSizeGrip(self.ui.size_grip)
        

        # ############################################
        # Show window
        self.show()
        # ###############################################

    
    def loadMusicalPiece(self):
        fname = QtWidgets.QFileDialog.getOpenFileName(self, 'Open file', 'E:/UMSA/0Tesis2/CODIGO FINAL/0 Klapuri/harmonic/samples/input','WAV Files (*.wav)')
        self.ui.loadWavEditLine.setText(fname[0])
    
    def update_duration(self,duration):
        self.ui.timestampSlider.setMaximum(duration)
        if duration >= 0:
            self.ui.totaltimeLabel.setText(self.hhmmss(duration))
    def update_position(self, position):
        if position >= 0:
            self.ui.timestampLabel.setText(self.hhmmss(position))
        
        self.ui.timestampSlider.blockSignals(True)
        self.ui.timestampSlider.setValue(position)
        self.ui.timestampSlider.blockSignals(False)
    
    def createScore(self):
        global audioduration
        filepath = self.ui.loadWavEditLine.text()
        umbral = self.ui.umbralSlider.value()
        heuristica = self.ui.heuristicaSlider.value()
        
        audio = AudioLoader(filepath)
        #audio.cut(stop=5)
        audioduration = int (audio.returnDuration()/2)
             
        '''
        self.timer_conv = QtCore.QTimer()
        self.timer_conv.timeout.connect(self.conversion_status)
        self.timer_conv.start(audioduration)
        QtCore.QTimer.singleShot(0, lambda: self.ui.progress.rpb_setValue(0))
        '''
        
        self.threadpool = QtCore.QThreadPool()
        self.initCreateScore = initCreateScore(filepath, audio, umbral, heuristica)
        self.threadpool.start(self.initCreateScore)

        self.startProgressBar()
        

        
        
        #initInterface(filepath, audio, umbral, heuristica)
        
        
        
    
    def startProgressBar(self):
        sl = (audioduration/125)
        #print(audioduration, sl)
        self.thread = ThreadClass(sl)
        self.thread.change_value.connect(self.setProgressBar)
        self.thread.start()
    
    def setProgressBar(self, val):
        self.ui.progress.rpb_setValue(val)
        
    
    def conversion_status(self):
        
        global porcentaje
        
        if(porcentaje <= 100):
            self.ui.progress.rpb_setValue(porcentaje)
        
        porcentaje += 1
   
        
    def hhmmss(self, ms):
        s = round(ms/1000)
        m, s = divmod(s, 60)
        h, m = divmod(m, 60)
        return ("%d:%02d:%02d" % (m, h, s)) if h else ("%d:%02d" % (m, s))
    
    def open_webbrowser(self):
        webbrowser.open('https://github.com/TheProdigyK/HarmonicAlgorithm-thesis')
    

    def restore_or_maximize_window(self):
        
        global WINDOW_SIZE 
        win_status = WINDOW_SIZE
        if win_status == 0:
        	WINDOW_SIZE = 1 
        	self.showMaximized()
        	self.ui.restoreButton.setIcon(QtGui.QIcon(u":/icons/icons/cil-window-restore.png"))
        else:
            WINDOW_SIZE = 0
            self.showNormal()
            self.ui.restoreButton.setIcon(QtGui.QIcon(u":/icons/icons/cil-window-maximize.png"))

    ########################################################################
    # Slide left menu
    ########################################################################
    def slideLeftMenu(self):
        width = self.ui.left_side_menu.width()

       
        if width == 55:
            
            newWidth = 150

        else:

            newWidth = 50


        self.animation = QPropertyAnimation(self.ui.left_side_menu, b"minimumWidth")
        self.animation.setDuration(250)
        self.animation.setStartValue(width)
        self.animation.setEndValue(newWidth)
        self.animation.setEasingCurve(QtCore.QEasingCurve.InOutQuart)
        self.animation.start()

    # //////////////////////////////////////////////////////////////////////
    
    def applyButtonStyle(self):
        # Reset style for other buttons
        for w in self.ui.left_side_menu.findChildren(QPushButton):
            # If the button name is not equal to clicked button name
            if w.objectName() != self.sender().objectName():
                # Create default style by removing the left border
                # Lets remove the bottom border style
                defaultStyle = w.styleSheet().replace("border-bottom: 2px solid  rgb(0, 136, 255);", "")

                # Lets also remove the left border style
                defaultStyle = defaultStyle.replace("border-left: 2px solid  rgb(0, 136, 255);", "")

                # Apply the default style
                w.setStyleSheet(defaultStyle)
                #                 

        # Apply new style to clicked button
        # Sender = clicked button
        # Get the clicked button stylesheet then add new left-border style to it
        # Lets add the bottom border style
        newStyle = self.sender().styleSheet() + ("border-left: 2px solid  rgb(0, 136, 255);border-bottom: 2px solid  rgb(0, 136, 255);")
        # Apply the new style
        self.sender().setStyleSheet(newStyle)
        # 
        return


class ThreadClass(QtCore.QThread):
    def __init__(self,sleep):
        QtCore.QThread.__init__(self)
        self.sleep = sleep
        
    change_value = QtCore.Signal(int)
    
    def run(self):
        cnt = 0
        print(self.sleep)
        while cnt <= 100:
            #print(cnt)
            time.sleep(self.sleep)
            self.change_value.emit(cnt)
            cnt +=1

class initCreateScore(QtCore.QRunnable):
    def __init__(self, filepath, audio, umbral, heuristica):
        #super.__init__(self, filepath, audio, umbral, heuristica)
        super(initCreateScore, self).__init__(filepath, audio, umbral, heuristica)
        self.filepath = filepath
        self.audio = audio
        self.umbral = umbral
        self.heuristica = heuristica
        
    def run(self):
        initInterface(self.filepath, self.audio, self.umbral, self.heuristica)
        
            
# Execute app
# 
if __name__ == "__main__":
    #app = QApplication(sys.argv)
    if not QApplication.instance():
        app = QApplication(sys.argv)
    else:
        app = QApplication.instance()
    window = MainWindow()
    sys.exit(app.exec_())
else:
	print(__name__, "hh")


