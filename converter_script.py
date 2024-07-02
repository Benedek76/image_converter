import sys
import os
from PIL import Image 

# RUN it in the terminal: python3 converter_script.py Image/ new/


# grab first and second argument
image_folder = sys.argv[1]
output_folder = sys.argv[2]

# check is new/ exist, if not create
if not os.path.exists(output_folder):
    os.makedirs(output_folder)

# loop through images
for filename in os.listdir(image_folder):
    img = Image.open(f'{image_folder}{filename}')
    clean_name = os.path.splitext(filename)[0]
    # print(clean_name)

    # convert images to png and save to the new folder
    img.save(f'{output_folder}{clean_name}.png', 'png')
    print('all done!')










