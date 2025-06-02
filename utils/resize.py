import cv2

def resize_image_by_scale(image,scale_percent):

    if scale_percent<=0:
        raise ValueError("Scale should be greater than 0.")
    
    width=int(image.shape[1]*scale_percent/100)
    height=int(image.shape[0]*scale_percent/100)

    resized=cv2.resize(image,(width,height),interpolation=cv2.INTER_AREA)

    return resized