#!/usr/bin/env python

import sys
import os

from PyQt4 import QtCore, QtGui
from PIL import Image
from PIL.ImageQt import ImageQt
from lib.binarization import binarize
from lib.skeletonization import skeletonize

PROJECT_PATH = os.path.abspath(os.path.dirname(__file__))

rsrcPath = os.path.join(PROJECT_PATH, "images")
rsrcPathActions = os.path.join(rsrcPath, "actions")


class ScrollArea(QtGui.QScrollArea):
    def wheelEvent(self, event):
        if (event.modifiers() & QtCore.Qt.ControlModifier):
            if event.delta() > 0:
                self.parent().zoomIn()
            if event.delta() < 0:
                self.parent().zoomOut()
        else:
            super(ScrollArea, self).wheelEvent(event)


class SpinBoxDialog(QtGui.QInputDialog):
    def __init__(self, *args, **kwargs):
        super(SpinBoxDialog, self).__init__(*args, **kwargs)


class MainWindow(QtGui.QMainWindow):
    def __init__(self, fileName=None, parent=None):
        super(MainWindow, self).__init__(parent)

        self.setWindowIcon(QtGui.QIcon(rsrcPath + '/logo.png'))
        self.setToolButtonStyle(QtCore.Qt.ToolButtonFollowStyle)
        self.statusBar().showMessage('Ready')
        self.setupFileActions()
        self.setupEditActions()
        self.setupTextActions()
        self.setupBiometriaActions()

        self.isModified = False

        helpMenu = QtGui.QMenu("Help", self)
        self.menuBar().addMenu(helpMenu)
        helpMenu.addAction("About", self.about)
        helpMenu.addAction("About &Qt", QtGui.qApp.aboutQt)

        self.printer = QtGui.QPrinter()

        self.scaleFactor = 0.0

        self.imageLabel = QtGui.QLabel()
        self.imageLabel.setBackgroundRole(QtGui.QPalette.Base)
        self.imageLabel.setSizePolicy(QtGui.QSizePolicy.Ignored,
                                      QtGui.QSizePolicy.Ignored)
        self.imageLabel.setScaledContents(True)

        self.scrollArea = ScrollArea(self)
        self.scrollArea.setBackgroundRole(QtGui.QPalette.Dark)
        self.scrollArea.setWidget(self.imageLabel)
        self.setCentralWidget(self.scrollArea)

        self.setCurrentFileName()

        """
        self.actionSave.setEnabled(self.textEdit.document().isModified())
        self.actionUndo.setEnabled(self.textEdit.document().isUndoAvailable())
        self.actionRedo.setEnabled(self.textEdit.document().isRedoAvailable())
        self.actionUndo.triggered.connect(self.textEdit.undo)
        self.actionRedo.triggered.connect(self.textEdit.redo)
        self.actionCut.setEnabled(False)
        self.actionCopy.setEnabled(False)
        self.actionCut.triggered.connect(self.textEdit.cut)
        self.actionCopy.triggered.connect(self.textEdit.copy)
        self.actionPaste.triggered.connect(self.textEdit.paste)
        """

        #self.fileNew()

    def PIL2QImage(self, pilimage):
        pilimage.convert('RGB')
        return QtGui.QImage(ImageQt(pilimage))

    def PIL2QPixmap(self, pilimage):
        return QtGui.QPixmap.fromImage(self.PIL2QImage(pilimage))

    def closeEvent(self, e):
        if self.maybeSave():
            e.accept()
        else:
            e.ignore()

    def zoomIn(self):
        self.scaleImage(1.25)

    def zoomOut(self):
        self.scaleImage(0.8)

    def normalSize(self):
        self.imageLabel.adjustSize()
        self.scaleFactor = 1.0

    def fitToWindow(self):
        fitToWindow = self.fitToWindowAct.isChecked()
        self.scrollArea.setWidgetResizable(fitToWindow)
        if not fitToWindow:
            self.normalSize()

        self.updateActions()

    def updateActions(self):
        self.zoomInAct.setEnabled(not self.fitToWindowAct.isChecked())
        self.zoomOutAct.setEnabled(not self.fitToWindowAct.isChecked())
        self.normalSizeAct.setEnabled(not self.fitToWindowAct.isChecked())

    def scaleImage(self, factor):
        self.scaleFactor *= factor
        self.imageLabel.resize(
            self.scaleFactor * self.imageLabel.pixmap().size())

        self.adjustScrollBar(self.scrollArea.horizontalScrollBar(), factor)
        self.adjustScrollBar(self.scrollArea.verticalScrollBar(), factor)

        self.zoomInAct.setEnabled(self.scaleFactor < 3.0)
        self.zoomOutAct.setEnabled(self.scaleFactor > 0.333)

    def adjustScrollBar(self, scrollBar, factor):
        scrollBar.setValue(int(factor * scrollBar.value()
                               + ((factor - 1) * scrollBar.pageStep() / 2)))

    def setupBiometriaActions(self):
        tb = QtGui.QToolBar(self)
        tb.setWindowTitle("Biometria")
        self.addToolBar(tb)

        menu = QtGui.QMenu("&Biometria", self)
        self.menuBar().addMenu(menu)

        self.actionBinarize = QtGui.QAction(self, triggered=self.binarize)
        self.actionBinarize.setText("&Binarize")
        self.actionBinarize.setIconText("&Binarize")
        self.actionBinarize.setIcon(QtGui.QIcon(rsrcPathActions + '/filenew.png'))
        self.actionBinarize.setIconVisibleInMenu(True)
        self.actionBinarize.setPriority(QtGui.QAction.LowPriority)
        #self.actionBinarize.setShortcut(QtGui.QKeySequence.New)
        self.actionBinarize.setStatusTip("Binarize image")
        self.actionBinarize.setToolTip("Binarize image")
        self.actionBinarize.setVisible(True)
        tb.addAction(self.actionBinarize)
        menu.addAction(self.actionBinarize)

        self.actionSkeletonize = QtGui.QAction(self, triggered=self.skeletonize)
        self.actionSkeletonize.setText("&Skeletonize")
        self.actionSkeletonize.setIconText("&Skeletonize")
        self.actionSkeletonize.setIcon(QtGui.QIcon(rsrcPathActions + '/filenew.png'))
        self.actionSkeletonize.setIconVisibleInMenu(True)
        self.actionSkeletonize.setPriority(QtGui.QAction.LowPriority)
        #self.actionSkeletonize.setShortcut(QtGui.QKeySequence.New)
        self.actionSkeletonize.setStatusTip("Skeletonize image")
        self.actionSkeletonize.setToolTip("Skeletonize image")
        self.actionSkeletonize.setVisible(True)
        tb.addAction(self.actionSkeletonize)
        menu.addAction(self.actionSkeletonize)

    def setupFileActions(self):
        tb = QtGui.QToolBar(self)
        tb.setWindowTitle("File Actions")
        self.addToolBar(tb)

        menu = QtGui.QMenu("&File", self)
        self.menuBar().addMenu(menu)

        self.actionNew = QtGui.QAction(self, triggered=self.fileNew)
        self.actionNew.setText("&New")
        self.actionNew.setIconText("&New")
        self.actionNew.setIcon(QtGui.QIcon.fromTheme(
            'file-new', QtGui.QIcon(rsrcPathActions + '/filenew.png')))
        self.actionNew.setIconVisibleInMenu(True)
        self.actionNew.setPriority(QtGui.QAction.LowPriority)
        self.actionNew.setShortcut(QtGui.QKeySequence.New)
        self.actionNew.setStatusTip("New file")
        self.actionNew.setToolTip("New file")
        self.actionNew.setVisible(True)
        tb.addAction(self.actionNew)
        menu.addAction(self.actionNew)

        self.actionOpen = QtGui.QAction(
            QtGui.QIcon.fromTheme('document-open',
                                  QtGui.QIcon(rsrcPath + '/fileopen.png')),
            "&Open...", self, shortcut=QtGui.QKeySequence.Open,
            triggered=self.fileOpen)
        tb.addAction(self.actionOpen)
        menu.addAction(self.actionOpen)
        menu.addSeparator()

        self.actionSave = QtGui.QAction(
            QtGui.QIcon.fromTheme('document-save',
                                  QtGui.QIcon(rsrcPath + '/filesave.png')),
            "&Save", self, shortcut=QtGui.QKeySequence.Save,
            triggered=self.fileSave, enabled=False)
        self.actionNew.setStatusTip('Open file')
        tb.addAction(self.actionSave)
        menu.addAction(self.actionSave)

        self.actionSaveAs = QtGui.QAction("Save &As...", self,
                                          priority=QtGui.QAction.LowPriority,
                                          shortcut=QtCore.Qt.CTRL + QtCore.Qt.SHIFT + QtCore.Qt.Key_S,
                                          triggered=self.fileSaveAs)
        menu.addAction(self.actionSaveAs)
        menu.addSeparator()

        self.actionPrint = QtGui.QAction(
            QtGui.QIcon.fromTheme('document-print',
                                  QtGui.QIcon(rsrcPath + '/fileprint.png')),
            "&Print...", self, priority=QtGui.QAction.LowPriority,
            shortcut=QtGui.QKeySequence.Print, triggered=self.filePrint)
        tb.addAction(self.actionPrint)
        menu.addAction(self.actionPrint)

        self.actionPrintPreview = QtGui.QAction(
            QtGui.QIcon.fromTheme('fileprint',
                                  QtGui.QIcon(rsrcPath + '/fileprint.png')),
            "Print Preview...", self,
            shortcut=QtCore.Qt.CTRL + QtCore.Qt.SHIFT + QtCore.Qt.Key_P,
            triggered=self.filePrintPreview)
        menu.addAction(self.actionPrintPreview)

        self.actionPrintPdf = QtGui.QAction(
            QtGui.QIcon.fromTheme('exportpdf',
                                  QtGui.QIcon(rsrcPath + '/exportpdf.png')),
            "&Export PDF...", self, priority=QtGui.QAction.LowPriority,
            shortcut=QtCore.Qt.CTRL + QtCore.Qt.Key_D,
            triggered=self.filePrintPdf)
        tb.addAction(self.actionPrintPdf)
        menu.addAction(self.actionPrintPdf)
        menu.addSeparator()

        self.actionQuit = QtGui.QAction("&Quit", self,
                                        shortcut=QtGui.QKeySequence.Quit, triggered=self.close)
        menu.addAction(self.actionQuit)

    def setupEditActions(self):
        tb = QtGui.QToolBar(self)
        tb.setWindowTitle("Edit Actions")
        self.addToolBar(tb)

        menu = QtGui.QMenu("&Edit", self)
        self.menuBar().addMenu(menu)

        self.actionUndo = QtGui.QAction(
            QtGui.QIcon.fromTheme('edit-undo',
                                  QtGui.QIcon(rsrcPath + '/editundo.png')),
            "&Undo", self, shortcut=QtGui.QKeySequence.Undo)
        tb.addAction(self.actionUndo)
        menu.addAction(self.actionUndo)

        self.actionRedo = QtGui.QAction(
            QtGui.QIcon.fromTheme('edit-redo',
                                  QtGui.QIcon(rsrcPath + '/editredo.png')),
            "&Redo", self, priority=QtGui.QAction.LowPriority,
            shortcut=QtGui.QKeySequence.Redo)
        tb.addAction(self.actionRedo)
        menu.addAction(self.actionRedo)
        menu.addSeparator()

        self.actionCut = QtGui.QAction(
            QtGui.QIcon.fromTheme('edit-cut',
                                  QtGui.QIcon(rsrcPath + '/editcut.png')),
            "Cu&t", self, priority=QtGui.QAction.LowPriority,
            shortcut=QtGui.QKeySequence.Cut)
        tb.addAction(self.actionCut)
        menu.addAction(self.actionCut)

        self.actionCopy = QtGui.QAction(
            QtGui.QIcon.fromTheme('edit-copy',
                                  QtGui.QIcon(rsrcPath + '/editcopy.png')),
            "&Copy", self, priority=QtGui.QAction.LowPriority,
            shortcut=QtGui.QKeySequence.Copy)
        tb.addAction(self.actionCopy)
        menu.addAction(self.actionCopy)

        self.actionPaste = QtGui.QAction(
            QtGui.QIcon.fromTheme('edit-paste',
                                  QtGui.QIcon(rsrcPath + '/editpaste.png')),
            "&Paste", self, priority=QtGui.QAction.LowPriority,
            shortcut=QtGui.QKeySequence.Paste,
            enabled=(len(QtGui.QApplication.clipboard().text()) != 0))
        tb.addAction(self.actionPaste)
        menu.addAction(self.actionPaste)

    def setupTextActions(self):

        self.zoomInAct = QtGui.QAction(
            "Zoom &In (25%)",
            self,
            shortcut="Ctrl++",
            enabled=False,
            triggered=self.zoomIn)

        self.zoomOutAct = QtGui.QAction(
            "Zoom &Out (25%)",
            self,
            shortcut="Ctrl+-",
            enabled=False,
            triggered=self.zoomOut)

        self.normalSizeAct = QtGui.QAction(
            "&Normal Size",
            self,
            shortcut="Ctrl+0",
            enabled=False,
            triggered=self.normalSize)

        self.fitToWindowAct = QtGui.QAction(
            "&Fit to Window",
            self,
            enabled=False,
            checkable=True,
            shortcut="Ctrl+F",
            triggered=self.fitToWindow)

        self.viewMenu = QtGui.QMenu("&View", self)
        self.viewMenu.addAction(self.zoomInAct)
        self.viewMenu.addAction(self.zoomOutAct)
        self.viewMenu.addAction(self.normalSizeAct)
        self.viewMenu.addSeparator()
        self.viewMenu.addAction(self.fitToWindowAct)
        self.menuBar().addMenu(self.viewMenu)

    def binarize(self):
        threshold, ok = QtGui.QInputDialog.getInteger(self, "Binarization", "Threshold", 255 / 2, 0, 255)

        if ok:
            self.current_image = binarize(self.current_image, int(threshold))
            self.updateImage()

    def skeletonize(self):
        self.current_image = skeletonize(self.current_image)
        self.updateImage()

    def updateImage(self):
        image = self.PIL2QImage(self.current_image)
        self.imageLabel.setPixmap(QtGui.QPixmap.fromImage(image))

    def print_(self, printer):
        painter = QtGui.QPainter(printer)
        rect = painter.viewport()
        size = self.imageLabel.pixmap().size()
        size.scale(rect.size(), QtCore.Qt.KeepAspectRatio)
        painter.setViewport(
            rect.x(), rect.y(), size.width(), size.height())
        painter.setWindow(self.imageLabel.pixmap().rect())
        painter.drawPixmap(0, 0, self.imageLabel.pixmap())

    def load(self, fileName):
        if not QtCore.QFile.exists(fileName):
            return False

        self.current_image = Image.open(fileName)

        image = self.PIL2QImage(self.current_image)

        if image.isNull():
            QtGui.QMessageBox.information(self, "Image Viewer",
                                          "Cannot load %s." % fileName)
            return False

        self.imageLabel.setPixmap(QtGui.QPixmap.fromImage(image))
        self.scaleFactor = 1.0

        self.actionPrint.setEnabled(True)
        self.fitToWindowAct.setEnabled(True)
        self.updateActions()

        if not self.fitToWindowAct.isChecked():
            self.imageLabel.adjustSize()
        self.setCurrentFileName(fileName)

    def maybeSave(self):
        if not self.isModified:
            return True

        ret = QtGui.QMessageBox.warning(
            self,
            "Application",
            "The document has been modified.\n"
            "Do you want to save your changes?",
            QtGui.QMessageBox.Save | QtGui.QMessageBox.Discard |
            QtGui.QMessageBox.Cancel)

        if ret == QtGui.QMessageBox.Save:
            return self.fileSave()

        if ret == QtGui.QMessageBox.Cancel:
            return False

        return True

    def setCurrentFileName(self, fileName=''):
        self.fileName = fileName

        if not fileName:
            shownName = 'untitled.txt'
        else:
            shownName = QtCore.QFileInfo(fileName).fileName()

        self.setWindowTitle(self.tr("%s[*] - %s" % (shownName, "Rich Text")))
        self.setWindowModified(False)

    def fileNew(self):
        if self.maybeSave():
            #self.textEdit.clear()
            #TODO: usuwac obrazek
            self.setCurrentFileName()

    def fileOpen(self):
        files = QtGui.QFileDialog.getOpenFileName(
            self,
            "Open File...",
            None,
            "Images (*.jpg *.png *.bmp *.tif *.raw);;All Files (*)")

        if files:
            self.load(fn)

    def fileSave(self):
        #TODO: napisac zapisywanie
        if not self.fileName:
            return self.fileSaveAs()

        success = True

        if success:
            #self.textEdit.document().setModified(False)
            pass

        return success

    def fileSaveAs(self):
        fn = QtGui.QFileDialog.getSaveFileName(
            self,
            "Save as...",
            None,
            "Images (*.png *.jpg);;All Files (*)")

        if not fn:
            return False

        lfn = fn.lower()
        if not lfn.endswith(('.png', '.jpg', '.bmp')):
            # The default.
            fn += '.png'

        self.setCurrentFileName(fn)
        return self.fileSave()

    def filePrint(self):
        printer = QtGui.QPrinter(QtGui.QPrinter.HighResolution)
        dlg = QtGui.QPrintDialog(printer, self)

        dlg.setWindowTitle("Print Document")

        if dlg.exec_() == QtGui.QDialog.Accepted:
            self.print_(printer)

        del dlg

    def filePrintPreview(self):
        printer = QtGui.QPrinter(QtGui.QPrinter.HighResolution)
        preview = QtGui.QPrintPreviewDialog(printer, self)
        preview.paintRequested.connect(self.printPreview)
        preview.exec_()

    def printPreview(self, printer):
        self.print_(printer)

    def filePrintPdf(self):
        fn = QtGui.QFileDialog.getSaveFileName(
            self,
            "Export PDF",
            None,
            "PDF files (*.pdf);;All Files (*)")

        if fn:
            if QtCore.QFileInfo(fn).suffix().isEmpty():
                fn += '.pdf'

            printer = QtGui.QPrinter(QtGui.QPrinter.HighResolution)
            printer.setOutputFormat(QtGui.QPrinter.PdfFormat)
            printer.setOutputFileName(fn)
            self.print_(printer)

    def about(self):
        QtGui.QMessageBox.about(
            self,
            "About",
            "This example demonstrates Qt's rich text editing facilities "
            "in action, providing an example document for you to "
            "experiment with.")


if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)

    mainWindows = []
    for fn in sys.argv[1:] or [None]:
        mw = MainWindow(fn)
        mw.resize(700, 800)
        mw.show()
        mainWindows.append(mw)

    sys.exit(app.exec_())
