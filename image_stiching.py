import cv2

image_paths = ['./Panorama-Stitching/images/real/1.jpg',
               './Panorama-Stitching/images/real/2.jpg',
               './Panorama-Stitching/images/real/3.jpg',
               './Panorama-Stitching/images/real/4.jpg',
               './Panorama-Stitching/images/real/5.jpg',]
imgs = []

#for i in range(len(image_paths)):
#    imgs.append(cv2.imread(image_paths(i)))
#    imgs[i] = cv2.resize(imgs[i],(0,0), fx=0.4,fy=0.4)
#simply scaling down the image incase the image is too big for your screen(this is optional)

#simply showing the original picture
cv2.imshow('1',imgs[0])
cv2.imshow('2',imgs[1])
cv2.imshow('3',imgs[2])
cv2.imshow('4',imgs[3])
cv2.imshow('5',imgs[4])

#stitch code
stitching = cv2.Stitcher.create()
(dummy,output) = stitching.stitch(imgs)

#checking if the procedure is successful or not
if dummy != cv2.STITCHER.OK:
    print("stitching process failed")
else:
    print("stitching process sucess!")

#show result
cv2.imshow("result", output)
cv2.waitkey(0)