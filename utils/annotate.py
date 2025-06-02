import cv2

def annotate_image(image,text,position,color):
    font=cv2.FONT_HERSHEY_SIMPLEX
    font_scale=1
    thickness=2
    cv2.putText(image,text,position,font,font_scale,color,thickness)
    return image