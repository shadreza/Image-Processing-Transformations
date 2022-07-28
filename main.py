import numpy as np
import cv2
from PIL import Image
from PIL import ImageDraw


def makeImgTo8BitGreyScale(imgDirectory, outputLabel):

    colorImage = Image.open(imgDirectory)
    greyScaleImage = colorImage.convert("L")
    imageWithColorPalette = greyScaleImage.convert("P", palette=Image.ADAPTIVE, colors=8)
    greyScale8BitImageOut = imageWithColorPalette.save("Outputs-Images-In-8bit-GreyScale/" + outputLabel)


def useErosion(imgDirectory, outputLabel):

    img = cv2.imread(imgDirectory)
    squareKernelSide = 7
    kernel = np.ones((squareKernelSide, squareKernelSide), np.uint8)
    resultErosionImg = cv2.erode(img, kernel, cv2.BORDER_REFLECT)
    cv2.imwrite(outputLabel, resultErosionImg)
    cv2.imshow(outputLabel, resultErosionImg)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


def useKMeansClustering(imgDirectory, outputLabel):

    img = cv2.imread(imgDirectory)
    reshapedImg = img.reshape((-1, 3))
    reshapedImg = np.float32(reshapedImg)
    criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 10, 1.0)
    K = 8
    ret, label, center = cv2.kmeans(reshapedImg, K, None, criteria, 10, cv2.KMEANS_RANDOM_CENTERS)
    center = np.uint8(center)
    res = center[label.flatten()]
    resultKMeansClusteringImg = res.reshape(img.shape)
    cv2.imwrite(outputLabel, resultKMeansClusteringImg)
    cv2.imshow(outputLabel, resultKMeansClusteringImg)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


def use7x7GaussianHighPassFilter(imgDirectory, outputLabel):

    img = cv2.imread(imgDirectory)
    squareKernelSide = 7
    resultGaussianHighPassImg = cv2.GaussianBlur(img, (squareKernelSide, squareKernelSide), 0)
    cv2.imwrite(outputLabel, resultGaussianHighPassImg)
    cv2.imshow(outputLabel, resultGaussianHighPassImg)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


def use7x7LowPassFilter(imgDirectory, outputLabel):

    img = cv2.imread(imgDirectory)
    squareKernelSide = 7
    kernel = np.ones((squareKernelSide, squareKernelSide), np.float32) / (squareKernelSide * squareKernelSide)
    resultLowPassFilterImg = cv2.filter2D(img, -1, kernel)
    cv2.imwrite(outputLabel, resultLowPassFilterImg)
    cv2.imshow(outputLabel, resultLowPassFilterImg)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


def readImgAndShowImg(imgDirectory, outputLabel):

    img = cv2.imread(imgDirectory, 0)
    d = img.shape
    print("The Input Parrot Image is of size " + str(d))
    cv2.imshow(outputLabel, img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


inputImgName = "Input-Parrot-Greyscale-8bit-Image.png"
outputImgNames = ['Input.png', 'Output-LowPass-Filter-using-7x7-Kernel-Img.png',
                  'Output-Gaussian-HighPass-Filter-using-7x7-Kernel-Img.png', 'Output-K-Means-Clustering-Img.png',
                  'Output-Erosion-Img.png']
outputNames = ['Input', 'LowPass', 'Gaussian-HighPass', 'K-Means-Clustering', 'Erosion']

readImgAndShowImg(inputImgName, outputImgNames[0])
use7x7LowPassFilter(inputImgName, outputImgNames[1])
use7x7GaussianHighPassFilter(inputImgName, outputImgNames[2])
useKMeansClustering(inputImgName, outputImgNames[3])
useErosion(inputImgName, outputImgNames[4])

counter = -1
for img in outputImgNames:
    counter = counter + 1
    if img == 'Input.png':
        continue
    makeImgTo8BitGreyScale(img, img)
    outImg = Image.open(img)
    drawOnImg = ImageDraw.Draw(outImg)
    drawOnImg.text((10, 10), outputNames[counter], fill=(255, 0, 0))
    outImg.show()
