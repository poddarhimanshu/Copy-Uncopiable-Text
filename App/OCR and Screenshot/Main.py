# For creating GUI
from PyQt5.QtWidgets import QMainWindow, QApplication, QWidget
from PyQt5.QtCore import Qt, pyqtSignal, QRect, QSize
from PyQt5.QtGui import QPainter, QColor, QPainter, QBrush, QColor, QPalette


from enum import Enum
import pyperclip
import sys

# Utility classes
from Screenshot import Screenshot
from OCR import TesseractOCR


SCREENSHOT_NAME = './resources/screenshot.png'

class AppUtilities(Enum):
    OCR = 1
    SCREENSHOT = 2


class MainWindow(QMainWindow): 
    mouseRelease = 0
    # any app can use the close signal emitted by this app
    closing = pyqtSignal()

    def __init__(self, *arg, **kwargs):
        super().__init__()
        
        self.operation = kwargs['operation'] if 'operation' in kwargs else AppUtilities.OCR
        self.setWindowFlags(self.windowFlags() | Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground)

        borderWidget = QWidget(objectName='borderWidget')
        self.setCentralWidget(borderWidget)
        
        bgd = self.palette().color(QPalette.Window)
        bgd.setAlphaF(.005)
        self.setStyleSheet('''
            #borderWidget {{
                border: 3px solid blue;
                background: {bgd};
            }}
        '''.format(bgd=bgd.name(bgd.HexArgb)))
        self.captureRect = None
        self.makeRectangleTransparent = False

        self.showFullScreen()

        self.setCursor(Qt.CrossCursor)

    # paint event is called whenever any changes happen to window including left button being pressed etc
    def paintEvent(self, event):
        # makeRectangleTransparent becomes true when we have released the mouse and about to take screenshot of the captured rectangle
        if self.makeRectangleTransparent:
            qpbox = QPainter(self)
            br = QBrush(QColor(0, 0, 0, 0))  
            qpbox.setBrush(br)   
            qpbox.drawRect(self.captureRect)
            
        elif self.captureRect:
            qpbox = QPainter(self)
            br = QBrush(QColor(100, 10, 10, 40))  
            qpbox.setBrush(br)   
            qpbox.drawRect(self.captureRect)
            
    def mouseReleaseEvent(self, event):
        # close on right click release
        if event.button() == Qt.RightButton:
            self.close()
        # when left button is released its time to do our OCR/image copy
        elif event.button() == Qt.LeftButton:
            # make the area transparent by calling repaint and take screenshot
            self.makeRectangleTransparent = True
            self.repaint()

            screen = QApplication.primaryScreen()
            img = screen.grabWindow(0, *self.captureRect.getRect())
            img.save(SCREENSHOT_NAME, 'png')

            # if you want to show the image captured, uncomment these lines
            '''
            label = QLabel(self)
            label.setPixmap(img)
            self.setStyleSheet('')
            self.setCentralWidget(label)
            self.resize(img.width(), img.height())
            self.captureRect = None
            '''
            
            if self.operation == AppUtilities.OCR:
                # copy text to the clipboard
                textPredicted = TesseractOCR.GetText(SCREENSHOT_NAME)
                pyperclip.copy(textPredicted)
            elif self.operation == AppUtilities.SCREENSHOT:
                Screenshot.CopyImageToClipBoard(SCREENSHOT_NAME)

            # close the window
            self.close()

    def closeEvent(self, event):
        
        # Emit close event for the system tray app to use it to take any further action
        self.closing.emit()

    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.begin = event.pos()
            self.captureRect = QRect(self.begin, QSize())


    def mouseMoveEvent(self, event):
        # captureRect will store the rectangle on mouse move starting from beginning to the mouse position(current)
        self.captureRect = QRect(self.begin, event.pos()).normalized()
        self.update()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = MainWindow()
    sys.exit(app.exec_())