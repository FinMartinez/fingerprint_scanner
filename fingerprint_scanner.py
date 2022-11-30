import numpy as np
import matplotlib.pyplot as plt
import cv2
from zipfile import ZipFile

########################################
#            Import files              #
########################################

file_name = 'DB4_B.zip'

with ZipFile(file_name, 'r') as zip:
    zip.printdir()

    print('Extracting all the files now...')
    zip.extractall()
    print('Done!')