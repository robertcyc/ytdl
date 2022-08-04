from PyQt5 import QtWidgets,QtCore
from PyQt5.QtCore import QTimer,QThread
from PyQt5.QtGui import QTextCursor
from ui import Ui_MainWindow
import time
import sys,os
import youtube_dl
import images_rc
import webbrowser
import datetime
import psutil
from pytube import YouTube
#TODO
# pyinstaller --clean --onefile --noconsole  --icon=youtube.ico ytdl.py

class myWindows(QtWidgets.QMainWindow):
    def __init__(self):
    #++++++++++++++++++++++++++++++++
    #+ Create the windows form
    #++++++++++++++++++++++++++++++++
        super().__init__()
        self.ui=Ui_MainWindow()
        self.ui.setupUi(self)
        # +++++++++++++++++++++++++++++++++++++++++++++
        # System properties
        # +++++++++++++++++++++++++++++++++++++++++++++
        self.currPath = os.getcwd()
        self.gDT = time.strftime("[%Y-%m-%d %H:%M:%S] ")
        self.appStartTime = time.strftime("%Y-%m-%d %H:%M:%S")
        #++++++++++++++++++++++++++++++++++++++++++++++
        # setup Timer
        # +++++++++++++++++++++++++++++++++++++++++++++
        self.timeCounter=0
        self.delayTime=500
        self.myTimer=QTimer()
        self.myTimer.start(self.delayTime)
        self.myTimer.timeout.connect(self.winTimer)

        # +++++++++++++++++++++++++++++++++++++++++++++++
        # Windwos properties
        #++++++++++++++++++++++++++++++++++++++++++++++++
        self.setWindowFlag(QtCore.Qt.WindowMaximizeButtonHint, False)
        #+++++++++++++++++++++++++++++++++++++++++++++++
        # Button properties
        # ++++++++++++++++++++++++++++++++++++++++++++++
        self.ui.pushButton.setEnabled(True)
        self.ui.pushButton.setStyleSheet("background-color: green ; color:white ; font:bold 12px")

        self.ui.pushButton_2.setEnabled(True)
        self.ui.pushButton_2.setStyleSheet("background-color: green ; color:white ; font:bold 12px")

        self.ui.pushButton_3.setEnabled(True)
        self.ui.pushButton_3.setStyleSheet("background-color: green ; color:white ; font:bold 12px")

    def bootingTime(self):
        bootTime = str(datetime.datetime.fromtimestamp(psutil.boot_time()))
        return bootTime

    def upTime(self):
        Seconds = int(time.time()) - int(psutil.boot_time())
        m, s = divmod(Seconds, 60)
        h, m = divmod(m, 60)
        d, h = divmod(h, 24)
        upTimeTotal = str(d) + " Day " + str(h) + " Hour " + str(m) + " Min " + str(s) + " Sec"
        return upTimeTotal

    def yearCountDown(self):
        year = datetime.datetime.today().year
        mon = 12
        day = 31
        remainDays = datetime.datetime(year, mon, day).replace(microsecond=0) - datetime.datetime.today().replace(microsecond=0)
        return remainDays

    def winTimer(self):
        self.gDT = time.strftime("%Y-%m-%d %H:%M:%S")
        self.ui.statusbar.showMessage("電腦運行時間: {} | 程式啟動時間: {} | 檔案路徑:{}".format(self.upTime(),self.appStartTime,self.currPath))
        self.setWindowTitle("今年剩餘時間: {} | robertcyc@gmail.com".format(self.yearCountDown()))

    def ytdl(self,url):
        try:
            #+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
            # Download MP3
            #+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

            targetPath=self.currPath
            yt=YouTube(url)
            video=yt.streams.filter(only_audio=True).first()
            self.ui.textBrowser.append("[{}] 檔案名稱: {}".format(self.gDT,yt.title))
            self.ui.textBrowser.append("[{}] MP3 音樂下載中...".format(self.gDT))
            outFile=video.download(output_path=targetPath)
            base,ext=os.path.splitext(outFile)
            newFile=base+'.mp3'
            os.rename(outFile,newFile)
            self.ui.textBrowser.append("[{}] MP3 音樂下載完成.".format(self.gDT))

            # +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
            # Download MP4
            # +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
            self.ui.textBrowser.append("[{}] MP4 影片下載中...".format(self.gDT))
            targetPath = self.currPath
            yt = YouTube(url)
            video = yt.streams.filter(progressive=True,only_audio=False).order_by('resolution').desc().first()
            outFile = video.download(output_path=targetPath)
            base, ext = os.path.splitext(outFile)
            newFile = base + '.mp4'
            os.rename(outFile, newFile)
            self.ui.textBrowser.append("[{}] MP4 影片下載完成.".format(self.gDT))

            # ydl_opts_mp4 = {}
            # with youtube_dl.YoutubeDL(ydl_opts_mp4) as ydl:
            #     infoDict = ydl.extract_info(url, download=False)
            #     videoTitle=infoDict.get('title')
            #     self.ui.textBrowser.append("[{}] MP4 影片下載中... {}".format(self.gDT,videoTitle))
            #     ydl.download([url])
            # self.ui.textBrowser.append("[{}] MP4 影片下載完成.".format(self.gDT))

        except Exception as err:
            self.ui.textBrowser.append("[{}] {}".format(self.gDT,err))

    def ui_youtubeWebsite(self):
        url="https://www.youtube.com"
        webbrowser.open_new(url)
        pass

    def ui_youtubeDL1(self):
        self.ui.pushButton.setEnabled(False)
        self.ui.pushButton.setStyleSheet("background-color: red ; color:white ; font:bold 12px")
        self.ytdl1=youtubeDL1(self)
        self.ytdl1.tdRun=1
        self.ytdl1.start()
        pass

    def ui_youtubeDL2(self):
        self.ui.pushButton_2.setEnabled(False)
        self.ui.pushButton_2.setStyleSheet("background-color: red ; color:white ; font:bold 12px")
        self.ytdl2=youtubeDL2(self)
        self.ytdl2.tdRun=1
        self.ytdl2.start()
        pass

    def ui_youtubeDL3(self):
        self.ui.pushButton_3.setEnabled(False)
        self.ui.pushButton_3.setStyleSheet("background-color: red ; color:white ; font:bold 12px")
        self.ytdl3=youtubeDL3(self)
        self.ytdl3.tdRun=1
        self.ytdl3.start()
        pass


class youtubeDL1(QThread):
    def __init__(self,parent=None):
        super().__init__(parent)
        self.inheritWin=myWindows()
        self.tdRun=0
        pass

    def run(self):
        startTime=time.time()
        url=self.parent().ui.lineEdit.text()
        #self.parent().ui.textBrowser.append("[{}] Downloading from {}".format(self.parent().gDT,url))
        self.parent().ytdl(url)
        # self.parent().ui.textBrowser.append("[{}] Download completed.".format(self.parent().gDT))
        self.parent().ui.pushButton.setEnabled(True)
        self.parent().ui.pushButton.setStyleSheet("background-color: green ; color:white ; font:bold 12px")
        self.tdRun = 0
        endTime=time.time()
        elaspedTime=round((endTime-startTime),1)
        self.parent().ui.textBrowser.append("[{}] {} /下載花費時間: {} seconds.".format(self.parent().gDT,url,elaspedTime))
        self.parent().ui.lineEdit.clear()

class youtubeDL2(QThread):
    def __init__(self,parent=None):
        super().__init__(parent)
        self.inheritWin=myWindows()
        self.tdRun=0
        pass

    def run(self):
        startTime=time.time()
        url=self.parent().ui.lineEdit_2.text()
        #self.parent().ui.textBrowser.append("[{}] Downloading from {}".format(self.parent().gDT,url))
        self.parent().ytdl(url)
        # self.parent().ui.textBrowser.append("[{}] Download completed.".format(self.parent().gDT))
        self.parent().ui.pushButton_2.setEnabled(True)
        self.parent().ui.pushButton_2.setStyleSheet("background-color: green ; color:white ; font:bold 12px")
        self.tdRun = 0
        endTime = time.time()
        elaspedTime = round((endTime - startTime), 1)
        self.parent().ui.textBrowser.append("[{}] {} /下載花費時間: {} seconds.".format(self.parent().gDT, url, elaspedTime))
        self.parent().ui.lineEdit_2.clear()

class youtubeDL3(QThread):
    def __init__(self,parent=None):
        super().__init__(parent)
        self.inheritWin=myWindows()
        self.tdRun=0
        pass

    def run(self):
        startTime=time.time()
        url=self.parent().ui.lineEdit_3.text()
        #self.parent().ui.textBrowser.append("[{}] Downloading from {}".format(self.parent().gDT,url))
        self.parent().ytdl(url)
        # self.parent().ui.textBrowser.append("[{}] Download completed.".format(self.parent().gDT))
        self.parent().ui.pushButton_3.setEnabled(True)
        self.parent().ui.pushButton_3.setStyleSheet("background-color: green ; color:white ; font:bold 12px")
        self.tdRun = 0
        endTime = time.time()
        elaspedTime = round((endTime - startTime), 1)
        self.parent().ui.textBrowser.append("[{}] {} /下載花費時間: {} seconds.".format(self.parent().gDT, url, elaspedTime))
        self.parent().ui.lineEdit_3.clear()

def main():
    app=QtWidgets.QApplication([])
    application=myWindows()
    application.show()
    sys.exit(app.exec())

# script starts from here

if __name__=="__main__":
    main()
