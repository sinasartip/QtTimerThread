from PySide2 import QtWidgets, QtCore
from PySide2.QtCore import SIGNAL, qDebug, SLOT
from Ui_mainwindow import Ui_MainWindow
import sys
import time
import threading 


class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        
        self.ui.Start_PB.clicked.connect(self.setup_browserThread)
    
    def setup_browserSignals(self):
        self.txtBrowser.timer_done.connect(lambda: self.txtBrowser.update())
        self.txtBrowser.timer_stop.connect(self.txtBrowser.stop_timer)
        self.txtBrowser.error.connect(self.print_err)
        self.txtBrowser.finished.connect(self.thread.quit)
        #self.txtBrowser.finished.connect(self.txtBrowser.deleteLater)

    def setup_browserThread(self):
        self.txtBrowser = Browser(self.ui.Display_Brws, 1)
        self.ui.Stop_PB.clicked.connect(lambda: self.txtBrowser.stop())
        self.thread = QtCore.QThread()
        self.txtBrowser.moveToThread(self.thread)
        self.thread.started.connect(self.txtBrowser.start)   
        self.thread.finished.connect(self.thread.deleteLater)
        self.setup_browserSignals()
        self.thread.start()

    @QtCore.Slot(str)
    def print_err(self, err: str):
        print(f"message from print_err: {err}")

    
class Browser(QtCore.QObject):
    finished = QtCore.Signal()
    error = QtCore.Signal(str)
    timer_done = QtCore.Signal()
    timer_stop = QtCore.Signal()

    def __init__(self, widget : QtWidgets.QTextBrowser, time_to_sleep):
        QtCore.QObject.__init__(self)
        self.browser = widget
        self.first = True
        
        self.append_text = self.browser.append
        self.set_text = self.browser.setText
        self.time_to_sleep = time_to_sleep

    def setup_timer(self):
        self.timer = QtCore.QTimer()
        self.timer.setTimerType(QtCore.Qt.PreciseTimer)
        self.timer.timeout.connect(self.timer_done.emit)
        self.prev_time = time.monotonic()

    def start(self):
        self.error.emit(f"start method in thread: {threading.get_ident()}")
        self.setup_timer()
        self.timer.start(self.time_to_sleep)
        loop = QtCore.QEventLoop()
        loop.exec_()

    @QtCore.Slot()
    def update(self):
        if self.first:
            self.error.emit(f"update method in thread: {threading.get_ident()}")
            self.first = False
        self.curr_time = time.monotonic()
        self.append_text(f"the process took: {self.curr_time - self.prev_time}")
        self.prev_time = self.curr_time

    @QtCore.Slot()    
    def stop_timer(self):
        self.error.emit(f"stop_timer method in thread: {threading.get_ident()}")
        self.timer.stop()

    def stop(self):
        self.error.emit(f"stop method in thread: {threading.get_ident()}")
        self.timer_stop.emit()
        self.finished.emit()
        

if __name__ == "__main__":
    print(f"thread for main : {threading.get_ident()}")
    app = QtWidgets.QApplication()
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
    