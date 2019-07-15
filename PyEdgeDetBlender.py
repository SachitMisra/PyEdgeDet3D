import cv2
import numpy as np
imgloc = r"" #Enter File Location
img = cv2.imread(imgloc, cv2.IMREAD_GRAYSCALE)



rsz_img = cv2.resize(img, None, fx=0.5, fy=0.5)


ret,thresh1 = cv2.threshold(rsz_img,254,255,cv2.THRESH_BINARY)

laplacian = cv2.Laplacian(img, cv2.CV_64F, ksize=5)
canny = cv2.Canny(thresh1, 100, 200)



ans = []
for y in range(0, canny.shape[0]):
    for x in range(0, canny.shape[1]):
        if canny[y, x] != 0:
            ans = ans + [(x, y, 0)]

for i in range(len(ans)):
    print(ans[i] , ",")

# For Edges[]     
#edge = 0
#for j in range(len(ans)):
#    print("(" , edge ,",", edge + 1,")", ",")
#    edge = j+1




cv2.imshow("Canny", canny)

cv2.waitKey(0)
cv2.destroyAllWindows()
