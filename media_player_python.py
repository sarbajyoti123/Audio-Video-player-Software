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






