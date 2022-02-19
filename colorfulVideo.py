#!/usr/bin/env python3.8
# Make a fun video!
#  (c) 2021 Bradley Knockel


import numpy as np
import matplotlib.pyplot as plt
from matplotlib import animation


# define some things
n = 501          # for n by n grid; n = 11 has an interesting look
extraDelay = 10  # per frame (in milliseconds)
# extraDelay can't be 0 to make a MP4, GIF, or HTML file,
# even though extraDelay does not affect the MP4 or GIF file


# create n by n by 1 arrays: X, Y, R
X, Y = np.meshgrid(np.linspace(0, 8*np.pi, n), np.linspace(0, 8*np.pi, n), [0])[0:2]
R = np.sqrt(np.square(X-4*np.pi) + np.square(Y-4*np.pi))
# R is radial value throughout the image

# setup figure
fig = plt.figure(figsize=(1, 1), dpi=n)
plt.axes([0,0,1,1], frameon=False).axis('off') 
im = plt.imshow(  np.concatenate( (0*X+.5,0*X+.5,0*X+.5), axis=2)  )  #grey

# setup time steps
myRange = np.concatenate((np.linspace(0., 2.3, 231), np.linspace(2.3, 0., 231)))
length = len(myRange)


def animate(k):

  i = myRange[k % length]
  j = k // length

  if j==0:
    a = np.concatenate( (np.sin(X*i), np.sin(X*np.power(i,1.1)), np.sin(X*np.power(i,1.2))), axis=2)
  elif j==1:
    a = np.concatenate( (np.sin((X-8*np.pi)*i), np.sin((X-8*np.pi)*np.power(i,1.1)), np.sin((X-8*np.pi)*np.power(i,1.2))), axis=2)
  else:
    a = np.concatenate( (np.sin(X*i), np.sin((X-8*np.pi)*np.power(i,1.1)), np.sin(R*i)), axis=2)
  im.set_array( (a + 1.0)*0.5 )
  return [im]


anim = animation.FuncAnimation(fig, animate, frames=3*length, interval=extraDelay, blit=True)




######################## your options for saving or showing the animation ########################

### The following first required `sudo port install ffmpeg` on my macOS
### On Windows: https://www.geeksforgeeks.org/how-to-install-ffmpeg-on-windows/
###   though you only need the ffmpeg.exe file
anim.save('animation.mp4', writer = animation.FFMpegWriter(fps=30))

### The following makes an HTML file
### The following first required `sudo port install ffmpeg` on my macOS
### On Windows: https://www.geeksforgeeks.org/how-to-install-ffmpeg-on-windows/
###   though you only need the ffmpeg.exe file
#with open("animation.html", "w") as f:
#  print(anim.to_html5_video(), file=f)

### The following only shows (does not save) the animation
### For larger n, pygame is faster than matplotlib! For small n, pygame is jumpy and slow.
### For some reason, making the figure window large slows it down (even if n is small).
#plt.show()

### The following GIF will be a large file
#anim.save('animation.gif', writer = animation.PillowWriter(fps=30))
