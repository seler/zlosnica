#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = u"Rafal Selewonko <rselewonko@murator.com.pl>"


import math
from PIL import Image


def convert(img, scale=1., watermark_img=None, watermark_coverage=.3, watermark_opacity=1.):

    width, height = img.size
    new_width, new_height = round(width * scale), round(height * scale)
    img.thumbnail(map(int, (new_width, new_height)), Image.ANTIALIAS)

    watermark_width, watermark_height = watermark_img.size
    new_watermark_width = math.ceil(new_width * watermark_coverage)
    new_watermark_height = math.ceil(new_watermark_width / float(watermark_width) * watermark_height)
    watermark_img.thumbnail(map(int, (new_watermark_width, new_watermark_height)), Image.ANTIALIAS)

    coords = tuple(map(int, (new_width - new_watermark_width, new_height - new_watermark_height)))
    img.paste(watermark_img, coords, watermark_img)

    return img


if __name__ == "__main__":
    import argparse
    import os
    import sys
    from glob import glob

    parser = argparse.ArgumentParser()
    parser.add_argument('infile', type=str, nargs='+')
    parser.add_argument('-o', '--outfile', type=str)
    parser.add_argument('-s', '--scale', type=int, default=100)
    parser.add_argument('-w', '--watermark', type=argparse.FileType('r'))
    parser.add_argument('-wc', '--watermark-coverage', type=int, default=30)
    parser.add_argument('-wo', '--watermark-opacity', type=int, default=100)
    args = parser.parse_args()

    infiles = []
    for infile in args.infile:
        #infiles.extend(glob(infile))
        infiles.append(infile)

    outfile = None
    if args.outfile:
        outfile = args.outfile

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

    for i, infile in enumerate(infiles):
        try:
            img = Image.open(infile)
        except IOError, e:
            sys.stderr.write("Error opening file %s: " % infile)
            sys.stderr.write(str(e))
            sys.stderr.write("\n")
        else:
            if watermark_img:
                img = convert(img, scale=args.scale / 100., watermark_img=watermark_img, watermark_coverage=args.watermark_coverage / 100.)
            else:
                img = convert(img, scale=args.scale / 100.)

            if outfile is None:
                path, extension = os.path.splitext(infile)
                routfile = "{path}_small{extension}".format(path=path, extension=extension)
            elif r"%d" in outfile:
                routfile = outfile % i
            img.save(routfile)
