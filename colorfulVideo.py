#!/usr/bin/env python3.13
# Make a fun video!
#  (c) 2021 Bradley Knockel


import numpy as np
import matplotlib.pyplot as plt
from matplotlib import animation


# define some things
n = 501          # for n by n grid; n = 11 has an interesting look
extraDelay = 10  # per frame (in milliseconds)
# Use a positive extraDelay because some animation backends dislike 0.
# For saved MP4/GIF files, fps controls the playback speed.


# create n by n arrays: X, Y, R
X, Y = np.meshgrid(np.linspace(0, 8*np.pi, n), np.linspace(0, 8*np.pi, n))
R = np.sqrt(np.square(X - 4*np.pi) + np.square(Y - 4*np.pi))
# R is radial value throughout the image

# setup figure
fig = plt.figure(figsize=(1, 1), dpi=n)
plt.axes([0,0,1,1], frameon=False).axis('off') 
im = plt.imshow(  np.full((n, n, 3), 0.5), interpolation='nearest' )  #grey

# setup time steps
myRange = np.concatenate((np.linspace(0., 2.3, 231), np.linspace(2.3, 0., 231)))
length = len(myRange)


def animate(k):

  i = myRange[k % length]
  j = k // length

  if j==0:
    a = np.dstack( (np.sin(X*i), np.sin(X*np.power(i,1.1)), np.sin(X*np.power(i,1.2))) )
  elif j==1:
    a = np.dstack( (np.sin((X-8*np.pi)*i), np.sin((X-8*np.pi)*np.power(i,1.1)), np.sin((X-8*np.pi)*np.power(i,1.2))) )
  else:
    a = np.dstack( (np.sin(X*i), np.sin((X-8*np.pi)*np.power(i,1.1)), np.sin(R*i)) )

  im.set_array( (a + 1.0)*0.5 )
  return [im]


anim = animation.FuncAnimation(fig, animate, frames=3*length, interval=extraDelay, blit=True)




######################## your options for saving or showing the animation ########################

### The following first required `sudo port install ffmpeg` on my macOS
### On Windows: https://www.geeksforgeeks.org/how-to-install-ffmpeg-on-windows/
###   though you only need the bin folder of the Windows build ZIP file.
###   Just put it in your current directory:
###      plt.rcParams['animation.ffmpeg_path'] = r'bin\ffmpeg.exe'
###   Perhaps just install ffmpeg via Cygwin! Then...
###      plt.rcParams['animation.ffmpeg_path'] = r'C:\cygwin64\bin\ffmpeg.exe'
###   though Cygwin's ffmpeg may not include a working H.264 encoder.
###
### Ideally, for MP4/H.264, set an even n above in my code
#anim.save('animation.mp4', writer = animation.FFMpegWriter(fps=30))

### The following makes an HTML file
### The following first required `sudo port install ffmpeg` on my macOS
### On Windows: https://www.geeksforgeeks.org/how-to-install-ffmpeg-on-windows/
###   though you only need the bin folder of the Windows build ZIP file.
###   Just put it in your current directory:
###      plt.rcParams['animation.ffmpeg_path'] = r'bin\ffmpeg.exe'
###   Perhaps just install ffmpeg via Cygwin! Then...
###      plt.rcParams['animation.ffmpeg_path'] = r'C:\cygwin64\bin\ffmpeg.exe'
###   though Cygwin's ffmpeg may not include a working H.264 encoder.
###
### Ideally, for MP4/H.264, set an even n above in my code
#with open("animation.html", "w") as f:
#  print(anim.to_html5_video(), file=f)

### The following only shows (does not save) the animation
### For larger n, pygame is faster than matplotlib! For small n, pygame is jumpy and slow.
### For some reason, making the figure window large slows it down (even if n is small).
plt.show()

### The following GIF will be a very large file
#anim.save('animation.gif', writer = animation.PillowWriter(fps=30))
