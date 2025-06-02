import cv2

def rotate_image(image,angle):
    (h,w)=image.shape[:2]
    center=(w//2,h//2)
    mat=cv2.getRotationMatrix2D(center,angle,1.0)
    rotated=cv2.warpAffine(image,mat,(w,h))
    return rotated
