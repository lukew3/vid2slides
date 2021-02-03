# vid2slides
A tool for extracting a slideshow from a video presentation. 

## Installation
Requires ffmpeg.

Package can be installed via pip: `pip install vid2slides`

## Usage
To use vid2slides on the command line use: `vid2slides <input-video>`
By default this will write `out.pdf` to your current directory.

To use in python:
```
from vid2slides import v2s
v2s(<input-video>)
```

## How it works
1. Video is split into its keyframes by ffmpeg. Using keyframes allows only the most important slides to be saved as images to parse later.
2. Slides are compared, and duplicates are removed. The Pillow package compares two adjacent images with ImageChops and returns a difference percent. The default percent used to determine difference is 2. If the difference between the images is less than 2%, it is assumed that they are identical, and one of the slides is removed.
3. Slides are combined and saved as out.pdf, or filename specified with -o.
