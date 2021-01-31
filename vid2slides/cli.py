import click
import os
import shutil
from PIL import Image, ImageChops, ImageStat
from .v2s import extract_slides, write_to_pdf

"""
How it works:
1. ffmpeg writes keyframes to frames folder
2. checks if adjacent keyframes are the same
3. write to pdf
"""

@click.command()
@click.argument('filename')
@click.option('-o', '--output')
def cli(filename, output):
    """ Extracts a slideshow from a video presentation """
    frames_folder = os.path.join(os.getcwd(), 'frames')
    extract_slides(filename, frames_folder)
    
    if output != None:
        write_to_pdf(frames_folder, output)
    else:
        write_to_pdf(frames_folder)
    
    shutil.rmtree(frames_folder)

