import pyqrcode


def Generator(Urlru):
    # String which represents the QR code
    Link = Urlru

    # Generate QR code
    url = pyqrcode.create(Link)

    # Create and save the svg file naming "myqr.svg"
    url.svg("myqr.svg", scale=8)

    # Create and save the png file naming "myqr.png"
    url.png('myqr.png', scale=6)