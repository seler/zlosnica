#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = u"Rafal Selewonko <rselewonko@murator.com.pl>"


import math
from PIL import Image


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
        new_watermark_width = math.ceil(new_width * watermark_coverage)
        new_watermark_height = math.ceil(new_watermark_width / float(watermark_width) * watermark_height)
        watermark_img.thumbnail(map(int, (new_watermark_width, new_watermark_height)), Image.ANTIALIAS)

        coords = tuple(map(int, (new_width - new_watermark_width, new_height - new_watermark_height)))
        img.paste(watermark_img, coords, watermark_img)

    return img
