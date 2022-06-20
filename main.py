import cv2 as cv
import numpy as np



img=cv.imread("costelo.jpg")
gray=cv.imread("ILOVEJOY.jpg", 0)

print("""

    [1] Accept or load colored image. Grayscale should be rejected.
    [2] Based on user input output a pixel value.
    [3] Based on user input, modify pixel value.
    [4] Set image dimensions and define if the image is Within boundaries or not.
    [5] Set image total pixel count then define if the image pixel is Higher or lower than the set pixel.
    [6] Show data type of the image.
    [7] EXIT 
""")
print("---------------------------------------------------------------------")
user_input = input("input number: ")

if user_input == '1' :
    imgs = len(img.shape)
    grays = len(gray.shape)
    if imgs > grays:
        cv.imshow("colored", img)
        cv.waitKey(0)
    else:
        exit()

    
elif user_input == '2':

    x = int(input("x-axis: "))
    y = int(input("y-axis: "))
    bgr = int(input("select BGR : |1. Blue| |2. Green| |3. Red|: "))
    c=bgr-1
    print(img.item(x, y , c))


elif user_input == '3':

    x = int(input("x-axis: "))
    y = int(input("y-axis: "))
    print(img[x, y])

    for index in range(0, 3, 1):

        bgr = int(input("select BGR : |1. Blue| |2. Green| |3. Red|: "))
        pixel = int(input("Pixel Value: "))
        c=bgr-1
        img.itemset((x, y, c), pixel)
        break
    print(img[x, y])
    cv.imshow("COLORED IMAGE", img)
    cv.waitKey(0)
      

elif user_input == '4':

    x=300
    y=200
    print(img.shape)

    if x <= img.shape[0] and y <= img.shape[1] :
       
        print(f"""
                X - Axis: {img.shape[0]}
                Y - Axis: {img.shape[1]}
                X - axis comapared value: {x}
                Y - axis comapared value: {y}
            [---The current load image is "WITHIN BOUNDARIES"---]
            """)
    
        
    else :

        print(f"""
                X - Axis: {img.shape[0]}
                Y - Axis: {img.shape[1]}
                X - axis comapared value: {x}
                Y - axis comapared value: {y}
            [---The current load image is "WITHIN BOUNDARIES"---]
            """)

elif user_input == '5':

    x=180
    y=180
    fixed=x * y
    pixel=img.shape[0] * img.shape[1]

   
    if fixed> pixel :

        print(f"FIXED VARIABLE IMAGE PIXELS: {fixed}")
        print(f"TOTAL IMAGE PIXELS: {pixel}")   
        print("Higher")

    elif fixed < pixel :

        print(f"FIXED VARIABLE IMAGE PIXELS: {fixed}")
        print(f"TOTAL IMAGE PIXELS: {pixel}")   
        print("Lower")

    else :

        print(f"FIXED VARIABLE IMAGE PIXELS: {fixed}")
        print(f"TOTAL IMAGE PIXELS: {pixel}")   
        print("Equal")

elif user_input == '6':

    print(f"IMAGE DATA TYPE: {img.dtype}")

else:

    exit()

