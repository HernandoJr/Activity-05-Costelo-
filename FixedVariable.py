import os
import cv2 
import numpy as ny

image= len(img.shape)
image_gray = len(gray.shape)
if image > image_gray:
cv.imshow("colored", img)
        cv.waitKey(0)
    else:
        exit()

elif user_input == '2':
    x = int(input("for x axis: "))
    y = int(input("for y axis: "))
    color = int(input("BGR selection: [1. BLUE] [2. GREEN] [3. RED]: "))
    c=color-1
    print(img.item(x, y , c))


elif user_input == '3':
    x = int(input("for x axis: "))
    y = int(input("for y axis: "))
    print(img[x, y])
    for i in range(0, 3, 1):
        color = int(input("BGR selection: [1. BLUE] [2. GREEN] [3. RED]: "))
        pixelValue = int(input("Pixel Value: "))
        c=color-1
        img.itemset((x, y, c), pixelValue)
    print(img[x, y])
    cv.imshow("colored", img)
    cv.waitKey(0)

elif user_input == '4':
    x=400
    y=200
    print(img.shape)
    print(f"""
                the total pixel in x-axis: {img.shape[0]}
                the total pixel in y-axis: {img.shape[1]}
                the compared value in x-axis: {x}
                the compared value in y-axis: {y}
            """)

    if x <= img.shape[0] and y <= img.shape[1] :
        print("Within boundaries")
    else :
        print("Out of boundaries")

elif user_input == '5':
    x=150
    y=150
    fixedValue=x * y
    totalPixel=img.shape[0] * img.shape[1]

    print(f"""
              the total fixed variable: {fixedValue}
              the total image pixels: {totalPixel}
            """)

    if fixedValue > totalPixel :
        print("higher")
    elif fixedValue < totalPixel :
        print("lower")
    else :
        print("equal")

elif user_input == '6':
    print(f"the image data type is: {img.dtype}")

else:
    exit()

