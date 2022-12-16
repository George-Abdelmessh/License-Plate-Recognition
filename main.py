import cv2 as cv
from easyocr import Reader

# Read an Image Using [imread]
car = cv.imread('./cars/car13.jpg')
# Resize The Selected Image Using [resize]
car = cv.resize(car, (800, 600))
# Convert The Selected Image to Gray Scale Image Using [cvtColor]
gray = cv.cvtColor(car, cv.COLOR_BGR2GRAY)
# Apply Blur Fliter Using [GaussianBlur] With (0) Border
blur = cv.GaussianBlur(gray, (5, 5), 0)
# Detect Edges Using [Canny] With Two Min & Max Threshold
edges = cv.Canny(blur, 10, 200)
# 
cont, _ = cv.findContours(edges, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)
#
cont = sorted(cont, key=cv.contourArea, reverse=True)

for c in cont:
    arc = cv.arcLength(c, True)
    approx = cv.approxPolyDP(c, 0.02 * arc, True)
    if len(approx) == 4:
        plate_cnt = approx
        break

(x, y, w, h) = cv.boundingRect(plate_cnt)
plate = gray[y:y + h, x:x + w]

reader = Reader(['en'], gpu=False, verbose=False)
detection = reader.readtext(plate)
print(detection)

if len(detection) == 0:
    text = 'impossible to read the text from license plate.'
    cv.putText(car, text, (20, 40), cv.FONT_HERSHEY_SIMPLEX, 0.75, (0, 0, 255), 2)
    cv.imshow('car', car)
    cv.waitKey(0)
else:
    cv.drawContours(car, [plate_cnt], -1, (0, 255, 0), 3)
    text = f'{detection[0][1]} {detection[0][2] * 100: .2f}%'
    cv.putText(car, text, (x, y-20), cv.FONT_HERSHEY_SIMPLEX, 0.75,(0, 255, 0), 2)
    cv.imshow('car', car)
    cv.waitKey(0)
