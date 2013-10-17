#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = u"Rafal Selewonko <rselewonko@murator.com.pl>"

from PIL import Image
from PIL.ExifTags import TAGS
import math
from ui import Ui_MainWindow
from PyQt4 import QtCore, QtGui
import os
import re
import sys
import ConfigParser


DEFAULT_FILENAME = "weronika_urbanska_1970-01-01_nazwa_okazji_%d.jpg"
CONFIG_FILENAME = os.path.expanduser('~/.zlosnica')


def get_exif(fn):
    ret = {}
    i = Image.open(fn)
    info = i._getexif()
    for tag, value in info.items():
        decoded = TAGS.get(tag, tag)
        ret[decoded] = value
    return ret


def get_exifv2(fn):
    ret = {}
    i = Image.open(fn)
#    info = i._getexif()
    info = i.tag.tags
    for tag, value in info.items():
        decoded = TAGS.get(tag, tag)
        ret[decoded] = value
    return ret


def convert(img, scale=None, width=None, height=None, watermark_img=None, watermark_coverage=.3, watermark_opacity=1.):

    original_width, original_height = img.size

    if scale is not None:
        new_width, new_height = round(original_width * scale), round(original_height * scale)
        img.thumbnail(map(int, (new_width, new_height)), Image.ANTIALIAS)

    if width is not None or height is not None:
        if width is None:
            width = original_width
        if height is None:
            height = original_height

        ratio = 1.0
        ratio_w = float(width) / original_width
        ratio_h = float(height) / original_height
        ratio_max = max(ratio_w, ratio_h)

        if ratio_max < 1.0:
            ratio = ratio_max
        else:
            ratio = min(ratio, ratio_w, ratio_h)

        ratio = min(ratio, ratio_w, ratio_h)

        new_width = original_width * ratio
        new_height = original_height * ratio

        img = img.resize(map(int, (new_width, new_height)), Image.ANTIALIAS).copy()
    else:
        new_width = original_width
        new_height = original_height

    # dodanie watermarka
    if watermark_img:
        watermark_width, watermark_height = watermark_img.size
        new_watermark_width = math.ceil(max(new_width, new_height) * watermark_coverage)
        new_watermark_height = math.ceil(new_watermark_width / float(watermark_width) * watermark_height)
        if new_watermark_width > new_width:
            new_watermark_height = new_width
        watermark_img = watermark_img.resize(map(int, (new_watermark_width, new_watermark_height)), Image.ANTIALIAS).copy()

        coords = tuple(map(int, (new_width - new_watermark_width, new_height - new_watermark_height)))
        img.paste(watermark_img, coords, watermark_img)

    return img


def launch(args):
    infiles = []
    for infile in args.infile:
        #infiles.extend(glob.glob(infile))
        infiles.append(infile)

    outfile = None
    if args.outfile:
        outfile = args.outfile

    total = len(infiles)

    if outfile:
        if len(infiles) == 1:
            outfile = args.outfile
        elif not r"%d" in outfile:
            path, extension = os.path.splitext(outfile)
            outfile = "{path}_%d{extension}".format(path=path, extension=extension)

    watermark_img = None
    if args.watermark:
        try:
            watermark_img = Image.open(args.watermark)
        except IOError, e:
            sys.stderr.write("Error opening file %s: " % args.watermark)
            sys.stderr.write(str(e))
            sys.stderr.write("\n")

    scale = None
    if args.scale:
        scale = args.scale / 100.

    width = None
    if args.max_width:
        width = args.max_width

    height = None
    if args.max_height:
        height = args.max_height

    for j, infile in enumerate(infiles):
        i = j + 1
        if not args.quiet:
            percent = int(round(i / float(total) * 100))
            sys.stdout.write(u"\rprzekonwertowano %d%% (plik %d z %d)" % (percent, i, total))
            sys.stdout.flush()
            if i == total:
                sys.stdout.write("\n")

        try:
            img = Image.open(infile)
        except IOError, e:
            sys.stderr.write("Error opening file %s: " % infile)
            sys.stderr.write(str(e))
            sys.stderr.write("\n")
        else:
            if watermark_img:
                img = convert(img, scale=scale, width=width, height=height, watermark_img=watermark_img, watermark_coverage=args.watermark_coverage / 100.)
            else:
                img = convert(img, scale=scale, width=width, height=height)

            if outfile is None:
                path, extension = os.path.splitext(infile)
                routfile = "{path}_p{extension}".format(path=path, extension=extension)
            elif r"%d" in outfile:
                routfile = outfile.replace(r'%d', r'%s')
                routfile = routfile % str(i).zfill(len(str(total)))
            img.save(routfile)


class ZlosnicaGUI(QtGui.QMainWindow):

    def __init__(self, parent=None):
        super(ZlosnicaGUI, self).__init__(parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.labelFilePushButton.clicked.connect(self.selectLabelFile)
        self.ui.inputDirPushButton.clicked.connect(self.selectInputDir)
        self.ui.outputDirPushButton.clicked.connect(self.selectOutputDir)
        self.ui.actionPreProcessFiles.triggered.connect(self.preProcessFiles)
        self.ui.actionProcessFiles.triggered.connect(self.processFiles)
        self.ui.actionFilesProcessed.triggered.connect(self.showPopup)
        self.home = QtCore.QDir.homePath()

        self.read_config()
        self.apply_config()

    def read_config(self):
        self.config = ConfigParser.RawConfigParser()

        if not os.path.exists(CONFIG_FILENAME):
            self.config.add_section('main')
            self.config.set('main', 'input_directory', self.home)
            self.config.set('main', 'output_directory', self.home)
            self.config.set('main', 'new_filename', DEFAULT_FILENAME)
            self.config.set('main', 'label_filename', self.home)
            self.write_config()

        self.config.read(CONFIG_FILENAME)

    def write_config(self):
        with open(CONFIG_FILENAME, 'wb') as configfile:
            self.config.write(configfile)

    def apply_config(self):
        self.ui.changeNameLineEdit.setText(self.config.get('main', 'new_filename'))
        self.ui.labelFileLineEdit.setText(self.config.get('main', 'label_filename'))
        self.ui.inputDirLineEdit.setText(self.config.get('main', 'input_directory'))
        self.ui.outputDirLineEdit.setText(self.config.get('main', 'output_directory'))

    def update_config(self):
        self.config.set('main', 'input_directory', str(self.ui.inputDirLineEdit.text()))
        self.config.set('main', 'output_directory', str(self.ui.outputDirLineEdit.text()))
        self.config.set('main', 'new_filename', str(self.ui.changeNameLineEdit.text()))
        self.config.set('main', 'label_filename', str(self.ui.labelFileLineEdit.text()))

    def selectLabelFile(self):
        self.ui.labelFileLineEdit.setText(QtGui.QFileDialog.getOpenFileName(
            self,
            u"Wskaż plik podpisu...",
            self.home,
            "Images (*.jpg *.png);;All Files (*)"))

    def selectInputDir(self):
        self.ui.inputDirLineEdit.setText(QtGui.QFileDialog.getExistingDirectory(
            self,
            u"Wskaż folder wejściowy...",
            self.home))

    def selectOutputDir(self):
        self.ui.outputDirLineEdit.setText(QtGui.QFileDialog.getExistingDirectory(
            self,
            u"Wskaż folder wyjściowy...",
            self.home))

    def preProcessFiles(self):
        self.scale = None
        self.max_width = None
        self.max_height = None
        if self.ui.changeSizeCheckBox.checkState():
            self.max_width = self.ui.maxWidthSpinBox.value()
            self.max_height = self.ui.maxHeightSpinBox.value()

        self.new_filename = None
        if self.ui.changeNameCheckBox.checkState():
            self.new_filename = os.path.join(str(self.ui.outputDirLineEdit.text()), str(self.ui.changeNameLineEdit.text()))

        self.label_size = None
        self.label_filename = None
        self.label_img = None
        if self.ui.insertLabelCheckBox.checkState():
            self.label_size = self.ui.labelSizeSpinBox.value() / 100.
            self.label_filename = str(self.ui.labelFileLineEdit.text())
            try:
                self.label_img = Image.open(self.label_filename)
            except IOError, e:
                QtGui.QMessageBox.warning(
                    self,
                    u"Nie można otworzyć pliku",
                    u"Nie udało się otworzyć pliku %s. Sprawdź czy plik istnieje." % self.label_filename)
                return

        inputDir = str(self.ui.inputDirLineEdit.text())
        if not os.path.exists(inputDir):
            QtGui.QMessageBox.warning(
                self,
                u"Folder wejściowy nie istnieje.",
                u"Folder wejściowy %s nie istnieje. Popraw ścieżkę i spróbuj ponownie." % inputDir)
            return

        outputDir = str(self.ui.outputDirLineEdit.text())
        if not os.path.exists(outputDir):
            QtGui.QMessageBox.warning(
                self,
                u"Folder wyjściowy nie istnieje.",
                u"Folder wyjściowy %s nie istnieje. Popraw ścieżkę i spróbuj ponownie." % outputDir)
            return

        self.files = self._getAllFiles(str(self.ui.inputDirLineEdit.text()))
        if self.files:
            self.ui.actionProcessFiles.trigger()
        else:
            QtGui.QMessageBox.warning(
                self,
                u"Nie znaleziono plików",
                u"Nie znaleziono plików graficznych w folderze wejściowym %s. Sprawdź zawartość folderu wejściowego." % inputDir)

    def processFiles(self):
        files = self.files
        for j, filename in enumerate(files):
            i = j + 1

            try:
                img = Image.open(filename)
            except IOError, e:
                sys.stderr.write("Error opening file %s: " % filename)
                sys.stderr.write(str(e))
                sys.stderr.write("\n")
            else:
                img = convert(img, scale=self.scale, width=self.max_width, height=self.max_height, watermark_img=self.label_img, watermark_coverage=self.label_size)

                if self.new_filename is None:
                    #path, extension = os.path.splitext(filename)
                    #routfile = "{path}_zmniejszone{extension}".format(path=path, extension=extension)
                    new_filename = filename
                elif r"%d" in self.new_filename:
                    new_filename = self.new_filename.replace(r'%d', r'%s')
                    new_filename = new_filename % str(i).zfill(len(str(len(files))))
                else:
                    path, extension = os.path.splitext(self.new_filename)
                    new_filename = "{path}_%s{extension}".format(path=path, extension=extension)
                    new_filename = new_filename % str(i).zfill(len(str(len(files))))

                img.save(new_filename)

            progress_message = QtCore.QString(u"przekonwertowano %p% (plik %1 z %2)").arg(str(i)).arg(str(len(files)))
            self.ui.processProgressBar.setFormat(progress_message)
            self.ui.processProgressBar.setValue(int(i / float(len(files)) * 100))

        self.update_config()
        self.write_config()
        self.ui.actionFilesProcessed.trigger()

    def _getAllFiles(self, directory):
        pattern = r'.*[.](jpg|jpeg|png|bmp|raw|tif)$'
        prog = re.compile(pattern)
        files = []
        for dirpath, dirnames, filenames in os.walk(directory):
            for filename in [f for f in filenames if prog.match(f.lower())]:
                files.append(os.path.join(dirpath, filename))
        return files

    def showPopup(self):
        QtGui.QMessageBox.information(
            self,
            u"Konwertowanie zakończone",
            u"Konwertowanie zakończone. Sprawdź zawartość folderu docelowego.")


def launch_gui(args=None):
    app = QtGui.QApplication(sys.argv)
    zlosnica_gui = ZlosnicaGUI()
    zlosnica_gui.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser()
    parser.add_argument('-g', '--gui', action="store_true")
    parser.add_argument('-i', '--infile', type=str, nargs='*')
    parser.add_argument('-o', '--outfile', type=str)
    parser.add_argument('-q', '--quiet', action="store_true")
    parser.add_argument('-s', '--scale', type=int)
    parser.add_argument('-mw', '--max_width', type=int)
    parser.add_argument('-mh', '--max_height', type=int)
    parser.add_argument('-w', '--watermark', type=argparse.FileType('r'))
    parser.add_argument('-wc', '--watermark-coverage', type=int, default=30)
    parser.add_argument('-wo', '--watermark-opacity', type=int, default=100)
    args = parser.parse_args()

    if args.gui:
        launch_gui(args)
    else:
        launch(args)
