from PyQt5.QtCore import QDir, Qt, QUrl,QSize
from PyQt5.QtMultimedia import QMediaContent, QMediaPlayer,QAudio
from PyQt5.QtMultimediaWidgets import QVideoWidget
from PyQt5.QtWidgets import (QApplication, QFileDialog, QHBoxLayout, QLabel,QPushButton, QSizePolicy, QSlider, QStyle, QVBoxLayout, QWidget)
from PyQt5.QtWidgets import QMainWindow,QWidget, QPushButton, QAction,QSplashScreen
from PyQt5.QtGui import QIcon,QPixmap
from PyQt5 import QtGui
import sys
import time

class VideoWindow(QMainWindow):

    def __init__(self):
        super().__init__()
        self.label3=QLabel(self)
        pix=QPixmap('background.png')
        self.label3.setPixmap(pix)
        self.label3.setGeometry(100,0, 640, 480)
        self.setWindowTitle("MALLIK AUDIO/VIDEO PLAYER") 
        self.setWindowIcon(QIcon('video icon.png'))

        videoWidget = QVideoWidget()
        self.playButton = QPushButton()
        self.playButton.setEnabled(False)
        self.playButton.setIcon(self.style().standardIcon(QStyle.SP_MediaPlay))
        self.playButton.clicked.connect(self.play)

        self.positionSlider = QSlider(Qt.Horizontal)
   
        self.positionSlider.sliderMoved.connect(self.setPosition)
        
        self.positionSlider2 = QSlider(Qt.Horizontal)
        self.positionSlider2.setMinimum(55)
        self.positionSlider2.setMaximum(100)
        self.positionSlider2.setValue(55)
        self.positionSlider2.valueChanged.connect(self.volumeChanged)
        self.positionSlider2.setTickPosition(QSlider.TicksBothSides)

        self.backward = QPushButton()
        self.backward.setEnabled(True)
        self.backward.setIcon(self.style().standardIcon(QStyle.SP_MediaSeekBackward))
        # self.backward.clicked.connect(self.backwar)

        self.forward = QPushButton()
        self.forward.setEnabled(True)
        self.forward.setIcon(self.style().standardIcon(QStyle.SP_MediaSeekForward))
        # self.forward.clicked.connect(self.forwar)
        

      

        # Create new action
        openAction = QAction(QIcon('open3.png'), '&Open', self)        
        openAction.setShortcut('Ctrl+O')
        openAction.setStatusTip('Open movie')
        openAction.triggered.connect(self.openFile)

        # Create exit action
        exitAction = QAction(QIcon('exit.png'), '&Exit', self)        
        exitAction.setShortcut('Ctrl+Q')
        exitAction.setStatusTip('Exit application')
        exitAction.triggered.connect(self.exitCall)

        # Create menu bar and add action
        menuBar = self.menuBar()
        fileMenu = menuBar.addMenu(QIcon('open8.png'),'&File')
        
        # fileName = QFileDialog.getOpenFileName(self, "Open Movie",QDir.homePath())
        menuBar2 = self.menuBar()
        fileMenu2 = menuBar2.addMenu('playback')
        action = QAction(QIcon('forward.png'), '&1.5', self)
        action.triggered.connect(self.forward1)
        fileMenu2.addAction(action)
        action1 = QAction(QIcon('forward.png'), '&2.0', self)
        action1.triggered.connect(self.forward2)
        fileMenu2.addAction(action1)

        action2 = QAction(QIcon('forward.png'), '&0.25', self)
        action2.triggered.connect(self.forward3)
        fileMenu2.addAction(action2)

        action3 = QAction('&audio', self)
        # action3.triggered.connect(self.audio)
        fileMenu2.addAction(action3)
        
        fileMenu.addAction(openAction)
        fileMenu.addAction(exitAction)

        # Create a widget for window contents
        wid = QWidget(self)
        self.setCentralWidget(wid)
        
        # self.label4=QLabel()
        # self.label4.setText('hiiiiiiiii')
        # Create layouts to place inside widget
        controlLayout = QHBoxLayout()
        # controlLayout.setContentsMargins(0, 0, 0, 0)
        # controlLayout.addWidget(self.label4)
        controlLayout.addWidget(self.playButton)
        # controlLayout.addWidget(self.backward)
        controlLayout.addWidget(self.positionSlider)
        # controlLayout.addWidget(self.forward)
        controlLayout.addWidget(self.positionSlider2)
        
        layout = QVBoxLayout()
        layout.addWidget(videoWidget)
        layout.addLayout(controlLayout)
        # layout.addWidget(self.label4)
        # layout.addWidget(self.errorLabel)
        # layout.addWidget(self.positionSlider2)
        
        # Set widget to contain window contents
        wid.setLayout(layout)
        
        self.mediaPlayer = QMediaPlayer(None, QMediaPlayer.VideoSurface)
        # print(self.mediaPlayer.currentMedia().canonicalUrl().toString())
        

        self.mediaPlayer.setVideoOutput(videoWidget)
        self.mediaPlayer.stateChanged.connect(self.mediaStateChanged)
        self.mediaPlayer.positionChanged.connect(self.positionChanged)
        self.mediaPlayer.durationChanged.connect(self.durationChanged)
        self.mediaPlayer.currentMediaChanged.connect(self.songChanged)
        # self.sound=QAudio()
        # self.mediaPlayer.error.connect(self.handleError)
    
    def songChanged(self, media):
        if not media.isNull():
            url = media.canonicalUrl()
            self.statusBar().showMessage(url.fileName())

    def openFile(self,fileName):
        fileName, _ = QFileDialog.getOpenFileName(self, "Open Movie",QDir.homePath())
      

        if fileName != '':
            self.mediaPlayer.setMedia(QMediaContent(QUrl.fromLocalFile(fileName)))
       
            self.mediaPlayer.setPosition(0)

            self.playButton.setEnabled(True)
          
    def exitCall(self):
            sys.exit(app.exec_())

    def play(self,state):
        if self.mediaPlayer.state() == QMediaPlayer.PlayingState:
            self.mediaPlayer.pause()
        else:
            self.mediaPlayer.play()

    def mediaStateChanged(self, state):
        if self.mediaPlayer.state() == QMediaPlayer.PlayingState:
            self.playButton.setIcon(
                    self.style().standardIcon(QStyle.SP_MediaPause))
        else:
            self.playButton.setIcon(self.style().standardIcon(QStyle.SP_MediaPlay))

    def positionChanged(self, position):
        self.positionSlider.setValue(position)
    
    def durationChanged(self, duration):
        self.positionSlider.setRange(0, duration)

    def setPosition(self, position):
        self.mediaPlayer.setPosition(position)
    
    def volumeChanged(self,volume):
        volume=self.positionSlider2.value()
        self.mediaPlayer.setVolume(volume)

    def forward1(self):
        self.mediaPlayer.setPlaybackRate(1.5)
    
    def forward2(self):
        self.mediaPlayer.setPlaybackRate(2.0)

    def forward3(self):
        self.mediaPlayer.setPlaybackRate(0.25)
    # def audio(self):
        # a=
        # print(a)


if __name__ == '__main__':
    import time
    # time.sleep(2)
    app = QApplication(sys.argv)
    splash_pix = QPixmap('main3.png')
    splash = QSplashScreen(splash_pix, Qt.WindowStaysOnTopHint)
    splash.setMask(splash_pix.mask())
    splash.show()
    app.processEvents()
    
    # Simulate something that takes time
    time.sleep(2)
    player = VideoWindow()
    player.resize(640, 480)
    player.show()
    splash.finish(player)
    sys.exit(app.exec_())







# # # PLAY FROM PLAY BUTTON==============================================================>
# # from PyQt5.QtCore import QDir, Qt, QUrl
# # from PyQt5.QtMultimedia import QMediaContent, QMediaPlayer
# # from PyQt5.QtMultimediaWidgets import QVideoWidget
# # from PyQt5.QtWidgets import (QApplication, QFileDialog, QHBoxLayout, QLabel,QPushButton, QSizePolicy, QSlider, QStyle, QVBoxLayout, QWidget)
# # from PyQt5.QtWidgets import QMainWindow,QWidget, QPushButton, QAction
# # from PyQt5.QtGui import QIcon
# # import sys
# # import time

# # class VideoWindow(QMainWindow):

# #     def __init__(self, parent=None):
# #         super(VideoWindow, self).__init__(parent)
# #         self.setWindowTitle("PyQt Video Player Widget Example - pythonprogramminglanguage.com") 

# #         self.mediaPlayer = QMediaPlayer(None, QMediaPlayer.VideoSurface)

# #         videoWidget = QVideoWidget()

# #         self.playButton = QPushButton()
# #         self.playButton.setEnabled(True)
# #         self.playButton.setIcon(self.style().standardIcon(QStyle.SP_MediaPlay))
# #         # self.playButton.clicked.connect(self.openFile)
# #         self.playButton.clicked.connect(self.play)

# #         self.positionSlider = QSlider(Qt.Horizontal)
# #         self.positionSlider.setRange(0, 0)
# #         self.positionSlider.sliderMoved.connect(self.setPosition)

# #         self.errorLabel = QLabel()
# #         self.errorLabel.setSizePolicy(QSizePolicy.Preferred,
# #                 QSizePolicy.Maximum)

# #         # Create new action
# #         openAction = QAction(QIcon('open.png'), '&Open', self)        
# #         openAction.setShortcut('Ctrl+O')
# #         openAction.setStatusTip('Open movie')
# #         # openAction.triggered.connect(self.openFile)

# #         # Create exit action
# #         exitAction = QAction(QIcon('exit.png'), '&Exit', self)        
# #         exitAction.setShortcut('Ctrl+Q')
# #         exitAction.setStatusTip('Exit application')
# #         exitAction.triggered.connect(self.exitCall)

# #         # Create menu bar and add action
# #         menuBar = self.menuBar()
# #         fileMenu = menuBar.addMenu('&File')
        
# #         # fileMenu.addAction(newAction)
# #         fileMenu.addAction(openAction)
# #         fileMenu.addAction(exitAction)

# #         # Create a widget for window contents
# #         wid = QWidget(self)
# #         self.setCentralWidget(wid)

# #         # Create layouts to place inside widget
# #         controlLayout = QHBoxLayout()
# #         controlLayout.setContentsMargins(0, 0, 0, 0)
# #         controlLayout.addWidget(self.playButton)
# #         controlLayout.addWidget(self.positionSlider)

# #         layout = QVBoxLayout()
# #         layout.addWidget(videoWidget)
# #         layout.addLayout(controlLayout)
# #         layout.addWidget(self.errorLabel)

# #         # Set widget to contain window contents
# #         wid.setLayout(layout)

# #         self.mediaPlayer.setVideoOutput(videoWidget)
# #         self.mediaPlayer.stateChanged.connect(self.mediaStateChanged)
# #         self.mediaPlayer.positionChanged.connect(self.positionChanged)
# #         self.mediaPlayer.durationChanged.connect(self.durationChanged)
# #         self.mediaPlayer.error.connect(self.handleError)
# #         fileName=r'D:\python\Open Movie.mp4'

# #         if fileName != '':
# #             self.mediaPlayer.setMedia(QMediaContent(QUrl.fromLocalFile(fileName)))
# #             self.playButton.setEnabled(True)
# #         # time.sleep(2)


# #     def exitCall(self):
# #         sys.exit(app.exec_())

# #     def play(self):
# #         if self.mediaPlayer.state() == QMediaPlayer.PlayingState:
# #             self.mediaPlayer.pause()
# #         else:
# #             self.mediaPlayer.play()

# #     def mediaStateChanged(self, state):
# #         if self.mediaPlayer.state() == QMediaPlayer.PlayingState:
# #             self.playButton.setIcon(
# #                     self.style().standardIcon(QStyle.SP_MediaPause))
# #         else:
# #             self.playButton.setIcon(
# #                     self.style().standardIcon(QStyle.SP_MediaPlay))

# #     def positionChanged(self, position):
# #         self.positionSlider.setValue(position)

# #     def durationChanged(self, duration):
# #         self.positionSlider.setRange(0, duration)

# #     def setPosition(self, position):
# #         self.mediaPlayer.setPosition(position)

# #     def handleError(self):
# #         self.playButton.setEnabled(False)
# #         self.errorLabel.setText("Error: " + self.mediaPlayer.errorString())

# # if __name__ == '__main__':
# #     app = QApplication(sys.argv)
# #     player = VideoWindow()
# #     player.resize(640, 480)
# #     player.show()
# #     sys.exit(app.exec_())

# from PyQt5.QtGui import QPalette, QKeySequence, QIcon
# from PyQt5.QtCore import QDir, Qt, QUrl, QSize, QPoint, QTime, QMimeData, QProcess
# from PyQt5.QtMultimedia import QMediaContent, QMediaPlayer, QMediaMetaData
# from PyQt5.QtMultimediaWidgets import QVideoWidget
# from PyQt5.QtWidgets import (QApplication, QFileDialog, QHBoxLayout, QLineEdit,
#                             QPushButton, QSizePolicy, QSlider, QMessageBox, QStyle, QVBoxLayout,  
#                             QWidget, QShortcut, QMenu)
# import sys
# import os
# import subprocess
# #QT_DEBUG_PLUGINS

# class VideoPlayer(QWidget):

#     def __init__(self, aPath, parent=None):
#         super(VideoPlayer, self).__init__(parent)

#         self.setAttribute( Qt.WA_NoSystemBackground, True )
#         self.setAcceptDrops(True)
#         self.mediaPlayer = QMediaPlayer(None, QMediaPlayer.StreamPlayback)
#         self.mediaPlayer.mediaStatusChanged.connect(self.printMediaData)
#         self.mediaPlayer.setVolume(80)
#         self.videoWidget = QVideoWidget(self)
        
#         self.lbl = QLineEdit('00:00:00')
#         self.lbl.setReadOnly(True)
#         self.lbl.setFixedWidth(70)
#         self.lbl.setUpdatesEnabled(True)
#         self.lbl.setStyleSheet(stylesheet(self))
        
#         self.elbl = QLineEdit('00:00:00')
#         self.elbl.setReadOnly(True)
#         self.elbl.setFixedWidth(70)
#         self.elbl.setUpdatesEnabled(True)
#         self.elbl.setStyleSheet(stylesheet(self))

#         self.playButton = QPushButton()
#         self.playButton.setEnabled(False)
#         self.playButton.setFixedWidth(32)
#         self.playButton.setStyleSheet("background-color: black")
#         self.playButton.setIcon(self.style().standardIcon(QStyle.SP_MediaPlay))
#         self.playButton.clicked.connect(self.play)

#         self.positionSlider = QSlider(Qt.Horizontal, self)
#         self.positionSlider.setStyleSheet (stylesheet(self)) 
#         self.positionSlider.setRange(0, 100)
#         self.positionSlider.sliderMoved.connect(self.setPosition)
#         self.positionSlider.sliderMoved.connect(self.handleLabel)
#         self.positionSlider.setSingleStep(2)
#         self.positionSlider.setPageStep(20)
#         self.positionSlider.setAttribute(Qt.WA_TranslucentBackground, True)

#         self.clip = QApplication.clipboard()
#         self.process = QProcess(self)
#         self.process.readyRead.connect(self.dataReady)
# #        self.process.started.connect(lambda: print("grabbing YouTube URL"))
#         self.process.finished.connect(self.playFromURL)

#         self.myurl = ""
        
#         controlLayout = QHBoxLayout()
#         controlLayout.setContentsMargins(5, 0, 5, 0)
#         controlLayout.addWidget(self.playButton)
#         controlLayout.addWidget(self.lbl)
#         controlLayout.addWidget(self.positionSlider)
#         controlLayout.addWidget(self.elbl)

#         layout = QVBoxLayout()
#         layout.setContentsMargins(0, 0, 0, 0)
#         layout.addWidget(self.videoWidget)
#         layout.addLayout(controlLayout)

#         self.setLayout(layout)
        
#         self.myinfo = "©2016\nAxel Schneider\n\nMouse Wheel = Zoom\nUP = Volume Up\nDOWN = Volume Down\n" + \
#                 "LEFT = < 1 Minute\nRIGHT = > 1 Minute\n" + \
#                 "SHIFT+LEFT = < 10 Minutes\nSHIFT+RIGHT = > 10 Minutes"

#         self.widescreen = True
        
#         #### shortcuts ####
#         self.shortcut = QShortcut(QKeySequence("q"), self)
#         self.shortcut.activated.connect(self.handleQuit)
#         self.shortcut = QShortcut(QKeySequence("u"), self)
#         self.shortcut.activated.connect(self.playFromURL)

#         self.shortcut = QShortcut(QKeySequence("y"), self)
#         self.shortcut.activated.connect(self.getYTUrl)

#         self.shortcut = QShortcut(QKeySequence("o"), self)
#         self.shortcut.activated.connect(self.openFile)
#         self.shortcut = QShortcut(QKeySequence(" "), self)
#         self.shortcut.activated.connect(self.play)
#         self.shortcut = QShortcut(QKeySequence("f"), self)
#         self.shortcut.activated.connect(self.handleFullscreen)
#         self.shortcut = QShortcut(QKeySequence("i"), self)
#         self.shortcut.activated.connect(self.handleInfo)
#         self.shortcut = QShortcut(QKeySequence("s"), self)
#         self.shortcut.activated.connect(self.toggleSlider)
#         self.shortcut = QShortcut(QKeySequence(Qt.Key_Right), self)
#         self.shortcut.activated.connect(self.forwardSlider)
#         self.shortcut = QShortcut(QKeySequence(Qt.Key_Left), self)
#         self.shortcut.activated.connect(self.backSlider)
#         self.shortcut = QShortcut(QKeySequence(Qt.Key_Up), self)
#         self.shortcut.activated.connect(self.volumeUp)
#         self.shortcut = QShortcut(QKeySequence(Qt.Key_Down), self)
#         self.shortcut.activated.connect(self.volumeDown)    
#         self.shortcut = QShortcut(QKeySequence(Qt.ShiftModifier +  Qt.Key_Right) , self)
#         self.shortcut.activated.connect(self.forwardSlider10)
#         self.shortcut = QShortcut(QKeySequence(Qt.ShiftModifier +  Qt.Key_Left) , self)
#         self.shortcut.activated.connect(self.backSlider10)

#         self.mediaPlayer.setVideoOutput(self.videoWidget)
#         self.mediaPlayer.stateChanged.connect(self.mediaStateChanged)
#         self.mediaPlayer.positionChanged.connect(self.positionChanged)
#         self.mediaPlayer.positionChanged.connect(self.handleLabel)
#         self.mediaPlayer.durationChanged.connect(self.durationChanged)
#         self.mediaPlayer.error.connect(self.handleError)

#         print("QT5 Player started")
#         self.suspend_screensaver()

#     def playFromURL(self):
#         self.mediaPlayer.pause()
#         self.myurl = self.clip.text()
#         self.mediaPlayer.setMedia(QMediaContent(QUrl(self.myurl)))
#         self.playButton.setEnabled(True)
#         self.mediaPlayer.play()
#         self.hideSlider()
#         print(self.myurl)

#     def getYTUrl(self):
#         cmd = "youtube-dl -g -f best " + self.clip.text()
#         print("grabbing YouTube URL")
#         self.process.start(cmd)

#     def dataReady(self):
#         self.myurl = str(self.process.readAll(), encoding = 'utf8').rstrip() ###
#         self.myurl = self.myurl.partition("\n")[0]
#         print(self.myurl)
#         self.clip.setText(self.myurl)
#         self.playFromURL()

#     def suspend_screensaver(self):
#         'suspend linux screensaver'
#         proc = subprocess.Popen('gsettings set org.gnome.desktop.screensaver idle-activation-enabled false', shell=True)
#         proc.wait()

#     def resume_screensaver(self):
#         'resume linux screensaver'
#         proc = subprocess.Popen('gsettings set org.gnome.desktop.screensaver idle-activation-enabled true', shell=True)
#         proc.wait()

#     def openFile(self):
#         fileName, _ = QFileDialog.getOpenFileName(self, "Open Movie",
#                 QDir.homePath() + "/Videos", "Media (*.webm *.mp4 *.ts *.avi *.mpeg *.mpg *.mkv *.VOB *.m4v *.3gp *.mp3 *.m4a *.wav *.ogg *.flac *.m3u *.m3u8)")

#         if fileName != '':
#             self.loadFilm(fileName)
#             print("File loaded")

#     def play(self):
#         if self.mediaPlayer.state() == QMediaPlayer.PlayingState:
#             self.mediaPlayer.pause()
#         else:
#             self.mediaPlayer.play()
    
#     def mediaStateChanged(self, state):
#         if self.mediaPlayer.state() == QMediaPlayer.PlayingState:
#             self.playButton.setIcon(
#                     self.style().standardIcon(QStyle.SP_MediaPause))
#         else:
#             self.playButton.setIcon(
#                     self.style().standardIcon(QStyle.SP_MediaPlay))

#     def positionChanged(self, position):
#         self.positionSlider.setValue(position)
        
#     def durationChanged(self, duration):
#         self.positionSlider.setRange(0, duration)
#         mtime = QTime(0,0,0,0)
#         mtime = mtime.addMSecs(self.mediaPlayer.duration())
#         self.elbl.setText(mtime.toString())

#     def setPosition(self, position):
#         self.mediaPlayer.setPosition(position)

#     def handleError(self):
#         self.playButton.setEnabled(False)
#         print("Error: ", self.mediaPlayer.errorString())

#     def handleQuit(self):
#         self.mediaPlayer.stop()
#         self.resume_screensaver()
#         print("Goodbye ...")
#         app.quit()
    
#     def contextMenuRequested(self,point):
#         menu = QMenu()
#         actionFile = menu.addAction(QIcon.fromTheme("video-x-generic"),"open File (o)")
#         actionclipboard = menu.addSeparator() 
#         actionURL = menu.addAction(QIcon.fromTheme("browser"),"URL from Clipboard (u)")
#         actionclipboard = menu.addSeparator() 
#         actionYTurl = menu.addAction(QIcon.fromTheme("youtube"), "URL from YouTube (y)")
#         actionclipboard = menu.addSeparator() 
#         actionToggle = menu.addAction(QIcon.fromTheme("next"),"show / hide Slider (s)") 
#         actionFull = menu.addAction(QIcon.fromTheme("view-fullscreen"),"Fullscreen (f)")
#         action169 = menu.addAction(QIcon.fromTheme("tv-symbolic"),"16 : 9")
#         action43 = menu.addAction(QIcon.fromTheme("tv-symbolic"),"4 : 3")
#         actionSep = menu.addSeparator()
#         actionInfo = menu.addAction(QIcon.fromTheme("help-about"),"Info (i)")
#         action5 = menu.addSeparator() 
#         actionQuit = menu.addAction(QIcon.fromTheme("application-exit"),"Exit (q)")

#         actionFile.triggered.connect(self.openFile)
#         actionQuit.triggered.connect(self.handleQuit)
#         actionFull.triggered.connect(self.handleFullscreen)
#         actionInfo.triggered.connect(self.handleInfo)
#         actionToggle.triggered.connect(self.toggleSlider)
#         actionURL.triggered.connect(self.playFromURL)
#         actionYTurl.triggered.connect(self.getYTUrl)
#         action169.triggered.connect(self.screen169)
#         action43.triggered.connect(self.screen43)
#         menu.exec_(self.mapToGlobal(point))

#     def wheelEvent(self,event):
#         mwidth = self.frameGeometry().width()
#         mheight = self.frameGeometry().height()
#         mleft = self.frameGeometry().left()
#         mtop = self.frameGeometry().top()
#         mscale = event.angleDelta().y() / 5
#         if self.widescreen == True:
#             self.setGeometry(mleft, mtop, mwidth + mscale, (mwidth + mscale) / 1.778) 
#         else:
#             self.setGeometry(mleft, mtop, mwidth + mscale, (mwidth + mscale) / 1.33)            

#     def screen169(self):
#         self.widescreen = True
#         mwidth = self.frameGeometry().width()
#         mheight = self.frameGeometry().height()
#         mleft = self.frameGeometry().left()
#         mtop = self.frameGeometry().top()
#         mratio = 1.778
#         self.setGeometry(mleft, mtop, mwidth, mwidth / mratio)

#     def screen43(self):
#         self.widescreen = False
#         mwidth = self.frameGeometry().width()
#         mheight = self.frameGeometry().height()
#         mleft = self.frameGeometry().left()
#         mtop = self.frameGeometry().top()
#         mratio = 1.33
#         self.setGeometry(mleft, mtop, mwidth, mwidth / mratio)

#     def handleFullscreen(self):
#         if self.windowState() & Qt.WindowFullScreen:
#             self.showNormal()
#             print("no Fullscreen")
#         else:
#             self.showFullScreen()
#             print("Fullscreen entered")

#     def handleInfo(self):
#         msg = QMessageBox.about(self, "QT5 Player", self.myinfo)
            
#     def toggleSlider(self):    
#         if self.positionSlider.isVisible():
#             self.hideSlider()
#         else:
#             self.showSlider()
    
#     def hideSlider(self):
#             self.playButton.hide()
#             self.lbl.hide()
#             self.positionSlider.hide()
#             self.elbl.hide()
#             mwidth = self.frameGeometry().width()
#             mheight = self.frameGeometry().height()
#             mleft = self.frameGeometry().left()
#             mtop = self.frameGeometry().top()
#             if self.widescreen == True:
#                 self.setGeometry(mleft, mtop, mwidth, mwidth / 1.778) 
#             else:
#                 self.setGeometry(mleft, mtop, mwidth, mwidth / 1.33)
    
#     def showSlider(self):
#             self.playButton.show()
#             self.lbl.show()
#             self.positionSlider.show()
#             self.elbl.show()
#             mwidth = self.frameGeometry().width()
#             mheight = self.frameGeometry().height()
#             mleft = self.frameGeometry().left()
#             mtop = self.frameGeometry().top()
#             if self.widescreen == True:
#                 self.setGeometry(mleft, mtop, mwidth, mwidth / 1.55) 
#             else:
#                 self.setGeometry(mleft, mtop, mwidth, mwidth / 1.33)
    
#     def forwardSlider(self):
#         self.mediaPlayer.setPosition(self.mediaPlayer.position() + 1000*60)

#     def forwardSlider10(self):
#             self.mediaPlayer.setPosition(self.mediaPlayer.position() + 10000*60)

#     def backSlider(self):
#         self.mediaPlayer.setPosition(self.mediaPlayer.position() - 1000*60)

#     def backSlider10(self):
#         self.mediaPlayer.setPosition(self.mediaPlayer.position() - 10000*60)
        
#     def volumeUp(self):
#         self.mediaPlayer.setVolume(self.mediaPlayer.volume() + 10)
#         print("Volume: " + str(self.mediaPlayer.volume()))
    
#     def volumeDown(self):
#         self.mediaPlayer.setVolume(self.mediaPlayer.volume() - 10)
#         print("Volume: " + str(self.mediaPlayer.volume()))
        
#     def mouseMoveEvent(self, event):   
#         if event.buttons() == Qt.LeftButton:
#             self.move(event.globalPos() \
#                         - QPoint(self.frameGeometry().width() / 2, \
#                         self.frameGeometry().height() / 2))
#             event.accept() 
        
#     def dragEnterEvent(self, event):
#         if event.mimeData().hasUrls():
#             event.accept()
#         elif event.mimeData().hasText():
#             event.accept()
#         else:
#             event.ignore()

#     def dropEvent(self, event):
#         if event.mimeData().hasUrls():
#             f = str(event.mimeData().urls()[0].toLocalFile())
#             self.loadFilm(f)
#         elif event.mimeData().hasText():
#             mydrop = str(event.mimeData().text())
#             print(mydrop)
#             ### YouTube url
#             if "https://www.youtube" in mydrop:
#                 print("is YouTube")
# #                mydrop = mydrop.partition("&")[0].replace("watch?v=", "v/")
#                 self.clip.setText(mydrop)
#                 self.getYTUrl()
#             else:
#                 ### normal url
#                 self.mediaPlayer.setMedia(QMediaContent(QUrl(mydrop)))
#                 self.playButton.setEnabled(True)
#                 self.mediaPlayer.play()
#                 self.hideSlider()
#             print(mydrop)
    
#     def loadFilm(self, f):
#             self.mediaPlayer.setMedia(QMediaContent(QUrl.fromLocalFile(f)))
#             self.playButton.setEnabled(True)
#             self.mediaPlayer.play()

#     def printMediaData(self):
#         if self.mediaPlayer.mediaStatus() == 6:
#             if self.mediaPlayer.isMetaDataAvailable():
#                 res = str(self.mediaPlayer.metaData("Resolution")).partition("PyQt5.QtCore.QSize(")[2].replace(", ", " x ").replace(")", "")
#                 print("%s%s" % ("Video Resolution = ",res))
#             else:
#                 print("no metaData available")
      
#     def openFileAtStart(self, filelist):
#             matching = [s for s in filelist if ".myformat" in s]
#             if len(matching) > 0:
#                 self.loadFilm(matching)

# ##################### update Label ##################################
#     def handleLabel(self):
#             self.lbl.clear()
#             mtime = QTime(0,0,0,0)
#             self.time = mtime.addMSecs(self.mediaPlayer.position())
#             self.lbl.setText(self.time.toString())
# ###################################################################

# def stylesheet(self):
#     return """
# QSlider::handle:horizontal 
# {
# background: qlineargradient(x1:0, y1:0, x2:0, y2:1, stop:0 #333, stop:1 #555555);
# width: 14px;
# border-radius: 0px;
# }
# QSlider::groove:horizontal {
# border: 1px solid #444;
# height: 10px;
# background: qlineargradient(x1:0, y1:0, x2:0, y2:1, stop:0 #000, stop:1 #222222);
# }
# QLineEdit
# {
# background: black;
# color: #585858;
# border: 0px solid #076100;
# font-size: 8pt;
# font-weight: bold;
# }
#     """

# if __name__ == '__main__':

# #    QApplication.setDesktopSettingsAware(False)
#     app = QApplication(sys.argv)

#     player = VideoPlayer('')
#     player.setAcceptDrops(True)
#     player.setWindowTitle("QT5 Player")
#     player.setWindowFlags(Qt.FramelessWindowHint | Qt.WindowStaysOnTopHint)
#     player.setGeometry(100, 300, 600, 380)
#     player.setContextMenuPolicy(Qt.CustomContextMenu);
#     player.customContextMenuRequested[QPoint].connect(player.contextMenuRequested)
#     # player.hideSlider()
#     player.show()
#     player.widescreen = True
#     if len(sys.argv) > 1:
#         print(sys.argv[1])
#         player.loadFilm(sys.argv[1])
# sys.exit(app.exec_())




# 3RD PLAYER=======================================
# from PyQt5.QtCore import (pyqtSignal, pyqtSlot, Q_ARG, QAbstractItemModel,
#         QFileInfo, qFuzzyCompare, QMetaObject, QModelIndex, QObject, Qt,
#         QThread, QTime, QUrl)
# from PyQt5.QtGui import QColor, qGray, QImage, QPainter, QPalette
# from PyQt5.QtMultimedia import (QAbstractVideoBuffer, QMediaContent,
#         QMediaMetaData, QMediaPlayer, QMediaPlaylist, QVideoFrame, QVideoProbe)
# from PyQt5.QtMultimediaWidgets import QVideoWidget
# from PyQt5.QtWidgets import (QApplication, QComboBox, QDialog, QFileDialog,
#         QFormLayout, QHBoxLayout, QLabel, QListView, QMessageBox, QPushButton,
#         QSizePolicy, QSlider, QStyle, QToolButton, QVBoxLayout, QWidget)


# class VideoWidget(QVideoWidget):

#     def __init__(self, parent=None):
#         super(VideoWidget, self).__init__(parent)

#         self.setSizePolicy(QSizePolicy.Ignored, QSizePolicy.Ignored)

#         p = self.palette()
#         p.setColor(QPalette.Window, Qt.black)
#         self.setPalette(p)

#         self.setAttribute(Qt.WA_OpaquePaintEvent)

#     def keyPressEvent(self, event):
#         if event.key() == Qt.Key_Escape and self.isFullScreen():
#             self.setFullScreen(False)
#             event.accept()
#         elif event.key() == Qt.Key_Enter and event.modifiers() & Qt.Key_Alt:
#             self.setFullScreen(not self.isFullScreen())
#             event.accept()
#         else:
#             super(VideoWidget, self).keyPressEvent(event)

#     def mouseDoubleClickEvent(self, event):
#         self.setFullScreen(not self.isFullScreen())
#         event.accept()


# class PlaylistModel(QAbstractItemModel):

#     Title, ColumnCount = range(2)

#     def __init__(self, parent=None):
#         super(PlaylistModel, self).__init__(parent)

#         self.m_playlist = None

#     def rowCount(self, parent=QModelIndex()):
#         return self.m_playlist.mediaCount() if self.m_playlist is not None and not parent.isValid() else 0

#     def columnCount(self, parent=QModelIndex()):
#         return self.ColumnCount if not parent.isValid() else 0

#     def index(self, row, column, parent=QModelIndex()):
#         return self.createIndex(row, column) if self.m_playlist is not None and not parent.isValid() and row >= 0 and row < self.m_playlist.mediaCount() and column >= 0 and column < self.ColumnCount else QModelIndex()

#     def parent(self, child):
#         return QModelIndex()

#     def data(self, index, role=Qt.DisplayRole):
#         if index.isValid() and role == Qt.DisplayRole:
#             if index.column() == self.Title:
#                 location = self.m_playlist.media(index.row()).canonicalUrl()
#                 return QFileInfo(location.path()).fileName()

#             return self.m_data[index]

#         return None

#     def playlist(self):
#         return self.m_playlist

#     def setPlaylist(self, playlist):
#         if self.m_playlist is not None:
#             self.m_playlist.mediaAboutToBeInserted.disconnect(
#                     self.beginInsertItems)
#             self.m_playlist.mediaInserted.disconnect(self.endInsertItems)
#             self.m_playlist.mediaAboutToBeRemoved.disconnect(
#                     self.beginRemoveItems)
#             self.m_playlist.mediaRemoved.disconnect(self.endRemoveItems)
#             self.m_playlist.mediaChanged.disconnect(self.changeItems)

#         self.beginResetModel()
#         self.m_playlist = playlist

#         if self.m_playlist is not None:
#             self.m_playlist.mediaAboutToBeInserted.connect(
#                     self.beginInsertItems)
#             self.m_playlist.mediaInserted.connect(self.endInsertItems)
#             self.m_playlist.mediaAboutToBeRemoved.connect(
#                     self.beginRemoveItems)
#             self.m_playlist.mediaRemoved.connect(self.endRemoveItems)
#             self.m_playlist.mediaChanged.connect(self.changeItems)

#         self.endResetModel()

#     def beginInsertItems(self, start, end):
#         self.beginInsertRows(QModelIndex(), start, end)

#     def endInsertItems(self):
#         self.endInsertRows()

#     def beginRemoveItems(self, start, end):
#         self.beginRemoveRows(QModelIndex(), start, end)

#     def endRemoveItems(self):
#         self.endRemoveRows()

#     def changeItems(self, start, end):
#         self.dataChanged.emit(self.index(start, 0),
#                 self.index(end, self.ColumnCount))


# class PlayerControls(QWidget):

#     play = pyqtSignal()
#     pause = pyqtSignal()
#     stop = pyqtSignal()
#     next = pyqtSignal()
#     previous = pyqtSignal()
#     changeVolume = pyqtSignal(int)
#     changeMuting = pyqtSignal(bool)
#     changeRate = pyqtSignal(float)

#     def __init__(self, parent=None):
#         super(PlayerControls, self).__init__(parent)

#         self.playerState = QMediaPlayer.StoppedState
#         self.playerMuted = False

#         self.playButton = QToolButton(clicked=self.playClicked)
#         self.playButton.setIcon(self.style().standardIcon(QStyle.SP_MediaPlay))

#         self.stopButton = QToolButton(clicked=self.stop)
#         self.stopButton.setIcon(self.style().standardIcon(QStyle.SP_MediaStop))
#         self.stopButton.setEnabled(False)

#         self.nextButton = QToolButton(clicked=self.next)
#         self.nextButton.setIcon(
#                 self.style().standardIcon(QStyle.SP_MediaSkipForward))

#         self.previousButton = QToolButton(clicked=self.previous)
#         self.previousButton.setIcon(
#                 self.style().standardIcon(QStyle.SP_MediaSkipBackward))

#         self.muteButton = QToolButton(clicked=self.muteClicked)
#         self.muteButton.setIcon(
#                 self.style().standardIcon(QStyle.SP_MediaVolume))

#         self.volumeSlider = QSlider(Qt.Horizontal,
#                 sliderMoved=self.changeVolume)
#         self.volumeSlider.setRange(0, 100)

#         self.rateBox = QComboBox(activated=self.updateRate)
#         self.rateBox.addItem("0.5x", 0.5)
#         self.rateBox.addItem("1.0x", 1.0)
#         self.rateBox.addItem("2.0x", 2.0)
#         self.rateBox.setCurrentIndex(1)

#         layout = QHBoxLayout()
#         layout.setContentsMargins(0, 0, 0, 0)
#         layout.addWidget(self.stopButton)
#         layout.addWidget(self.previousButton)
#         layout.addWidget(self.playButton)
#         layout.addWidget(self.nextButton)
#         layout.addWidget(self.muteButton)
#         layout.addWidget(self.volumeSlider)
#         layout.addWidget(self.rateBox)
#         self.setLayout(layout)

#     def state(self):
#         return self.playerState

#     def setState(self,state):
#         if state != self.playerState:
#             self.playerState = state

#             if state == QMediaPlayer.StoppedState:
#                 self.stopButton.setEnabled(False)
#                 self.playButton.setIcon(
#                         self.style().standardIcon(QStyle.SP_MediaPlay))
#             elif state == QMediaPlayer.PlayingState:
#                 self.stopButton.setEnabled(True)
#                 self.playButton.setIcon(
#                         self.style().standardIcon(QStyle.SP_MediaPause))
#             elif state == QMediaPlayer.PausedState:
#                 self.stopButton.setEnabled(True)
#                 self.playButton.setIcon(
#                         self.style().standardIcon(QStyle.SP_MediaPlay))

#     def volume(self):
#         return self.volumeSlider.value()

#     def setVolume(self, volume):
#         self.volumeSlider.setValue(volume)

#     def isMuted(self):
#         return self.playerMuted

#     def setMuted(self, muted):
#         if muted != self.playerMuted:
#             self.playerMuted = muted

#             self.muteButton.setIcon(
#                     self.style().standardIcon(
#                             QStyle.SP_MediaVolumeMuted if muted else QStyle.SP_MediaVolume))

#     def playClicked(self):
#         if self.playerState in (QMediaPlayer.StoppedState, QMediaPlayer.PausedState):
#             self.play.emit()
#         elif self.playerState == QMediaPlayer.PlayingState:
#             self.pause.emit()

#     def muteClicked(self):
#         self.changeMuting.emit(not self.playerMuted)

#     def playbackRate(self):
#         return self.rateBox.itemData(self.rateBox.currentIndex())

#     def setPlaybackRate(self, rate):
#         for i in range(self.rateBox.count()):
#             if qFuzzyCompare(rate, self.rateBox.itemData(i)):
#                 self.rateBox.setCurrentIndex(i)
#                 return

#         self.rateBox.addItem("%dx" % rate, rate)
#         self.rateBox.setCurrentIndex(self.rateBox.count() - 1)

#     def updateRate(self):
#         self.changeRate.emit(self.playbackRate())


# class FrameProcessor(QObject):

#     histogramReady = pyqtSignal(list)

#     @pyqtSlot(QVideoFrame, int)
#     def processFrame(self, frame, levels):
#         histogram = [0.0] * levels

#         if levels and frame.map(QAbstractVideoBuffer.ReadOnly):
#             pixelFormat = frame.pixelFormat()

#             if pixelFormat == QVideoFrame.Format_YUV420P or pixelFormat == QVideoFrame.Format_NV12:
#                 # Process YUV data.
#                 bits = frame.bits()
#                 for idx in range(frame.height() * frame.width()):
#                     histogram[(bits[idx] * levels) >> 8] += 1.0
#             else:
#                 imageFormat = QVideoFrame.imageFormatFromPixelFormat(pixelFormat)
#                 if imageFormat != QImage.Format_Invalid:
#                     # Process RGB data.
#                     image = QImage(frame.bits(), frame.width(), frame.height(), imageFormat)

#                     for y in range(image.height()):
#                         for x in range(image.width()):
#                             pixel = image.pixel(x, y)
#                             histogram[(qGray(pixel) * levels) >> 8] += 1.0

#             # Find the maximum value.
#             maxValue = 0.0
#             for value in histogram:
#                 if value > maxValue:
#                     maxValue = value

#             # Normalise the values between 0 and 1.
#             if maxValue > 0.0:
#                 for i in range(len(histogram)):
#                     histogram[i] /= maxValue

#             frame.unmap()

#         self.histogramReady.emit(histogram)


# class HistogramWidget(QWidget):

#     def __init__(self, parent=None):
#         super(HistogramWidget, self).__init__(parent)

#         self.m_levels = 128
#         self.m_isBusy = False
#         self.m_histogram = []
#         self.m_processor = FrameProcessor()
#         self.m_processorThread = QThread()

#         self.m_processor.moveToThread(self.m_processorThread)
#         self.m_processor.histogramReady.connect(self.setHistogram)

#     def __del__(self):
#         self.m_processorThread.quit()
#         self.m_processorThread.wait(10000)

#     def setLevels(self, levels):
#         self.m_levels = levels

#     def processFrame(self, frame):
#         if self.m_isBusy:
#             return

#         self.m_isBusy = True
#         QMetaObject.invokeMethod(self.m_processor, 'processFrame',
#                 Qt.QueuedConnection, Q_ARG(QVideoFrame, frame),
#                 Q_ARG(int, self.m_levels))

#     @pyqtSlot(list)
#     def setHistogram(self, histogram):
#         self.m_isBusy = False
#         self.m_histogram = list(histogram)
#         self.update()

#     def paintEvent(self, event):
#         painter = QPainter(self)

#         if len(self.m_histogram) == 0:
#             painter.fillRect(0, 0, self.width(), self.height(),
#                     QColor.fromRgb(0, 0, 0))
#             return

#         barWidth = self.width() / float(len(self.m_histogram))

#         for i, value in enumerate(self.m_histogram):
#             h = value * self.height()
#             # Draw the level.
#             painter.fillRect(barWidth * i, self.height() - h,
#                     barWidth * (i + 1), self.height(), Qt.red)
#             # Clear the rest of the control.
#             painter.fillRect(barWidth * i, 0, barWidth * (i + 1),
#                     self.height() - h, Qt.black)


# class Player(QWidget):

#     fullScreenChanged = pyqtSignal(bool)

#     def __init__(self, playlist, parent=None):
#         super(Player, self).__init__(parent)

#         self.colorDialog = None
#         self.trackInfo = ""
#         self.statusInfo = ""
#         self.duration = 0

#         self.player = QMediaPlayer()
#         self.playlist = QMediaPlaylist()
#         self.player.setPlaylist(self.playlist)

#         self.player.durationChanged.connect(self.durationChanged)
#         self.player.positionChanged.connect(self.positionChanged)
#         self.player.metaDataChanged.connect(self.metaDataChanged)
#         self.playlist.currentIndexChanged.connect(self.playlistPositionChanged)
#         self.player.mediaStatusChanged.connect(self.statusChanged)
#         self.player.bufferStatusChanged.connect(self.bufferingProgress)
#         self.player.videoAvailableChanged.connect(self.videoAvailableChanged)
#         self.player.error.connect(self.displayErrorMessage)

#         self.videoWidget = VideoWidget()
#         self.player.setVideoOutput(self.videoWidget)

#         self.playlistModel = PlaylistModel()
#         self.playlistModel.setPlaylist(self.playlist)

#         self.playlistView = QListView()
#         self.playlistView.setModel(self.playlistModel)
#         self.playlistView.setCurrentIndex(
#                 self.playlistModel.index(self.playlist.currentIndex(), 0))

#         self.playlistView.activated.connect(self.jump)

#         self.slider = QSlider(Qt.Horizontal)
#         self.slider.setRange(0, self.player.duration() / 1000)

#         self.labelDuration = QLabel()
#         self.slider.sliderMoved.connect(self.seek)

#         self.labelHistogram = QLabel()
#         self.labelHistogram.setText("Histogram:")
#         self.histogram = HistogramWidget()
#         histogramLayout = QHBoxLayout()
#         histogramLayout.addWidget(self.labelHistogram)
#         histogramLayout.addWidget(self.histogram, 1)

#         self.probe = QVideoProbe()
#         self.probe.videoFrameProbed.connect(self.histogram.processFrame)
#         self.probe.setSource(self.player)

#         openButton = QPushButton("Open", clicked=self.open)

#         controls = PlayerControls()
#         controls.setState(self.player.state())
#         controls.setVolume(self.player.volume())
#         controls.setMuted(controls.isMuted())

#         controls.play.connect(self.player.play)
#         controls.pause.connect(self.player.pause)
#         controls.stop.connect(self.player.stop)
#         controls.next.connect(self.playlist.next)
#         controls.previous.connect(self.previousClicked)
#         controls.changeVolume.connect(self.player.setVolume)
#         controls.changeMuting.connect(self.player.setMuted)
#         controls.changeRate.connect(self.player.setPlaybackRate)
#         controls.stop.connect(self.videoWidget.update)

#         self.player.stateChanged.connect(controls.setState)
#         self.player.volumeChanged.connect(controls.setVolume)
#         self.player.mutedChanged.connect(controls.setMuted)

#         self.fullScreenButton = QPushButton("FullScreen")
#         self.fullScreenButton.setCheckable(True)

#         self.colorButton = QPushButton("Color Options...")
#         self.colorButton.setEnabled(False)
#         self.colorButton.clicked.connect(self.showColorDialog)

#         displayLayout = QHBoxLayout()
#         displayLayout.addWidget(self.videoWidget, 2)
#         displayLayout.addWidget(self.playlistView)

#         controlLayout = QHBoxLayout()
#         controlLayout.setContentsMargins(0, 0, 0, 0)
#         controlLayout.addWidget(openButton)
#         controlLayout.addStretch(1)
#         controlLayout.addWidget(controls)
#         controlLayout.addStretch(1)
#         controlLayout.addWidget(self.fullScreenButton)
#         controlLayout.addWidget(self.colorButton)

#         layout = QVBoxLayout()
#         layout.addLayout(displayLayout)
#         hLayout = QHBoxLayout()
#         hLayout.addWidget(self.slider)
#         hLayout.addWidget(self.labelDuration)
#         layout.addLayout(hLayout)
#         layout.addLayout(controlLayout)
#         layout.addLayout(histogramLayout)

#         self.setLayout(layout)

#         if not self.player.isAvailable():
#             QMessageBox.warning(self, "Service not available",
#                     "The QMediaPlayer object does not have a valid service.\n"
#                     "Please check the media service plugins are installed.")

#             controls.setEnabled(False)
#             self.playlistView.setEnabled(False)
#             openButton.setEnabled(False)
#             self.colorButton.setEnabled(False)
#             self.fullScreenButton.setEnabled(False)

#         self.metaDataChanged()

#         self.addToPlaylist(playlist)

#     def open(self):
#         fileNames, _ = QFileDialog.getOpenFileNames(self, "Open Files")
#         self.addToPlaylist(fileNames)

#     def addToPlaylist(self, fileNames):
#         for name in fileNames:
#             fileInfo = QFileInfo(name)
#             if fileInfo.exists():
#                 url = QUrl.fromLocalFile(fileInfo.absoluteFilePath())
#                 if fileInfo.suffix().lower() == 'm3u':
#                     self.playlist.load(url)
#                 else:
#                     self.playlist.addMedia(QMediaContent(url))
#             else:
#                 url = QUrl(name)
#                 if url.isValid():
#                     self.playlist.addMedia(QMediaContent(url))

#     def durationChanged(self, duration):
#         duration /= 1000

#         self.duration = duration
#         self.slider.setMaximum(duration)

#     def positionChanged(self, progress):
#         progress /= 1000

#         if not self.slider.isSliderDown():
#             self.slider.setValue(progress)

#         self.updateDurationInfo(progress)

#     def metaDataChanged(self):
#         if self.player.isMetaDataAvailable():
#             self.setTrackInfo("%s - %s" % (
#                     self.player.metaData(QMediaMetaData.AlbumArtist),
#                     self.player.metaData(QMediaMetaData.Title)))

#     def previousClicked(self):
#         # Go to the previous track if we are within the first 5 seconds of
#         # playback.  Otherwise, seek to the beginning.
#         if self.player.position() <= 5000:
#             self.playlist.previous()
#         else:
#             self.player.setPosition(0)

#     def jump(self, index):
#         if index.isValid():
#             self.playlist.setCurrentIndex(index.row())
#             self.player.play()

#     def playlistPositionChanged(self, position):
#         self.playlistView.setCurrentIndex(
#                 self.playlistModel.index(position, 0))

#     def seek(self, seconds):
#         self.player.setPosition(seconds * 1000)

#     def statusChanged(self, status):
#         self.handleCursor(status)

#         if status == QMediaPlayer.LoadingMedia:
#             self.setStatusInfo("Loading...")
#         elif status == QMediaPlayer.StalledMedia:
#             self.setStatusInfo("Media Stalled")
#         elif status == QMediaPlayer.EndOfMedia:
#             QApplication.alert(self)
#         elif status == QMediaPlayer.InvalidMedia:
#             self.displayErrorMessage()
#         else:
#             self.setStatusInfo("")

#     def handleCursor(self, status):
#         if status in (QMediaPlayer.LoadingMedia, QMediaPlayer.BufferingMedia, QMediaPlayer.StalledMedia):
#             self.setCursor(Qt.BusyCursor)
#         else:
#             self.unsetCursor()

#     def bufferingProgress(self, progress):
#         self.setStatusInfo("Buffering %d%" % progress)

#     def videoAvailableChanged(self, available):
#         if available:
#             self.fullScreenButton.clicked.connect(
#                     self.videoWidget.setFullScreen)
#             self.videoWidget.fullScreenChanged.connect(
#                     self.fullScreenButton.setChecked)

#             if self.fullScreenButton.isChecked():
#                 self.videoWidget.setFullScreen(True)
#         else:
#             self.fullScreenButton.clicked.disconnect(
#                     self.videoWidget.setFullScreen)
#             self.videoWidget.fullScreenChanged.disconnect(
#                     self.fullScreenButton.setChecked)

#             self.videoWidget.setFullScreen(False)

#         self.colorButton.setEnabled(available)

#     def setTrackInfo(self, info):
#         self.trackInfo = info

#         if self.statusInfo != "":
#             self.setWindowTitle("%s | %s" % (self.trackInfo, self.statusInfo))
#         else:
#             self.setWindowTitle(self.trackInfo)

#     def setStatusInfo(self, info):
#         self.statusInfo = info

#         if self.statusInfo != "":
#             self.setWindowTitle("%s | %s" % (self.trackInfo, self.statusInfo))
#         else:
#             self.setWindowTitle(self.trackInfo)

#     def displayErrorMessage(self):
#         self.setStatusInfo(self.player.errorString())

#     def updateDurationInfo(self, currentInfo):
#         duration = self.duration
#         if currentInfo or duration:
#             currentTime = QTime((currentInfo/3600)%60, (currentInfo/60)%60,
#                     currentInfo%60, (currentInfo*1000)%1000)
#             totalTime = QTime((duration/3600)%60, (duration/60)%60,
#                     duration%60, (duration*1000)%1000);

#             format = 'hh:mm:ss' if duration > 3600 else 'mm:ss'
#             tStr = currentTime.toString(format) + " / " + totalTime.toString(format)
#         else:
#             tStr = ""

#         self.labelDuration.setText(tStr)

#     def showColorDialog(self):
#         if self.colorDialog is None:
#             brightnessSlider = QSlider(Qt.Horizontal)
#             brightnessSlider.setRange(-100, 100)
#             brightnessSlider.setValue(self.videoWidget.brightness())
#             brightnessSlider.sliderMoved.connect(
#                     self.videoWidget.setBrightness)
#             self.videoWidget.brightnessChanged.connect(
#                     brightnessSlider.setValue)

#             contrastSlider = QSlider(Qt.Horizontal)
#             contrastSlider.setRange(-100, 100)
#             contrastSlider.setValue(self.videoWidget.contrast())
#             contrastSlider.sliderMoved.connect(self.videoWidget.setContrast)
#             self.videoWidget.contrastChanged.connect(contrastSlider.setValue)

#             hueSlider = QSlider(Qt.Horizontal)
#             hueSlider.setRange(-100, 100)
#             hueSlider.setValue(self.videoWidget.hue())
#             hueSlider.sliderMoved.connect(self.videoWidget.setHue)
#             self.videoWidget.hueChanged.connect(hueSlider.setValue)

#             saturationSlider = QSlider(Qt.Horizontal)
#             saturationSlider.setRange(-100, 100)
#             saturationSlider.setValue(self.videoWidget.saturation())
#             saturationSlider.sliderMoved.connect(
#                     self.videoWidget.setSaturation)
#             self.videoWidget.saturationChanged.connect(
#                     saturationSlider.setValue)

#             layout = QFormLayout()
#             layout.addRow("Brightness", brightnessSlider)
#             layout.addRow("Contrast", contrastSlider)
#             layout.addRow("Hue", hueSlider)
#             layout.addRow("Saturation", saturationSlider)

#             button = QPushButton("Close")
#             layout.addRow(button)

#             self.colorDialog = QDialog(self)
#             self.colorDialog.setWindowTitle("Color Options")
#             self.colorDialog.setLayout(layout)

#             button.clicked.connect(self.colorDialog.close)

#         self.colorDialog.show()


# if __name__ == '__main__':

#     import sys

#     app = QApplication(sys.argv)

#     player = Player(sys.argv[1:])
#     player.show()

#     sys.exit(app.exec_())