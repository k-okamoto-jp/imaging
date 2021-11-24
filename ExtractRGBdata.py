import cv2
import pandas as pd
# %matplotlib inline

Xposition = 50
img = cv2.imread('legend.PNG')
print(img.shape)
h, w = img.shape[:2]

imgline = img[:, Xposition, :]
df = pd.DataFrame(imgline)
df.to_clipboard()
cv2.line(img, (Xposition+2, 0), (Xposition+2, h), (0, 0, 0), 2)

cv2.imshow('img', img)
cv2.imshow('imgline', imgline)
cv2.waitKey(0)
cv2.destroyAllWindows()
pass