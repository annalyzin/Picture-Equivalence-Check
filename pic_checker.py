from os import listdir
from os.path import isfile, join
import numpy as np
import cv2

# set directories
original = raw_input("Input first directory path: ")
revised = raw_input("Input second directory path: ")

# get filenames in directory
original_files = [f for f in listdir(original) if isfile(join(original, f))]
revised_files = [f for f in listdir(revised) if isfile(join(revised, f))]


check = []
for i in range(0, len(original_files)):

    # read in pics
    original_img = cv2.imread(original + original_files[i],0)
    revised_img = cv2.imread(revised + revised_files[i],0)

    # check whether pics are exactly equal
    res = (original_img == revised_img)
    check.append(res.all())


print check

print [i for i, x in enumerate(check) if x == False]
