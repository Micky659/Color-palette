# This program can detect and display the dominant colors in a picture.
# Run the program with path of the image and number of colors and it will produce two images one a palette
# with a number of major colors in the picture and the second picture is a combination of the image and palette

from PIL import Image
import matplotlib.pyplot as plt
from scipy import cluster
import pandas as pd
import math


# Function build palette uses kmeans algorithm to find the dominant colors
def build_palette(input_file, num):
    input_img = plt.imread(input_file)

    red, green, blue = [], [], []
    for line in input_img:
        for pixel in line:
            r, g, b = pixel
            red.append(r)
            green.append(g)
            blue.append(b)

    df = pd.DataFrame({
        'red': red,
        'green': green,
        'blue': blue
    })

    df['standardRed'] = cluster.vq.whiten(df['red'])
    df['standardGreen'] = cluster.vq.whiten(df['green'])
    df['standardBlue'] = cluster.vq.whiten(df['blue'])

    color_palette, distort = cluster.vq.kmeans(df[['standardRed', 'standardGreen', 'standardBlue']], num)
    colors = []
    red_std, green_std, blue_std = df[['red', 'green', 'blue']].std()
    for color in color_palette:
        scaledRed, scaledGreen, scaledBlue = color
        colors.append((
            math.ceil(scaledRed * red_std),
            math.ceil(scaledGreen * green_std),
            math.ceil(scaledBlue * blue_std)
        ))

    pil_img = Image.open(input_file)
    pil_width, pil_height = pil_img.size

    if pil_height > pil_width:
        height = math.floor(pil_height / 6)
    else:
        height = math.floor(pil_height / 4)

    palette = Image.new('RGB', (pil_width, height), (255, 255, 255))
    color_space = math.floor(pil_width / num)
    offset = math.floor(color_space / 14)
    total_offset = offset * (num + 1)
    color_width = math.floor((pil_width - total_offset) / num)
    color_space = color_width + offset

    total_color_width = (color_width + (pil_width - (color_space * num))) - offset

    x_offset = 0
    for i in range(len(colors)):
        if i == len(colors) - 1:
            new_img = Image.new('RGB', (total_color_width, height), colors[i])
            palette.paste(new_img, (x_offset, 0))

        elif i == 0:
            new_img = Image.new('RGB', (color_width, height), colors[i])
            palette.paste(new_img, (offset, 0))

            x_offset += color_space + offset
        else:
            new_img = Image.new('RGB', (color_width, height), colors[i])
            palette.paste(new_img, (x_offset, 0))

            x_offset += color_space

    path = input_file.split('/')
    global image
    image = path[1].split('.')
    palette_file = 'Output/' + 'palette of ' + image[0] + '.' + image[1]
    palette.save(palette_file)

    combine_palette(input_file, palette_file)


# Combine palette function combines the base input image with the palette image created in the above function
def combine_palette(original_image, color_palette):
    base_img = Image.open(original_image)
    base_width, base_height = base_img.size
    palette_img = Image.open(color_palette)
    palette_width, palette_height = palette_img.size

    height_offset = math.ceil(base_height / 20)
    if base_height > base_width:
        height_offset = math.ceil(base_height / 30)

    total_width = base_width
    total_height = base_height + palette_height + (height_offset * 2)

    combine = Image.new('RGB', (total_width, total_height), (255, 255, 255))

    combine.paste(base_img, (0, 0))
    combine.paste(palette_img, (0, base_height + height_offset))
    output_file = 'Output/' + image[0] + ' with palette.' + image[1]
    combine.save(output_file)


def main(image_file, num_colors):
    try:
        build_palette(image_file, int(num_colors))
    except Exception as e:
        print(e)


# Output will be stored in the folder named Output with the same extension as the input image
if __name__ == '__main__':
    img = input("Enter image location: ")
    number = input("Enter number of colors in palette: ")
    if len(number) < 1:
        number = 5
    main(img, number)

# Created by Akshat Kothari (April, 2021)
