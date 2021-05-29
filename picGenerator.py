#!/usr/bin/env python3.8
# Create a colorful-pattern in 4 steps!
#  (c) 2019 Bradley Knockel



# (1) choose the length in pixels of the square image (n=16 for favicon)
n = 300

# (2) choose which pattern you want from the list near bottom of this file
pattern = 1
# modify or create your own!

# (3) choose the name of your PNG file
name = 'pattern'
# set name to 0 (name = 0) if you do not want to create a file
# existing files will be overwritten

# (4) run this file to display your image and create a PNG file

# *5* On the Internet, you can find and download a free program called
# PNGOUT to optimize your PNG file! Sometimes, JPG can give smaller files.



import numpy as np
from PIL import Image   # pip install pillow



## define X, Y, and R

# from left and top
# The [0] and [0:2] added to make X and Y 3D arrays for np.concatenate()
X, Y = np.meshgrid(np.linspace(0, 2*np.pi, n), np.linspace(0, 2*np.pi, n), [0])[0:2]

R = np.sqrt(np.square(X - np.pi) + np.square(Y - np.pi))  #from center



## define distances from corners
Rnw = np.sqrt(np.square(X) + np.square(Y))
Rne = np.sqrt(np.square(X - 2*np.pi) + np.square(Y))
Rsw = np.sqrt(np.square(X) + np.square(Y-2*np.pi))
Rse = np.sqrt(np.square(X - 2*np.pi) + np.square(Y - 2*np.pi))

## define distances from the corners of an isosceles triangle
R1 = np.sqrt(np.square(X - np.pi) + np.square(Y - 2/3*np.pi))  #top
R2 = np.sqrt(np.square(X - 2/3*np.pi) + np.square(Y - 4/3*np.pi))  #bottom left
R3 = np.sqrt(np.square(X - 4/3*np.pi) + np.square(Y - 4/3*np.pi))  #bottom right



## LIST OF AVAILABLE PATTERNS
#Add your own or edit them as you wish.
#r = red, g = green, b = blue have values in the range [0,1]
if pattern == 0:
    r = X/(2*np.pi)
    g = Y*0+.75
    b = R/(2*np.pi)
elif pattern == 1:
    r = .5*np.sin(1*X) + .5
    g = .5*np.sin(2*X) + .5
    b = .5*np.sin(4*X) + .5
elif pattern == 2:
    r = .5*np.sin(2*Rnw) + .5
    g = .5*np.sin(1*Rnw) + .5
    b = .5*np.sin(.5*Rnw) + .5
elif pattern == 3:
    r = .5*np.sin(2*R) + .5
    g = .5*np.sin(1*R) + .5
    b = .5*np.sin(4*R) + .5
elif pattern == 4:
    r = .5*np.sin(10*R) + .5
    g = .5*np.sin(20*R) + .5
    b = .5*np.sin(40*R) + .5
elif pattern == 5:
    r = .5*np.cos(5*R1) + .5
    g = .5*np.cos(5*R2) + .5
    b = .5*np.cos(5*R3) + .5
elif pattern == 6:
    r = .5*np.cos(50*R1) + .5
    g = .5*np.cos(50*R2) + .5
    b = .5*np.cos(50*R3) + .5
elif pattern == 7:
    r = .5*np.cos(1*R1) + .5
    g = .5*np.cos(2*R2) + .5
    b = .5*np.cos(4*R3) + .5
elif pattern == 8:
    r = .5*np.cos(1*X) + .5
    g = .5*np.cos(2*X) + .5
    b = .5*np.cos(4*X) + .5
elif pattern == 9:
    r = .5*np.cos(4*X) + .5
    g = .5*np.cos(2*X) + .5
    b = .5*np.cos(1*X) + .5
elif pattern == 10:
    r = .5*np.cos(1*Rsw) + .5
    g = .5*np.cos(1*Rne) + .5
    b = .5*np.cos(1*R) + .5
elif pattern == 11:
    r = .5*np.cos(2*Rsw) + .5
    g = .5*np.cos(2*Rne) + .5
    b = 0*np.cos(1*R) + .5
elif pattern == 12:
    r = .5*np.cos(2*X) + .5
    g = .5*np.cos(3*X) + .5
    b = .5*np.cos(1*X) + .5
elif pattern == 13:
    r = .5*np.sin(2*X) + .5
    g = .5*np.sin(1*X) + .5
    b = .5*np.sin(3*X) + .5
elif pattern == 14:
    r = .5*np.sin(1*X) + .5
    g = .5*np.sin(2*X+2*pi/3) + .5
    b = .5*np.sin(3*X+4*pi/3) + .5
elif pattern == 15:
    r = .5*np.sin(1*Rse) + .5
    g = .5*np.sin(2*Rse) + .5
    b = .5*np.sin(.5*Rse) + .5
elif pattern == 16:
    r = .5*np.cos(1*Rne) + .5
    g = .5*np.cos(1*Rsw) + .5
    b = .5*np.cos(2*R) + .5
elif pattern == 17:
    r = .5*np.sin(2*R) + .5
    g = .5*np.sin(1*R) + .5
    b = .5*np.sin(4*X) + .5
else:
    print('error: not a valid pattern')
    quit()

## actually create the image
pic = np.concatenate( (r*255.999, g*255.999, b*255.999), axis=2)
image = Image.fromarray(pic.astype('uint8'), 'RGB')
image.show()
if isinstance(name, str):
    #feel free to use JPG
    fullname = name + '.png'
    image.save(fullname, 'PNG')
    print(fullname + ' has been created')
