import txt
from cmath import sqrt
import os

#The script allows to go through a series of premade .txt files that contain the area and
#the perimeter of a scale bar from the SEM image. From this data, it finds the length of the
#scale bar in pixels by solving a quadratic equation.

#It was determined prior to writing this script that if the length of the scale bar is
#in the range from 0 to 150 pxls, then it is a 100 nm scaled image. Otherwise, it is a
#1 micrometer scale image.

#After determining the length of the scale bar and the magnification used to take the image, the
#information is appended to the jpg file with the same filename.

#This allows to pass the "scale" of the image as a parameter through the file's name. This scale will
#later be used to scale the image in ImageJ prior to further processing it.

#The script eliminates the need to manually set scale in ImageJ.

#@author Lidmila Strelnikova
#@version 14.04.2021



#Gets the value of area and perimeter of the rectangle from the
#specified .txt file
#note: it is assumed that the .txt file contains only one line with only
#two values, the first of which is area, the second is perimeter
#@param file_source the address of the .txt file
#@return ap_array array whose first element is the area, and second - perimeter
#
def getAP(file_source, filename):
    
    file = open(file_source + filename + ".txt", "r").readlines()
    line = file[0].split() 
    area = float(line[0])
    parameter = float(line[1])
    ap_array = [area, parameter]
    return ap_array

#Receives the array whose first element is the area, and second - perimeter,
#then solves the system of equations:
#xy = area
#2x+2y = perimeter
#Returns the two roots as an array.
#note: it is assumed D>0 always
#@param ap_array array whose first element is the area, and second - perimeter
#@return roots array with two roots, or lengths of the rectangle
#
def getRoots(ap_array):
    ar = ap_array[0]
    p = ap_array[1]

    #quadratic equation
    a = 1
    b = (-1)*p/2
    c = ar
    D=b**2-4*c
    
    y1_comp=((-1)*b + sqrt(D))/2
    y1 = y1_comp.real
    y2_comp=((-1)*b - sqrt(D))/2
    y2 = y2_comp.real

    x1= p/2-y1
    x2=p/2-y2

    if y1 < 0:
        root1 = y2
        root2 = x2
    elif y2 < 0:
        root1 = y1
        root2 = x1
    
    elif (y1 and y2 > 0):
        if x1 < 0:
            root1 = y2
            root2 = x2
        elif x2 < 0:
            root1 = y1
            root2 = x1
        else:
            root1 = y1
            root2 = x1
    roots = [root1, root2]
       
    return roots

#Makes the biggest side of the rectangle the scale.
#If the number of pixels is less that 150, it is assumed that the scale is 100 nm,
#1 micrometer otherwise.
#@param roots the two sides of the sclale bar
#@return scale the string of the format: -#pxls-#-units that will later be
#appended to the image's filename and used for automatic scaling
#
def getScale(roots):
    scale = ""
    pxls = max(roots[0],roots[1])
    if pxls > 0 and pxls < 150:
        scale = "-" + scale + str(round(pxls,2)) + "-100-nm"
    else:
        scale = "-" + scale + str(round(pxls,2)) + "-1-microm"
    return scale

#Appends the scale as a variable to the specified .jpeg file
#@param file_source the directory where the file is at
#@param filename the name of the file before the modification (without the extension)
#@scale the string of the form -#pxls-#-units
#
def appendScaletoName(file_source, filename, scale):
    os.chdir(file_source)
    os.rename(filename + ".jpg", filename + scale + ".jpg")

#Takes a .txt file of interest from the specified folder and performs a series of operations
#on it to retreive a the scale which is represented by a string which later
#gets appended to the .jpg file with the same filename in another specified folder
#@param data_source the directory where the .txt file is at
#@param image_sourse the directory where the .jpg file is at
#@param filename the name of the file of interest (without the extension)
#
def doDaJob(data_source, image_source, filename):
    ap_array = getAP(data_source, filename)
    roots = getRoots(ap_array)
    scale = getScale(roots)
    appendScaletoName(image_source, filename, scale)
    
    
#Main body
#
data_source = "C:/Users/test/Desktop/Job/Cobalt Ferrites/100_ Trial2 txt_results/"
image_source = "C:/Users/test/Desktop/Job/Cobalt Ferrites/100_ Trial2 copy/"




for file in os.listdir(data_source):
    splitArr = file.split(".")
    filename = splitArr[0]
    doDaJob(data_source, image_source, filename)
    
