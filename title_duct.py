from PIL import ImageFont
from datetime import datetime


def draw_title_duct(draw, motor_count):

    try:
        font = ImageFont.truetype(
            "arial.ttf",
            18
        )

    except:

        font = ImageFont.load_default()

    draw.rectangle(
        (
            1280,
            1470,
            1700,
            1560
        ),
        outline="black",
        width=2
    )

    today = datetime.now().strftime(
        "%d-%m-%Y"
    )

    draw.text(
        (
            1300,
            1480
        ),
        "AUTOPANEL AI",
        fill="black",
        font=font
    )

    draw.text(
        (
            1300,
            1505
        ),
        "Project : ABB EngineeredX",
        fill="black",
        font=font
    )

    draw.text(
        (
            1300,
            1525
        ),
        f"Motors : {motor_count}",
        fill="black",
        font=font
    )

    draw.text(
        (
            1300,
            1545
        ),
        today,
        fill="black",
        font=font
    )