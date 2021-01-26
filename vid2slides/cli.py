import click
import cv2
from skimage.metrics import structural_similarity

"""
How it works:
Detect and mask webcam
Extract slides as jpg from video by detecting when a frame is different than the last
Write jpg to ppt or pdf file
    pdf default, ppt or open source version of ppt if specified
"""

@click.command()
def cli():
    """ Extracts a slideshow from a video presentation """
    extract_slides('test.webm')
    print('slides extracted')


def extract_slides(video_path):
    vidcap = cv2.VideoCapture(video_path)
    success,previous_image = vidcap.read()
    slide_num = 0
    while success:
        # Saves previous slide if slide changes
        success,current_image = vidcap.read()
        if check_different(previous_image, current_image): 
            cv2.imwrite("slide%d.jpg" % slide_num, previous_image)
            slide_num += 1
        previous_image = current_image
    # next line saves the last slide, because it has not been saved yet
    cv2.imwrite("slide%d.jpg" % slide_num, last_image)


def check_different(image1, image2):
    """ Returns true if the frames are different, false if not """
    gray_img1 = cv2.cvtColor(image1, cv2.COLOR_BGR2GRAY)
    gray_img2 = cv2.cvtColor(image2, cv2.COLOR_BGR2GRAY)
    (score, diff) = structural_similarity(gray_img1, gray_img2, full=True)
    diff = (diff * 255).astype("uint8")
    print("Structural Similarity Index: {}".format(score))
    if (score != 1.0):
        return True
    else:
        return False
