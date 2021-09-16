from skimage import img_as_ubyte
import numpy as np
from skimage import io
import os

def main():

    path = "F:\IV_Năm_ĐH\DH_Nam III (HK I)\AI\Python\\anh\Tony_Blair"
    image = read_images(path)
    image = img_as_ubyte(image)
    io.imsave("Image4.jpg",image)

# Read all jpg images in folder.
def read_images(path):
    #Create array of array of images.
    images_array = np.zeros((250, 250, 3), dtype=np.float64)
    count=0
    #List all files in the directory and read points from text files one by one
    for file_path in sorted(os.listdir(path)):
        if file_path.endswith('.jpg'):
            # Read image found.
            img = io.imread(os.path.join(path, file_path))
            # Convert to float_ing point
            img = np.float32(img) / 255.0
            count = count+1
            # Add to array of images
            images_array += img
    images_array=images_array/count
    return images_array
main()