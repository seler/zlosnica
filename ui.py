# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'zlosnica/zlosnica.ui'
#
# Created: Thu Oct 17 01:19:21 2013
#      by: PyQt4 UI code generator 4.9.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(700, 496)
        MainWindow.setMinimumSize(QtCore.QSize(700, 0))
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.gridLayout = QtGui.QGridLayout(self.centralwidget)
        self.gridLayout.setContentsMargins(-1, -1, 0, -1)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.labelSizeSpinBox = QtGui.QSpinBox(self.centralwidget)
        self.labelSizeSpinBox.setEnabled(False)
        self.labelSizeSpinBox.setMinimum(1)
        self.labelSizeSpinBox.setMaximum(100)
        self.labelSizeSpinBox.setProperty("value", 30)
        self.labelSizeSpinBox.setObjectName(_fromUtf8("labelSizeSpinBox"))
        self.gridLayout.addWidget(self.labelSizeSpinBox, 9, 1, 1, 1)
        self.labelFileLabel = QtGui.QLabel(self.centralwidget)
        self.labelFileLabel.setEnabled(False)
        self.labelFileLabel.setObjectName(_fromUtf8("labelFileLabel"))
        self.gridLayout.addWidget(self.labelFileLabel, 8, 0, 1, 1)
        self.inputDirLabel = QtGui.QLabel(self.centralwidget)
        self.inputDirLabel.setObjectName(_fromUtf8("inputDirLabel"))
        self.gridLayout.addWidget(self.inputDirLabel, 0, 0, 1, 1)
        self.outputDirLabel = QtGui.QLabel(self.centralwidget)
        self.outputDirLabel.setObjectName(_fromUtf8("outputDirLabel"))
        self.gridLayout.addWidget(self.outputDirLabel, 1, 0, 1, 1)
        self.labelFilePushButton = QtGui.QPushButton(self.centralwidget)
        self.labelFilePushButton.setEnabled(False)
        self.labelFilePushButton.setObjectName(_fromUtf8("labelFilePushButton"))
        self.gridLayout.addWidget(self.labelFilePushButton, 8, 2, 1, 1)
        self.labelFileLineEdit = QtGui.QLineEdit(self.centralwidget)
        self.labelFileLineEdit.setEnabled(False)
        self.labelFileLineEdit.setObjectName(_fromUtf8("labelFileLineEdit"))
        self.gridLayout.addWidget(self.labelFileLineEdit, 8, 1, 1, 1)
        self.labelSizeLabel = QtGui.QLabel(self.centralwidget)
        self.labelSizeLabel.setEnabled(False)
        self.labelSizeLabel.setObjectName(_fromUtf8("labelSizeLabel"))
        self.gridLayout.addWidget(self.labelSizeLabel, 9, 0, 1, 1)
        self.maxWidthLabel = QtGui.QLabel(self.centralwidget)
        self.maxWidthLabel.setEnabled(False)
        self.maxWidthLabel.setObjectName(_fromUtf8("maxWidthLabel"))
        self.gridLayout.addWidget(self.maxWidthLabel, 5, 0, 1, 1)
        self.maxHeightLabel = QtGui.QLabel(self.centralwidget)
        self.maxHeightLabel.setEnabled(False)
        self.maxHeightLabel.setObjectName(_fromUtf8("maxHeightLabel"))
        self.gridLayout.addWidget(self.maxHeightLabel, 6, 0, 1, 1)
        self.inputDirPushButton = QtGui.QPushButton(self.centralwidget)
        self.inputDirPushButton.setObjectName(_fromUtf8("inputDirPushButton"))
        self.gridLayout.addWidget(self.inputDirPushButton, 0, 2, 1, 1)
        self.inputDirLineEdit = QtGui.QLineEdit(self.centralwidget)
        self.inputDirLineEdit.setObjectName(_fromUtf8("inputDirLineEdit"))
        self.gridLayout.addWidget(self.inputDirLineEdit, 0, 1, 1, 1)
        self.maxHeightSpinBox = QtGui.QSpinBox(self.centralwidget)
        self.maxHeightSpinBox.setEnabled(False)
        self.maxHeightSpinBox.setMinimum(10)
        self.maxHeightSpinBox.setMaximum(5000)
        self.maxHeightSpinBox.setProperty("value", 1200)
        self.maxHeightSpinBox.setObjectName(_fromUtf8("maxHeightSpinBox"))
        self.gridLayout.addWidget(self.maxHeightSpinBox, 6, 1, 1, 1)
        self.outputDirLineEdit = QtGui.QLineEdit(self.centralwidget)
        self.outputDirLineEdit.setObjectName(_fromUtf8("outputDirLineEdit"))
        self.gridLayout.addWidget(self.outputDirLineEdit, 1, 1, 1, 1)
        self.changeNameCheckBox = QtGui.QCheckBox(self.centralwidget)
        self.changeNameCheckBox.setEnabled(True)
        self.changeNameCheckBox.setChecked(False)
        self.changeNameCheckBox.setObjectName(_fromUtf8("changeNameCheckBox"))
        self.gridLayout.addWidget(self.changeNameCheckBox, 2, 1, 1, 1)
        self.outputDirPushButton = QtGui.QPushButton(self.centralwidget)
        self.outputDirPushButton.setObjectName(_fromUtf8("outputDirPushButton"))
        self.gridLayout.addWidget(self.outputDirPushButton, 1, 2, 1, 1)
        self.changeNameLineEdit = QtGui.QLineEdit(self.centralwidget)
        self.changeNameLineEdit.setEnabled(False)
        self.changeNameLineEdit.setObjectName(_fromUtf8("changeNameLineEdit"))
        self.gridLayout.addWidget(self.changeNameLineEdit, 3, 1, 1, 1)
        self.changeNameLabel = QtGui.QLabel(self.centralwidget)
        self.changeNameLabel.setEnabled(False)
        self.changeNameLabel.setObjectName(_fromUtf8("changeNameLabel"))
        self.gridLayout.addWidget(self.changeNameLabel, 3, 0, 1, 1)
        self.insertLabelCheckBox = QtGui.QCheckBox(self.centralwidget)
        self.insertLabelCheckBox.setChecked(False)
        self.insertLabelCheckBox.setObjectName(_fromUtf8("insertLabelCheckBox"))
        self.gridLayout.addWidget(self.insertLabelCheckBox, 7, 1, 1, 1)
        self.processFIlesPushButton = QtGui.QPushButton(self.centralwidget)
        self.processFIlesPushButton.setEnabled(True)
        self.processFIlesPushButton.setObjectName(_fromUtf8("processFIlesPushButton"))
        self.gridLayout.addWidget(self.processFIlesPushButton, 10, 1, 1, 1)
        self.processProgressBar = QtGui.QProgressBar(self.centralwidget)
        self.processProgressBar.setEnabled(False)
        self.processProgressBar.setProperty("value", 0)
        self.processProgressBar.setInvertedAppearance(False)
        self.processProgressBar.setObjectName(_fromUtf8("processProgressBar"))
        self.gridLayout.addWidget(self.processProgressBar, 11, 1, 1, 1)
        self.maxWidthSpinBox = QtGui.QSpinBox(self.centralwidget)
        self.maxWidthSpinBox.setEnabled(False)
        self.maxWidthSpinBox.setMinimum(10)
        self.maxWidthSpinBox.setMaximum(5000)
        self.maxWidthSpinBox.setProperty("value", 1200)
        self.maxWidthSpinBox.setObjectName(_fromUtf8("maxWidthSpinBox"))
        self.gridLayout.addWidget(self.maxWidthSpinBox, 5, 1, 1, 1)
        self.changeSizeCheckBox = QtGui.QCheckBox(self.centralwidget)
        self.changeSizeCheckBox.setChecked(False)
        self.changeSizeCheckBox.setObjectName(_fromUtf8("changeSizeCheckBox"))
        self.gridLayout.addWidget(self.changeSizeCheckBox, 4, 1, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 700, 29))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)
        self.actionProcessFiles = QtGui.QAction(MainWindow)
        self.actionProcessFiles.setObjectName(_fromUtf8("actionProcessFiles"))
        self.actionPreProcessFiles = QtGui.QAction(MainWindow)
        self.actionPreProcessFiles.setObjectName(_fromUtf8("actionPreProcessFiles"))
        self.actionFilesProcessed = QtGui.QAction(MainWindow)
        self.actionFilesProcessed.setObjectName(_fromUtf8("actionFilesProcessed"))
        self.labelFileLabel.setBuddy(self.labelFileLineEdit)
        self.inputDirLabel.setBuddy(self.inputDirLineEdit)
        self.outputDirLabel.setBuddy(self.outputDirLineEdit)
        self.labelSizeLabel.setBuddy(self.labelSizeSpinBox)
        self.maxWidthLabel.setBuddy(self.maxWidthSpinBox)
        self.maxHeightLabel.setBuddy(self.maxHeightSpinBox)
        self.changeNameLabel.setBuddy(self.changeNameLineEdit)

        self.retranslateUi(MainWindow)
        QtCore.QObject.connect(self.changeNameCheckBox, QtCore.SIGNAL(_fromUtf8("clicked(bool)")), self.changeNameLineEdit.setEnabled)
        QtCore.QObject.connect(self.changeNameCheckBox, QtCore.SIGNAL(_fromUtf8("clicked(bool)")), self.changeNameLabel.setEnabled)
        QtCore.QObject.connect(self.changeSizeCheckBox, QtCore.SIGNAL(_fromUtf8("clicked(bool)")), self.maxWidthLabel.setEnabled)
        QtCore.QObject.connect(self.changeSizeCheckBox, QtCore.SIGNAL(_fromUtf8("clicked(bool)")), self.maxWidthSpinBox.setEnabled)
        QtCore.QObject.connect(self.changeSizeCheckBox, QtCore.SIGNAL(_fromUtf8("clicked(bool)")), self.maxHeightLabel.setEnabled)
        QtCore.QObject.connect(self.changeSizeCheckBox, QtCore.SIGNAL(_fromUtf8("clicked(bool)")), self.maxHeightSpinBox.setEnabled)
        QtCore.QObject.connect(self.insertLabelCheckBox, QtCore.SIGNAL(_fromUtf8("clicked(bool)")), self.labelFileLabel.setEnabled)
        QtCore.QObject.connect(self.insertLabelCheckBox, QtCore.SIGNAL(_fromUtf8("clicked(bool)")), self.labelFileLineEdit.setEnabled)
        QtCore.QObject.connect(self.insertLabelCheckBox, QtCore.SIGNAL(_fromUtf8("clicked(bool)")), self.labelSizeLabel.setEnabled)
        QtCore.QObject.connect(self.insertLabelCheckBox, QtCore.SIGNAL(_fromUtf8("clicked(bool)")), self.labelSizeSpinBox.setEnabled)
        QtCore.QObject.connect(self.insertLabelCheckBox, QtCore.SIGNAL(_fromUtf8("clicked(bool)")), self.labelFilePushButton.setEnabled)
        QtCore.QObject.connect(self.processFIlesPushButton, QtCore.SIGNAL(_fromUtf8("clicked()")), self.actionPreProcessFiles.trigger)
        QtCore.QObject.connect(self.actionProcessFiles, QtCore.SIGNAL(_fromUtf8("triggered(bool)")), self.inputDirLineEdit.setEnabled)
        QtCore.QObject.connect(self.actionProcessFiles, QtCore.SIGNAL(_fromUtf8("triggered(bool)")), self.changeNameCheckBox.setEnabled)
        QtCore.QObject.connect(self.actionProcessFiles, QtCore.SIGNAL(_fromUtf8("triggered(bool)")), self.changeNameLabel.setEnabled)
        QtCore.QObject.connect(self.actionProcessFiles, QtCore.SIGNAL(_fromUtf8("triggered(bool)")), self.changeNameLineEdit.setEnabled)
        QtCore.QObject.connect(self.actionProcessFiles, QtCore.SIGNAL(_fromUtf8("triggered(bool)")), self.changeSizeCheckBox.setEnabled)
        QtCore.QObject.connect(self.actionProcessFiles, QtCore.SIGNAL(_fromUtf8("triggered(bool)")), self.inputDirLabel.setEnabled)
        QtCore.QObject.connect(self.actionProcessFiles, QtCore.SIGNAL(_fromUtf8("triggered(bool)")), self.inputDirPushButton.setEnabled)
        QtCore.QObject.connect(self.actionProcessFiles, QtCore.SIGNAL(_fromUtf8("triggered(bool)")), self.insertLabelCheckBox.setEnabled)
        QtCore.QObject.connect(self.actionProcessFiles, QtCore.SIGNAL(_fromUtf8("triggered(bool)")), self.labelFileLabel.setEnabled)
        QtCore.QObject.connect(self.actionProcessFiles, QtCore.SIGNAL(_fromUtf8("triggered(bool)")), self.labelFileLineEdit.setEnabled)
        QtCore.QObject.connect(self.actionProcessFiles, QtCore.SIGNAL(_fromUtf8("triggered(bool)")), self.labelFilePushButton.setEnabled)
        QtCore.QObject.connect(self.actionProcessFiles, QtCore.SIGNAL(_fromUtf8("triggered(bool)")), self.labelSizeLabel.setEnabled)
        QtCore.QObject.connect(self.actionProcessFiles, QtCore.SIGNAL(_fromUtf8("triggered(bool)")), self.labelSizeSpinBox.setEnabled)
        QtCore.QObject.connect(self.actionProcessFiles, QtCore.SIGNAL(_fromUtf8("triggered(bool)")), self.maxHeightLabel.setEnabled)
        QtCore.QObject.connect(self.actionProcessFiles, QtCore.SIGNAL(_fromUtf8("triggered(bool)")), self.maxHeightSpinBox.setEnabled)
        QtCore.QObject.connect(self.actionProcessFiles, QtCore.SIGNAL(_fromUtf8("triggered(bool)")), self.maxWidthLabel.setEnabled)
        QtCore.QObject.connect(self.actionProcessFiles, QtCore.SIGNAL(_fromUtf8("triggered(bool)")), self.maxWidthSpinBox.setEnabled)
        QtCore.QObject.connect(self.actionProcessFiles, QtCore.SIGNAL(_fromUtf8("triggered(bool)")), self.outputDirLabel.setEnabled)
        QtCore.QObject.connect(self.actionProcessFiles, QtCore.SIGNAL(_fromUtf8("triggered(bool)")), self.outputDirLineEdit.setEnabled)
        QtCore.QObject.connect(self.actionProcessFiles, QtCore.SIGNAL(_fromUtf8("triggered(bool)")), self.outputDirPushButton.setEnabled)
        QtCore.QObject.connect(self.actionProcessFiles, QtCore.SIGNAL(_fromUtf8("triggered(bool)")), self.processFIlesPushButton.setEnabled)
        QtCore.QObject.connect(self.actionProcessFiles, QtCore.SIGNAL(_fromUtf8("triggered(bool)")), self.processProgressBar.setDisabled)
        QtCore.QObject.connect(self.actionFilesProcessed, QtCore.SIGNAL(_fromUtf8("triggered(bool)")), self.inputDirLineEdit.setDisabled)
        QtCore.QObject.connect(self.actionFilesProcessed, QtCore.SIGNAL(_fromUtf8("triggered(bool)")), self.changeNameCheckBox.setDisabled)
        QtCore.QObject.connect(self.actionFilesProcessed, QtCore.SIGNAL(_fromUtf8("triggered(bool)")), self.changeNameLabel.setDisabled)
        QtCore.QObject.connect(self.actionFilesProcessed, QtCore.SIGNAL(_fromUtf8("triggered(bool)")), self.changeNameLineEdit.setDisabled)
        QtCore.QObject.connect(self.actionFilesProcessed, QtCore.SIGNAL(_fromUtf8("triggered(bool)")), self.changeSizeCheckBox.setDisabled)
        QtCore.QObject.connect(self.actionFilesProcessed, QtCore.SIGNAL(_fromUtf8("triggered(bool)")), self.inputDirLabel.setDisabled)
        QtCore.QObject.connect(self.actionFilesProcessed, QtCore.SIGNAL(_fromUtf8("triggered(bool)")), self.inputDirPushButton.setDisabled)
        QtCore.QObject.connect(self.actionFilesProcessed, QtCore.SIGNAL(_fromUtf8("triggered(bool)")), self.insertLabelCheckBox.setDisabled)
        QtCore.QObject.connect(self.actionFilesProcessed, QtCore.SIGNAL(_fromUtf8("triggered(bool)")), self.labelFileLabel.setDisabled)
        QtCore.QObject.connect(self.actionFilesProcessed, QtCore.SIGNAL(_fromUtf8("triggered(bool)")), self.labelFileLineEdit.setDisabled)
        QtCore.QObject.connect(self.actionFilesProcessed, QtCore.SIGNAL(_fromUtf8("triggered(bool)")), self.labelFilePushButton.setDisabled)
        QtCore.QObject.connect(self.actionFilesProcessed, QtCore.SIGNAL(_fromUtf8("triggered(bool)")), self.labelSizeLabel.setDisabled)
        QtCore.QObject.connect(self.actionFilesProcessed, QtCore.SIGNAL(_fromUtf8("triggered(bool)")), self.labelSizeSpinBox.setDisabled)
        QtCore.QObject.connect(self.actionFilesProcessed, QtCore.SIGNAL(_fromUtf8("triggered(bool)")), self.maxHeightLabel.setDisabled)
        QtCore.QObject.connect(self.actionFilesProcessed, QtCore.SIGNAL(_fromUtf8("triggered(bool)")), self.maxHeightSpinBox.setDisabled)
        QtCore.QObject.connect(self.actionFilesProcessed, QtCore.SIGNAL(_fromUtf8("triggered(bool)")), self.maxWidthLabel.setDisabled)
        QtCore.QObject.connect(self.actionFilesProcessed, QtCore.SIGNAL(_fromUtf8("triggered(bool)")), self.maxWidthSpinBox.setDisabled)
        QtCore.QObject.connect(self.actionFilesProcessed, QtCore.SIGNAL(_fromUtf8("triggered(bool)")), self.outputDirLabel.setDisabled)
        QtCore.QObject.connect(self.actionFilesProcessed, QtCore.SIGNAL(_fromUtf8("triggered(bool)")), self.outputDirLineEdit.setDisabled)
        QtCore.QObject.connect(self.actionFilesProcessed, QtCore.SIGNAL(_fromUtf8("triggered(bool)")), self.outputDirPushButton.setDisabled)
        QtCore.QObject.connect(self.actionFilesProcessed, QtCore.SIGNAL(_fromUtf8("triggered(bool)")), self.processFIlesPushButton.setDisabled)
        QtCore.QObject.connect(self.actionFilesProcessed, QtCore.SIGNAL(_fromUtf8("triggered(bool)")), self.processProgressBar.setEnabled)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtGui.QApplication.translate("MainWindow", "Złośnica", None, QtGui.QApplication.UnicodeUTF8))
        self.labelSizeSpinBox.setSuffix(QtGui.QApplication.translate("MainWindow", "%", None, QtGui.QApplication.UnicodeUTF8))
        self.labelFileLabel.setText(QtGui.QApplication.translate("MainWindow", "Plik podpisu:", None, QtGui.QApplication.UnicodeUTF8))
        self.inputDirLabel.setText(QtGui.QApplication.translate("MainWindow", "Folder wejściowy:", None, QtGui.QApplication.UnicodeUTF8))
        self.outputDirLabel.setText(QtGui.QApplication.translate("MainWindow", "Folder wyjściowy:", None, QtGui.QApplication.UnicodeUTF8))
        self.labelFilePushButton.setText(QtGui.QApplication.translate("MainWindow", "Przeglądaj", None, QtGui.QApplication.UnicodeUTF8))
        self.labelFileLineEdit.setText(QtGui.QApplication.translate("MainWindow", "C:/podpis_weronika.png", None, QtGui.QApplication.UnicodeUTF8))
        self.labelSizeLabel.setText(QtGui.QApplication.translate("MainWindow", "Wielkość podpisu", None, QtGui.QApplication.UnicodeUTF8))
        self.maxWidthLabel.setText(QtGui.QApplication.translate("MainWindow", "Maksymalna szerokość:", None, QtGui.QApplication.UnicodeUTF8))
        self.maxHeightLabel.setText(QtGui.QApplication.translate("MainWindow", "Maksymalna wysokość:", None, QtGui.QApplication.UnicodeUTF8))
        self.inputDirPushButton.setText(QtGui.QApplication.translate("MainWindow", "Przeglądaj", None, QtGui.QApplication.UnicodeUTF8))
        self.inputDirLineEdit.setText(QtGui.QApplication.translate("MainWindow", "C:\\Users\\CurrenUser\\Obrazy", None, QtGui.QApplication.UnicodeUTF8))
        self.maxHeightSpinBox.setSuffix(QtGui.QApplication.translate("MainWindow", "px", None, QtGui.QApplication.UnicodeUTF8))
        self.outputDirLineEdit.setText(QtGui.QApplication.translate("MainWindow", "C:/asdfasdfasdf", None, QtGui.QApplication.UnicodeUTF8))
        self.changeNameCheckBox.setText(QtGui.QApplication.translate("MainWindow", "Zmień nazwę", None, QtGui.QApplication.UnicodeUTF8))
        self.outputDirPushButton.setText(QtGui.QApplication.translate("MainWindow", "Przeglądaj", None, QtGui.QApplication.UnicodeUTF8))
        self.changeNameLineEdit.setText(QtGui.QApplication.translate("MainWindow", "wu_2013-09-09_nazwa_imprezy_%d.jpg", None, QtGui.QApplication.UnicodeUTF8))
        self.changeNameLabel.setText(QtGui.QApplication.translate("MainWindow", "Nazwa pliku:", None, QtGui.QApplication.UnicodeUTF8))
        self.insertLabelCheckBox.setText(QtGui.QApplication.translate("MainWindow", "Wstaw podpis", None, QtGui.QApplication.UnicodeUTF8))
        self.processFIlesPushButton.setText(QtGui.QApplication.translate("MainWindow", "Konwertuj Pliki", None, QtGui.QApplication.UnicodeUTF8))
        self.processProgressBar.setFormat(QtGui.QApplication.translate("MainWindow", "%p%", None, QtGui.QApplication.UnicodeUTF8))
        self.maxWidthSpinBox.setSuffix(QtGui.QApplication.translate("MainWindow", "px", None, QtGui.QApplication.UnicodeUTF8))
        self.changeSizeCheckBox.setText(QtGui.QApplication.translate("MainWindow", "Zmień rozmiar", None, QtGui.QApplication.UnicodeUTF8))
        self.actionProcessFiles.setText(QtGui.QApplication.translate("MainWindow", "Konwertuj pliki", None, QtGui.QApplication.UnicodeUTF8))
        self.actionPreProcessFiles.setText(QtGui.QApplication.translate("MainWindow", "preProcessFiles", None, QtGui.QApplication.UnicodeUTF8))
        self.actionFilesProcessed.setText(QtGui.QApplication.translate("MainWindow", "Pliki przekonwertowane", None, QtGui.QApplication.UnicodeUTF8))

