import cv2 as cv
from easyocr import Reader

class Recognition:
        
    def __init__(self, path):
        # Read an Image Using [imread]
        self.car = cv.imread(path)
        # Resize The Selected Image Using [resize]
        self.car = cv.resize(self.car, (800, 600))
        # Convert The Selected Image to Gray Scale Image Using [cvtColor]
        self.gray = cv.cvtColor(self.car, cv.COLOR_BGR2GRAY)
        # Apply Blur Fliter Using [GaussianBlur] With (0) Border
        self.blur = cv.GaussianBlur(self.gray, (5, 5), 0)
        # Detect Edges Using [Canny] With Two Min & Max Threshold
        self.edges = cv.Canny(self.blur, 10, 200)
        # 
        self.cont, _ = cv.findContours(self.edges, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)
        #
        self.cont = sorted(self.cont, key=cv.contourArea, reverse=True)

    def processing(self):
        for c in self.cont:
            self.arc = cv.arcLength(c, True)
            self.approx = cv.approxPolyDP(c, 0.02 * self.arc, True)
            if len(self.approx) == 4:
                self.plate_cnt = self.approx
                break

        (x, y, w, h) = cv.boundingRect(self.plate_cnt)
        self.plate = self.gray[y:y + h, x:x + w]

        self.reader = Reader(['en'], gpu=False, verbose=False)
        self.detection = self.reader.readtext(self.plate)
        print(self.detection)

        if len(self.detection) == 0:
            self.text = 'impossible to read the text from license plate.'
            cv.putText(self.car, self.text, (20, 40), cv.FONT_HERSHEY_SIMPLEX, 0.75, (0, 0, 255), 2)
            # cv.imshow('car', self.car)
            return [self.car, self.text]
        else:
            cv.drawContours(self.car, [self.plate_cnt], -1, (0, 255, 0), 3)
            self.text = f'{self.detection[0][1]} {self.detection[0][2] * 100: .2f}%'
            cv.putText(self.car, self.text, (x, y-20), cv.FONT_HERSHEY_SIMPLEX, 0.75,(0, 255, 0), 2)
            # cv.imshow('car', self.car)
            return [self.car, self.detection[0][1]]
