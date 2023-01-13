import os
import pandas as pd
from PIL import Image, ImageDraw, ImageFont


def generate_certificate(image_list, award, reason, csv_list):

    for i in range(len(csv_list)):
        data = pd.read_csv(f"csv/{csv_list[i]}.csv")

        name_list = data["Name"].tolist()
        team_list = data["Team"].tolist()


        for j in range(len(name_list)):

            # Specify your certificate image route
            im = Image.open(f"templates/{image_list[i]}")

            # Extract Image width and height
            image_width = im.width
            # image_height = im.height

            # Draw Image
            d = ImageDraw.Draw(im)
            d = draw_name(d, name_list[j], image_width)
            # d = draw_award(d, award, image_width)
            # d = draw_date(d, reason, image_width)

            # Saving Certificate
            im.save(f"generated-certificates/{team_list[j]}/certificate_{name_list[j]}.png")


def draw_name(drawing, name, image_width):
    # Specify Y-Axis Height, and Text Color (Adjust these according to your needs)
    y_axis_height = 600

    # Blue: (0, 137, 209)
    # Purple: (128, 0, 128)
    # Black: (0, 0, 0)
    # White (255, 255, 255)
    text_color = (226, 190, 118)

    # Import text font (make sure text font is downloaded and in project root directory)
    font = ImageFont.truetype("fonts/TeanAeganRegular.ttf", 60)

    # Extracting text width
    text_width, _ = drawing.textsize(name, font=font)

    # Writing text (Adjust calculation according to your needs)
    drawing.text(
        ((image_width - text_width) / 2, y_axis_height),
        name,
        fill=text_color,
        font=font,
    )

    # Left Aligned Text
    # drawing.text(
    #     (300, y_axis_height),
    #     name,
    #     fill=text_color,
    #     font=font,
    # )

    return drawing


def draw_award(drawing, name, image_width):
    # Specify Y-Axis Height, and Text Color (Adjust these according to your needs)
    y_axis_height = 397

    # Blue: (0, 137, 209)
    # Purple: (128, 0, 128)
    # Black: (0, 0, 0)
    text_color = (0, 0, 0)

    # Import text font (make sure text font is downloaded and in project root directory)
    font = ImageFont.truetype("fonts/Century-Schoolbook-Bold-font.ttf", 28)

    # Extracting text width
    text_width, _ = drawing.textsize(name, font=font)

    # Writing text (Adjust calculation according to your needs)
    drawing.text(
        ((image_width - text_width) / 2 - 163, y_axis_height),
        name,
        fill=text_color,
        font=font,
    )

    # Left Aligned Text
    # drawing.text(
    #     (300, y_axis_height),
    #     name,
    #     fill=text_color,
    #     font=font,
    # )

    return drawing


def draw_date(drawing, name, image_width):
    # Specify Y-Axis Height, and Text Color (Adjust these according to your needs)
    y_axis_height = 460
    text_color = (0, 0, 0)

    # Import text font (make sure text font is downloaded and in project root directory)
    font = ImageFont.truetype("fonts/arial.ttf", 20)

    # Extracting text width
    text_width, _ = drawing.textsize(name, font=font)

    # Writing text (Adjust calculation according to your needs)
    drawing.text(
        ((image_width - text_width) / 2 - 164, y_axis_height),
        name,
        fill=text_color,
        font=font,
    )

    return drawing
