from main import generate_certificate


def set_params():
    # Image (Certificate) name
    image = "updated-certificate.png"

    # Award Name
    award = "Hello Coders Mentorship Program - S1 2022"

    # Reason/Date
    reason = "16th February - 8th April 2022"

    generate_certificate(image, award, reason)


if __name__ == "__main__":
    set_params()
    print("Certificates Generated!")
