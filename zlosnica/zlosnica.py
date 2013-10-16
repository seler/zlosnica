#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = u"Rafal Selewonko <rselewonko@murator.com.pl>"

from PIL import Image
from PIL.ExifTags import TAGS
import math
from ui import Ui_MainWindow
from PyQt4 import QtCore, QtGui


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

    # dodanie watermarka
    if watermark_img:
        watermark_width, watermark_height = watermark_img.size
        new_watermark_width = math.ceil(max(new_width, new_height) * watermark_coverage)
        new_watermark_height = math.ceil(new_watermark_width / float(watermark_width) * watermark_height)
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

    def selectLabelFile(self):
        self.ui.labelFileLineEdit.setText(QtGui.QFileDialog.getOpenFileName(
            self,
            u"Wskaż plik podpisu...",
            QtCore.QDir.homePath(),
            "Images (*.jpg *.png);;All Files (*)"))

    def selectInputDir(self):
        self.ui.inputDirLineEdit.setText(QtGui.QFileDialog.getExistingDirectory(
            self,
            u"Wskaż folder wejściowy...",
            QtCore.QDir.homePath()))

    def selectOutputDir(self):
        self.ui.outputDirLineEdit.setText(QtGui.QFileDialog.getExistingDirectory(
            self,
            u"Wskaż folder wyjściowy...",
            QtCore.QDir.homePath()))

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

        if self.ui.insertLabelCheckBox.checkState():
            self.label_size = self.ui.labelSizeSpinBox.value() / 100.
            self.label_filename = str(self.ui.labelFileLineEdit.text())
            try:
                self.label_img = Image.open(self.label_filename)
            except IOError, e:
                sys.stderr.write("Error opening file %s: " % self.label_filename)
                sys.stderr.write(str(e))
                sys.stderr.write("\n")
                raise

        self.ui.actionProcessFiles.trigger()

    def processFiles(self):
        files = self._getAllFiles(str(self.ui.inputDirLineEdit.text()))
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

            self.ui.processProgressBar.setValue(int(i / float(len(files)) * 100))

    def _getAllFiles(self, directory):
        files = []
        for dirpath, dirnames, filenames in os.walk(directory):
            for filename in [f for f in filenames if f.lower().endswith(".jpg")]:
                files.append(os.path.join(dirpath, filename))
        return files


def launch_gui(args):
    app = QtGui.QApplication(sys.argv)
    zlosnica_gui = ZlosnicaGUI()
    zlosnica_gui.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    import argparse
    import os
    import sys
    #import glob

    parser = argparse.ArgumentParser()
    parser.add_argument('-g', '--gui', action="store_true")
    parser.add_argument('infile', type=str, nargs='*')
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
