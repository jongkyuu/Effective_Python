# %%
import os
import cv2

def findImageFile(path):
    images = []
    files = os.listdir(path)
    for file in files:
        ext = os.path.splitext(file)[1]
        if os.path.splitext(file)[1].lower() == ".jpg":   # 다른 확장자 있을 경우 추가
            images.append(file)
    return images

def mergeImage(directoryPath, leftImageName, rightImageName, centerImageName):
    leftImage = cv2.imread(os.path.join(directoryPath, leftImageName))
    rightImage = cv2.imread(os.path.join(directoryPath, rightImageName))
    centerImage = cv2.imread(os.path.join(directoryPath, centerImageName))
    
    # 1번 이미지 r, 2번 이미지 g, 3번 이미지 r channel 분리
    _, _, leftImage_r = cv2.split(leftImage)
    _, rightImage_g, _ = cv2.split(rightImage)
    _, _, centerImage_r = cv2.split(centerImage)

    mergeImage = cv2.merge((leftImage_r, rightImage_g, centerImage_r))
    return mergeImage


def createFolder(directory):
    try:
        if not os.path.exists(directory):
            os.makedirs(directory, exist_ok=True)
    except OSError:
        print ('Error: Creating directory. ' +  directory)


def SaveResult(className, key, image):
    parentDirectory = os.path.dirname(rootDirectory)
    resultDirectory = os.path.join(parentDirectory, "MergeResult")
    classDirectory = os.path.join(resultDirectory, className)
    createFolder(classDirectory)
    imageFile = key + ".jpg"
    cv2.imwrite(os.path.join(classDirectory, imageFile), image)


rootDirectory = r"D:\JK\Study\MLS\Effective_Python\Practice\Images"  # 클래스 폴더들의 상위 폴더 경로
directoryPathList = []
for dir in os.listdir(rootDirectory):
    if os.path.isdir(os.path.join(rootDirectory, dir)):
        directoryPathList.append(os.path.join(rootDirectory, dir))

for directoryPath in directoryPathList:
    images = findImageFile(directoryPath)
    className = directoryPath.split(os.sep)[-1]

    print("className : ", className)

    imagesGroup = {}

    for image in images[:]:
        imageName = os.path.splitext(image)[0]
        imageExt = os.path.splitext(image)[1]
        commonImageName = imageName.split("_")[0]
        group = imagesGroup.get(commonImageName, [])
        group.append(image)
        imagesGroup[commonImageName] = group

    print("imagesGroup : ", imagesGroup)

    for key in imagesGroup.keys():
        if(len(imagesGroup[key]) == 3):  # 다른 Case 있으면 예외처리 필요
            images = imagesGroup[key]
            images = sorted(images, key=lambda file : os.path.splitext(file)[0][-1])
            mergeResult = mergeImage(directoryPath, *images)

            SaveResult(className, key, mergeResult)
    print("="*20)


# %%
