import pandas as pd
from PIL import Image, ImageDraw, ImageFont


def generate_certificate():

    data = pd.read_csv("names.csv")

    name_list = data["Name"].tolist()

    for i in range(len(name_list)):

        # Specify your certificate image route
        im = Image.open("new_certificate.jpg")

        # Extract Image width and height
        image_width = im.width
        image_height = im.height

        award = "Hello Coders Program"
        reason = "yes"

        # Draw Image
        d = ImageDraw.Draw(im)
        d = draw_name(d, name_list[i], image_width)
        d = draw_award(d, award, image_width)
        d = draw_reason(d, reason, image_width)

        # Saving Certificate
        im.save(f"certificates/certificate_{name_list[i]}.pdf")


def draw_name(drawing, name, image_width):
    # Specify Y-Axis Height, and Text Color (Adjust these according to your needs)
    y_axis_height = 540
    text_color = (0, 137, 209)

    # Import text font (make sure text font is downloaded and in project root directory)
    font = ImageFont.truetype("fonts/Montserrat-Regular.ttf", 60)

    # Extracting text width
    text_width, _ = drawing.textsize(name, font=font)

    # Writing text (Adjust calculation according to your needs)
    drawing.text(
        ((image_width - text_width) / 2, y_axis_height),
        name,
        fill=text_color,
        font=font,
    )

    return drawing


def draw_award(drawing, name, image_width):
    # Specify Y-Axis Height, and Text Color (Adjust these according to your needs)
    y_axis_height = 740
    text_color = (0, 137, 209)

    # Import text font (make sure text font is downloaded and in project root directory)
    font = ImageFont.truetype("fonts/arial.ttf", 50)

    # Extracting text width
    text_width, _ = drawing.textsize(name, font=font)

    # Writing text (Adjust calculation according to your needs)
    drawing.text(
        ((image_width - text_width) / 2, y_axis_height),
        name,
        fill=text_color,
        font=font,
    )

    return drawing


def draw_reason(drawing, name, image_width):
    # Specify Y-Axis Height, and Text Color (Adjust these according to your needs)
    y_axis_height = 900
    text_color = (0, 137, 209)

    # Import text font (make sure text font is downloaded and in project root directory)
    font = ImageFont.truetype("fonts/arial.ttf", 30)

    # Extracting text width
    text_width, _ = drawing.textsize(name, font=font)

    # Writing text (Adjust calculation according to your needs)
    drawing.text(
        ((image_width - text_width) / 2, y_axis_height),
        name,
        fill=text_color,
        font=font,
    )

    return drawing


if __name__ == "__main__":
    generate_certificate()
    print("Certificates Generated!")
