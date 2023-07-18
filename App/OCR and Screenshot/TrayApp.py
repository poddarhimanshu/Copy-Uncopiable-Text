import sys
from PyQt5 import QtWidgets as qtw, QtGui as qtg
from Main import *

class SystemTrayIcon(qtw.QSystemTrayIcon):

    window = None

    def __init__(self, icon, parent=None):
        qtw.QSystemTrayIcon.__init__(self, icon, parent)

        # set context menu, this menu opens on right clicking the tray
        self.menu = qtw.QMenu()
        # Add Quit option to the menu and connect to close slot
        self.menu.addAction('Quit', self.close, qtg.QKeySequence.Quit)
        self.setContextMenu(self.menu)

        # Whenever the icon is clicked activated signal is emitted, takeActionOnIconClick slot will be run
        self.activated.connect(self.takeActionOnIconClick)

        self.show()

    def close(self):
        sys.exit(0)

    def takeActionOnIconClick(self, reason):

        # close any previous window created
        if self.window:
            self.window.close()
            self.window = None

        if reason == qtw.QSystemTrayIcon.MiddleClick:
            self.window = MainWindow(operation = AppUtilities.SCREENSHOT)
            self.window.closing.connect(self.handleMainWindowClose)
            
        elif reason == qtw.QSystemTrayIcon.Trigger:
            # launch the main app
            self.window = MainWindow(operation = AppUtilities.OCR)
            self.window.closing.connect(self.handleMainWindowClose)
    
    def handleMainWindowClose(self):
        # Do whatever you want when the MainWindow is about to close
        pass

def main(image):

    app = qtw.QApplication(sys.argv)

    w = qtw.QWidget()
    trayIcon = SystemTrayIcon(qtg.QIcon(image), w)

    # do not take action of quit sent by the MainWindow
    app.setQuitOnLastWindowClosed(False)
    sys.exit(app.exec_())

if __name__ == '__main__':
    icon = './resources/icon.png'
    main(icon)