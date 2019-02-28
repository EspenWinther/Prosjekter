from PIL import Image
import random
import math
import cv2
import numpy as np

image = cv2.imread(r"C:\Users\Espen Eilertsen\Pictures\TrondPort.png",cv2.IMREAD_GRAYSCALE)

sift = cv2.xfeatures2d.SIFT_create()
surf = cv2.xfeatures2d.SURF_create()

orb = cv2.ORB_create(nfeatures=1500)

keypoints, descriptor = orb.detectAndCompute(image,None)
image = cv2.drawKeypoints(image, keypoints, None)
cv2.imshow('Image', image)

lister = []

for i in range(len(keypoints)):
    print(keypoints[i].pt)
    lister.append(keypoints[i].pt)

with open(r"C:\Users\Espen Eilertsen\testext.txt", 'w+') as output:
    for i in range(len(keypoints)):
        output.write(str(lister[i][0]))
        output.write(str("  "))
        output.write(str(lister[i][1]))
        output.write(str("\n"))

cv2.waitKey(0)
cv2.destroyAllWindows()


def generate_voronoi_diagram(width, height, num_cells):
    image = Image.open(r"C:\Users\Espen Eilertsen\Pictures\TrondPort.png")
    #myimage.show()
    #image = Image.new("RGB", (width, height))
    putpixel = image.putpixel
    imgx, imgy = image.size
    nx = []
    ny = []
    nr = []
    ng = []
    nb = []
    for i in range(num_cells):
        nx.append(random.randrange(imgx))
        ny.append(random.randrange(imgy))
        nr.append(random.randrange(256))
        ng.append(random.randrange(256))
        nb.append(random.randrange(256))
    for y in range(imgy):
        for x in range(imgx):
            dmin = math.hypot(imgx - 1, imgy - 1)
            j = -1
            for i in range(num_cells):
                d = math.hypot(nx[i] - x, ny[i] - y)
                if d < dmin:
                    dmin = d
                    j = i
            putpixel((x, y), (nr[j], ng[j], nb[j]))
    image.save("VoronoiDiagram.png", "PNG")
    image.show()


generate_voronoi_diagram(sift, surf, len(keypoints))