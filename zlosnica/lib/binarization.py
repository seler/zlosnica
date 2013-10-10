from PIL import Image


def binarize(img, threshold=None):

    im = img.load()

    width, height = img.size

    # jezeli nie ma ustawionego threshold ustawiam go na polowe
    if threshold is None:
        threshold = 255. / 2.

    if img.mode in ('L', '1'):
        def test(x):
            return x > threshold
        max_val = 255
        min_val = 0
        c = 1
    else:
        if img.mode == "RGB":
            c = 3.
        elif img.mode in ("CMYK", "RGBA"):
            c = 4.

        def test(x):
            return sum(x) / c > threshold

        max_val = (255, 255, 255)
        min_val = (0, 0, 0)

    for i in range(width):
        for j in range(height):
            im[i, j]
            if test(im[i, j]):
                im[i, j] = max_val
            else:
                im[i, j] = min_val

    return img


if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser()
    parser.add_argument('infile', type=str, nargs=1)
    parser.add_argument('outfile', type=str, nargs=1)
    parser.add_argument('-t', '--threshold', type=int)
    args = parser.parse_args()

    img = Image.open(args.infile[0])
    img = binarize(img, threshold=args.threshold)
    img.save(args.outfile[0])
