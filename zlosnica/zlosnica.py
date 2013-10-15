#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = u"Rafal Selewonko <rselewonko@murator.com.pl>"

from PIL import Image
from convert import convert


if __name__ == "__main__":
    import argparse
    import os
    import sys
    #import glob

    parser = argparse.ArgumentParser()
    parser.add_argument('infile', type=str, nargs='+')
    parser.add_argument('-o', '--outfile', type=str)
    parser.add_argument('-q', '--quiet', action="store_true")
    parser.add_argument('-s', '--scale', type=int)
    parser.add_argument('-mw', '--max_width', type=int)
    parser.add_argument('-mh', '--max_height', type=int)
    parser.add_argument('-w', '--watermark', type=argparse.FileType('r'))
    parser.add_argument('-wc', '--watermark-coverage', type=int, default=30)
    parser.add_argument('-wo', '--watermark-opacity', type=int, default=100)
    args = parser.parse_args()

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
