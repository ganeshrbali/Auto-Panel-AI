from PIL import Image, ImageDraw, ImageFont


def generate_wiring_layout(routes):

    WIDTH = 2200
    HEIGHT = 2500

    img = Image.new(
        "RGB",
        (WIDTH, HEIGHT),
        "white"
    )

    draw = ImageDraw.Draw(img)

    try:
        font = ImageFont.truetype(
            "arial.ttf",
            22
        )
    except:
        font = ImageFont.load_default()

    # MAIN MCCB
    draw.rectangle(
        (100,100,250,160),
        outline="black",
        width=3
    )

    draw.text(
        (130,120),
        "MCCB",
        fill="blue",
        font=font
    )

    y = 250

    motor_no = 1

    for route in routes:

        if route["type"] == "POWER":

            if route["from"] == "MCCB":

                # KM
                draw.rectangle(
                    (500,y,620,y+60),
                    outline="black",
                    width=2
                )

                draw.text(
                    (530,y+15),
                    f"KM{motor_no}",
                    fill="blue",
                    font=font
                )

                # OLR
                draw.rectangle(
                    (900,y,1020,y+60),
                    outline="black",
                    width=2
                )

                draw.text(
                    (930,y+15),
                    f"OL{motor_no}",
                    fill="blue",
                    font=font
                )

                # TB
                draw.rectangle(
                    (1300,y,1420,y+60),
                    outline="black",
                    width=2
                )

                draw.text(
                    (1330,y+15),
                    f"TB{motor_no}",
                    fill="blue",
                    font=font
                )

                # wires

                draw.line(
                    (250,130,500,y+30),
                    fill="red",
                    width=3
                )

                draw.line(
                    (620,y+30,900,y+30),
                    fill="red",
                    width=3
                )

                draw.line(
                    (1020,y+30,1300,y+30),
                    fill="red",
                    width=3
                )

                motor_no += 1

                y += 150

    return img