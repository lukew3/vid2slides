import click
import os
import shutil
from .vid2slides import v2s


@click.command()
@click.argument('filename')
@click.option('-o', '--output', default='out.pdf')
def cli(filename, output):
    """ Extracts a slideshow from a video presentation """
    v2s(filename, output)
