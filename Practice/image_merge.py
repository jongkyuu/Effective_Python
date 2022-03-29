# %%

import random
import os

rootDirectory = r"C:\GoogleDrive\Study\Python\Effective_Python\Practice"
directoryPathList = []
for dir in os.listdir(rootDirectory):
    if os.path.isdir(os.path.join(rootDirectory, dir)):
        directoryPathList.append(os.path.join(rootDirectory, dir))
# %%
directoryPathList


# %%
# 폴더 경로 주어지면 폴더 안 이미지 찾아서
# 이미지 이름별로 묶고
#

# %%
# 경로 내의 이미지 추출하는 함수

def findImageFile(path):
    images = []
    files = os.listdir(path)
    for file in files:
        print(file)
        ext = os.path.splitext(file)[1]
        print("os.path.splitext(file)[1] : ", os.path.splitext(file)[1])
        if os.path.splitext(file)[1].lower() == ".jpg":
            images.append(file)

    return images


# %%
images = findImageFile(directoryPathList[0])

# %%
images
# %%
imagesGroup = {}

for image in images[:]:
    imageName = os.path.splitext(image)[0]
    imageExt = os.path.splitext(image)[1]

    print("imageName : ", imageName)
    print("imageExt : ", imageExt)

    commonImageName = imageName.split("_")[0]
    print("commonImageName : ", commonImageName)
    group = imagesGroup.get(commonImageName, [])
    group.append(image)
    imagesGroup[commonImageName] = group

# %%
imagesGroup
# %%
testList = []
for key in imagesGroup.keys():
    if(len(imagesGroup[key]) == 3):
        testList.extend(imagesGroup[key])


# %%
testList

# %%

random.shuffle(testList)
# %%
testList


# %%
a1 = testList[0]
print(a1)
a2 = os.path.splitext(a1)[0][-1]

print(a2)

# %%
sortedtestList = sorted(
    testList, key=lambda test: os.path.splitext(test)[0][-1])
# %%
testList
# %%
sortedtestList
# %%
