import cv2
import numpy as np
import pathlib as pl
import os
import predict

def image_resize(image: np.ndarray, width = None, height = None, inter = cv2.INTER_AREA):
    '''
    Resize image while keeping it's aspect ratio
    '''
    # initialize the dimensions of the image to be resized and
    # grab the image size
    dim = None
    (h, w) = image.shape[:2]

    # if both the width and height are None, then return the
    # original image
    if width is None and height is None:
        return image

    # check to see if the width is None
    if width is None:
        # calculate the ratio of the height and construct the
        # dimensions
        r = height / float(h)
        dim = (int(w * r), height)

    # otherwise, the height is None
    else:
        # calculate the ratio of the width and construct the
        # dimensions
        r = width / float(w)
        dim = (width, int(h * r))

    # resize the image
    resized = cv2.resize(image, dim, interpolation = inter)

    # return the resized image
    return resized

def expand_dataset():
    photo_path = pl.Path('./photos/')
    
    photo_names = [photo_path / photo for photo in os.listdir(photo_path)]
    photo_names.remove(pl.WindowsPath('./photos/new'))

    angle_delta = 45
    
    for photo_name in photo_names:
        photo = cv2.imread(str(photo_name))
        angle = 0
        print(f"Processing {photo_name.stem}")
        for i in range(0, 360, angle_delta):
            scale = np.random.uniform(1.0, 1.5)
            rot_mat = cv2.getRotationMatrix2D((photo.shape[0] / 2, photo.shape[1] / 2), angle, scale)
            new_image = cv2.warpAffine(photo, rot_mat, (photo.shape[0], photo.shape[1]))
            cv2.imwrite(f"./photos/new/{photo_name.stem}_{i}.jpg", new_image)
            angle += angle_delta
            

if __name__ == '__main__':
    pass
    
        
        
    
