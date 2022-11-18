import torch.utils.data as data

from PIL import Image
import os
import os.path

IMG_EXTENSIONS = [
    '.jpg', '.JPG', '.jpeg', '.JPEG',
    '.png', '.PNG', '.ppm', '.PPM', '.bmp', '.BMP',
]


def is_image_file(filename):
    return any(filename.endswith(extension) for extension in IMG_EXTENSIONS)

def dataloader(filepath):

    all_left_img=[]
    all_right_img=[]
    all_left_disp = []
    test_left_img=[]
    test_right_img=[]
    test_left_disp = []


    for i in range(42):
        i = i+1
        all_left_img.append("input/L"+str(i)+".bmp")
        test_left_img.append("input/L"+str(i)+".bmp")
        all_right_img.append("input/R"+str(i)+".bmp")
        test_right_img.append("input/R"+str(i)+".bmp")
        all_left_disp.append("output/D"+str(i)+".txt")
        test_left_disp.append("output/D"+str(i)+".txt")


    return all_left_img, all_right_img, all_left_disp, test_left_img, test_right_img, test_left_disp


