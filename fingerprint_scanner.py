import numpy as np
import matplotlib.pyplot as plt
import cv2
from zipfile import ZipFile

########################################
#            Import files              #
########################################

# specifying the zip file name
file_name = "DB4_B.zip"

# opening the zip file in READ mode
with ZipFile(file_name, 'r') as zip:

    zip.extractall()