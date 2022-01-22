import pandas as pd
from PIL import Image, ImageDraw, ImageFont


def generate_certificate():

    data = pd.read_csv("names.csv")

    name_list = data["Name"].tolist()

    for i in range(len(name_list)):

        # Specify your certificate image route
        im = Image.open("hello-coders-certificate.jpg")

        # Extract Image width and height
        image_width = im.width
        image_height = im.height

        award = '"Hello Coders" Mentorship Program'
        reason = "18th October - 26th November 2021"

        # Draw Image
        d = ImageDraw.Draw(im)
        d = draw_name(d, name_list[i], image_width)
        d = draw_award(d, award, image_width)
        d = draw_date(d, reason, image_width)

        # Saving Certificate
        im.save(f"certificates/certificate_{name_list[i]}.pdf")


def draw_name(drawing, name, image_width):
    # Specify Y-Axis Height, and Text Color (Adjust these according to your needs)
    y_axis_height = 285

    # Blue: (0, 137, 209)
    # Purple: (128, 0, 128)
    # Black: (0, 0, 0)
    text_color = (0, 0, 0)

    # Import text font (make sure text font is downloaded and in project root directory)
    font = ImageFont.truetype("fonts/Montserrat-Bold.ttf", 25)

    # Extracting text width
    text_width, _ = drawing.textsize(name, font=font)

    # Writing text (Adjust calculation according to your needs)
    drawing.text(
        ((image_width - text_width) / 3, y_axis_height),
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
        ((image_width - text_width) / 4.3, y_axis_height),
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
        ((image_width - text_width) / 3.3, y_axis_height),
        name,
        fill=text_color,
        font=font,
    )

    return drawing


if __name__ == "__main__":
    generate_certificate()
    print("Certificates Generated!")
