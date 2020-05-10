from glitch_this import ImageGlitcher
from PIL import Image
import os
from datetime import datetime

time_start = datetime.now()

# 1 - Defining a variable to use the glitch module
glitcher = ImageGlitcher()

# 2 - Defining the paths to get the images and output the glitched images
# 2.1 - Path of raw images
rawDir = r'C:\Users\conta\Desktop\source'
# 2.2 - Path of glitched images (output)
modDir = r'C:\Users\conta\Desktop\output'

# 3 - Making sure that the output folder exists
if os.path.exists(modDir) == False:
    os.makedirs(r'C:\Users\conta\Desktop\output')

# 4 - Glitch the images of the desired folder
for rawImage in os.listdir(rawDir):
    start = datetime.now()
    img = Image.open(rawDir + "/" + str(rawImage))
    rgbImg = img.convert('RGB')
    glitchImage = glitcher.glitch_image(rgbImg, 10, color_offset=True)
    glitchImage.save(modDir + '/' + rawImage[:-4] + '-glitch.jpg')
    end = datetime.now()
    print(f'{rawImage} done in {end - start}!')

time_end = datetime.now()

# 5 - Print the progress of the glitching
print(f'All done! The process took {time_end - time_start} in total to finish.' '\n'
      'Check the folder to see your glitched images')
