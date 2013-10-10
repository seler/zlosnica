from PIL import Image

class ImageNotPrepared(Exception):
    pass


class Skeletonizator(object):
    def __init__(self, image):
        if image.mode != '1':
            image = image.convert('1')

        self.image = image
        self.im = image.load()
        self.width, self.height = image.size

        self.bitmap = [[0 for j in range(self.height)] for x in range(self.width)]
        self.s_array = [[0 for j in range(self.height)] for x in range(self.width)]

        for i in range(self.width):
            for j in range(self.height):
                pixel = int(not bool(self.image.getpixel((i, j))))
                self.bitmap[i][j] = pixel


    def skeletonize(self):
        deleted = 1
        while(deleted):
            self.step2()
            self.step3()
            deleted = self.step4(2)
            deleted += self.step4(3)
        self.to_image()


    def count_s_values(self):
        for i in range(self.width):
            for j in range(self.height):
                self.s_array[x][y] = self.set_s_value(i, j)

    def get_s_value(self, x, y):
        s_array = [[128, 1, 2], [64, 0, 4], [32, 16, 8]]
        if self.bitmap[x][y]:
            sum = 0
            for i in (-1, 0, 1):
                for j in (-1, 0, 1):
                    if (i or j) and self.width > x + i >= 0 and self.height > y + j >= 0:
                            value = self.bitmap[x + i][y + j]
                            if value:
                                sum += s_array[j + 1][i + 1]
            return sum

    def step2(self):
        for i in range(self.width):
            for j in range(self.height):
                if self.bitmap[i][j]:
                    try:
                        top = self.bitmap[i][j - 1]
                    except IndexError:
                        top = 0
                    try:
                        right = self.bitmap[i + 1][j]
                    except IndexError:
                        right = 0
                    try:
                        bottom = self.bitmap[i][j + 1]
                    except IndexError:
                        bottom = 0
                    try:
                        left = self.bitmap[i - 1][j]
                    except IndexError:
                        left = 0
                    try:
                        topright = self.bitmap[i + 1][j - 1]
                    except IndexError:
                        topright = 0
                    try:
                        rightbottom = self.bitmap[i + 1][j + 1]
                    except IndexError:
                        rightbottom = 0
                    try:
                        bottomleft = self.bitmap[i - 1][j + 1]
                    except IndexError:
                        bottomleft = 0
                    try:
                        lefttop = self.bitmap[i - 1][j - 1]
                    except IndexError:
                        lefttop = 0

                    if not top or not right or not bottom or not left:
                        self.bitmap[i][j] = 2
                    elif not (topright and rightbottom and bottomleft and lefttop):
                        self.bitmap[i][j] = 3

    def step4(self, n):
        deletion_array = [3, 5, 7, 12, 13, 14, 15, 20,
                        21, 22, 23, 28, 29, 30, 31, 48,
                        52, 53, 54, 55, 56, 60, 61, 62,
                        63, 65, 67, 69, 71, 77, 79, 80,
                        81, 83, 84, 85, 86, 87, 88, 89,
                        91, 92, 93, 94, 95, 97, 99, 101,
                        103, 109, 111, 112, 113, 115, 116, 117,
                        118, 119, 120, 121, 123, 124, 125, 126,
                        127, 131, 133, 135, 141, 143, 149, 151,
                        157, 159, 181, 183, 189, 191, 192, 193,
                        195, 197, 199, 205, 207, 208, 209, 211,
                        212, 213, 214, 215, 216, 217, 219, 220,
                        221, 222, 223, 224, 225, 227, 229, 231,
                        237, 239, 240, 241, 243, 244, 245, 246,
                        247, 248, 249, 251, 252, 253, 254, 255]

        deleted = 0

        for i in range(self.width):
            for j in range(self.height):
                if self.get_s_value(i, j) in deletion_array and self.bitmap[i][j] == n:
                    deleted += 1
                    self.bitmap[i][j] = 0
                elif self.bitmap[i][j]:
                    self.bitmap[i][j] = 1

        return deleted

    def step3(self):
        """ usuwanie czworek """
        # lista czworek z dokumentacji
        fours = [3 , 6 , 12 , 24 , 48 , 96 , 192 , 129,
                7 , 14 , 28 , 56 , 112 , 224 , 193 , 131,
                15 , 30 , 60 , 120 , 240 , 225 , 195 , 135]
        # w.w. lista czworek po odjeciu deletion_array
        fours = [3, 12, 48, 192, 7, 14, 28, 56, 112, 224,
                193, 131, 15, 30, 60, 120, 240, 225, 195, 135]
        for i in range(self.width):
            for j in range(self.height):
                if self.bitmap[i][j] == 2 and self.get_s_value(i, j) in fours:
                    self.bitmap[i][j] = 0

    def to_image(self):
        im = Image.new('RGB', (self.width, self.height), (255, 255, 255))
        for i in range(self.width):
            for j in range(self.height):
                if self.bitmap[i][j]:
                    im.putpixel((i, j), (0, 0, 0))
        self.skeletonized = im



def skeletonize(img):
    s = Skeletonizator(img)
    s.skeletonize()
    return s.skeletonized


if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser()
    parser.add_argument('infile', type=str, nargs=1)
    parser.add_argument('outfile', type=str, nargs=1)
    args = parser.parse_args()

    img = Image.open(args.infile[0])
    skeletonized = skeletonize(img)
    skeletonized.save(args.outfile[0])
