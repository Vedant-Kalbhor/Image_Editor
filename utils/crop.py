def crop_image(image,x,y,w,h):
    return image[int(y):int(y+h),int(x):int(x+w)]