from PIL import Image, ImageDraw, ImageFont


def generate_plc_page(selected_components):

    WIDTH = 2200
    HEIGHT = 2000

    img = Image.new("RGB", (WIDTH, HEIGHT), "white")
    draw = ImageDraw.Draw(img)

    try:
        font = ImageFont.truetype("arial.ttf", 20)
        small_font = ImageFont.truetype("arial.ttf", 16)
    except:
        font = ImageFont.load_default()
        small_font = ImageFont.load_default()

    # ==================================================
    # PAGE BORDER
    # ==================================================
    draw.rectangle(
        (20, 20, WIDTH-20, HEIGHT-20),
        outline="black",
        width=3
    )

    # ==================================================
    # GRID
    # ==================================================
    columns = ["A", "B", "C", "D", "E"]
    x_grid = [250, 650, 1050, 1450, 1850]

    for x, letter in zip(x_grid, columns):
        draw.text((x, 25), letter, fill="black", font=font)

    for i in range(1, 11):
        draw.text((25, 150+i*160), str(i), fill="black", font=font)

    # ==================================================
    # TITLE
    # ==================================================
    draw.text(
        (80, 40),
        "AUTO PANEL AI",
        fill="black",
        font=font
    )

    draw.text(
        (80, 70),
        "PLC I/O WIRING",
        fill="black",
        font=font
    )

    # ==================================================
    # 24V SMPS
    # ==================================================
    draw.rectangle((150,180,300,250), outline="black", width=2)

    draw.text(
        (180,205),
        "24V SMPS",
        fill="navy",
        font=font
    )

    # ==================================================
    # PLC CPU
    # ==================================================
    draw.rectangle((450,180,620,250), outline="black", width=2)

    draw.text(
        (495,190),
        "PLC CPU",
        fill="navy",
        font=small_font
    )

    draw.text(
        (470,215),
        "S7-1200",
        fill="black",
        font=small_font
    )

    # ==================================================
    # DI MODULE
    # ==================================================
    draw.rectangle((750,180,900,250), outline="black", width=2)

    draw.text(
        (785,205),
        "DI MODULE",
        fill="navy",
        font=small_font
    )

    # ==================================================
    # DO MODULE
    # ==================================================
    draw.rectangle((1030,180,1180,250), outline="black", width=2)

    draw.text(
        (1065,205),
        "DO MODULE",
        fill="navy",
        font=small_font
    )

    # ==================================================
    # HMI
    # ==================================================
    draw.rectangle((1350,180,1500,250), outline="black", width=2)

    draw.text(
        (1400,205),
        "HMI",
        fill="navy",
        font=font
    )

    # ==================================================
    # ETHERNET
    # ==================================================
    draw.line(
        (620,215,1350,215),
        fill="blue",
        width=3
    )

    draw.text(
        (900,180),
        "ETHERNET",
        fill="blue",
        font=font
    )

    motors = selected_components["CONTACTOR"]

    # ==================================================
    # INPUTS
    # ==================================================
    y = 450

    for i in range(1, motors+1):

        # START
        draw.text(
            (100, y),
            f"START{i}",
            fill="black",
            font=font
        )

        draw.line(
            (220, y+10, 750, y+10),
            fill="black",
            width=2
        )

        draw.text(
            (770, y),
            f"DI{2*i-2}",
            fill="green",
            font=font
        )

        y += 50

        # STOP
        draw.text(
            (100, y),
            f"STOP{i}",
            fill="black",
            font=font
        )

        draw.line(
            (220, y+10, 750, y+10),
            fill="black",
            width=2
        )

        draw.text(
            (770, y),
            f"DI{2*i-1}",
            fill="green",
            font=font
        )

        y += 80

    # ==================================================
    # OUTPUTS
    # ==================================================
    y = 450

    for i in range(1, motors+1):

        draw.text(
            (1050, y),
            f"DO{i-1}",
            fill="green",
            font=font
        )

        draw.line(
            (1120, y+10, 1450, y+10),
            fill="black",
            width=2
        )

        draw.text(
            (1480, y),
            f"KM{i}",
            fill="black",
            font=font
        )

        y += 80

    # ==================================================
    # TITLE BLOCK
    # ==================================================
    draw.rectangle(
        (1650,1780,2150,1950),
        outline="black",
        width=2
    )

    draw.text(
        (1680,1800),
        "AUTO PANEL AI",
        fill="black",
        font=font
    )

    draw.text(
        (1680,1830),
        "PLC I/O WIRING",
        fill="black",
        font=font
    )

    draw.text(
        (1680,1860),
        "415V DOL PANEL",
        fill="black",
        font=font
    )

    draw.text(
        (1680,1890),
        "Sheet : 3 / 3",
        fill="black",
        font=font
    )

    draw.text(
        (1680,1920),
        "Rev : 01",
        fill="black",
        font=font
    )

    return img