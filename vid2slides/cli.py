import click
import os
import shutil
from .v2s import v2s 

"""
How it works:
1. ffmpeg writes keyframes to frames folder
2. checks if adjacent keyframes are the same
3. write to pdf
"""


@click.command()
@click.argument('filename')
@click.option('-o', '--output', default='out.pdf')
def cli(filename, output):
    """ Extracts a slideshow from a video presentation """
    v2s(filename, output)
