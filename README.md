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
