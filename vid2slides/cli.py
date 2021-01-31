import click
import os
from PIL import Image, ImageChops, ImageStat

"""
How it works:
1. ffmpeg writes keyframes to frames folder
2. checks if adjacent keyframes are the same
3. write to pdf
"""

@click.command()
@click.argument('filename')
def cli(filename):
    """ Extracts a slideshow from a video presentation """
    extract_slides(filename)


def extract_slides(video_path):
    # Fill a folder with all of the images
    width = 1280
    height = 720
    cur_dir = os.getcwd()
    frames_folder = os.path.join(cur_dir, 'frames')
    if not os.path.exists(frames_folder):
        os.makedirs(frames_folder)
    #should I add an else statement here to delete frames folder if it exists?
    # Is -s WxH necessary?
    script = f'ffmpeg -i {video_path} -vsync 0 -vf select="eq(pict_type\,PICT_TYPE_I)" -f image2 frames/foo-%03d.jpeg'
    os.system(script)
    remove_duplicates(frames_folder)
    write_to_pdf(frames_folder)


def remove_duplicates(frames_folder):
    """ Goes through each file in the passed folder and removes if difference ratio is less than 2.0"""
    filename_list = []
    for filename in os.listdir(frames_folder):
        filename_list.append(filename)
    filename_list.sort()
    last_frame = Image.open(frames_folder + '/' + filename_list[0])
    duplicates_list = []
    for i in range(1, len(filename_list)):
        cur_frame = Image.open(frames_folder + '/' + filename_list[i])
        diff_img = ImageChops.difference(cur_frame, last_frame)
        stat = ImageStat.Stat(diff_img)
        diff_ratio = 100 * (sum(stat.mean) / (len(stat.mean) * 255))
        # print(filename_list[i] + ": " + str(diff_ratio))
        # If the images are identical, remove the previous file
        # 2.0 is what worked for me, might want to tweak this with an option
        if diff_ratio <= 2.0:
            duplicates_list.append(frames_folder + '/' + filename_list[i-1])
        last_frame = cur_frame
    #remove each image in list
    for image in duplicates_list:
        os.remove(image)


def write_to_pdf(frames_folder):
    frames_list = []
    images = []
    for filename in os.listdir(frames_folder):
        frames_list.append(filename)
    frames_list.sort()
    for frame in frames_list:
        images.append(Image.open(frames_folder + '/' + frame).convert("RGB"))
    images[0].save("out.pdf", save_all=True, append_images=images[1:])
    print("Output written to out.pdf")
