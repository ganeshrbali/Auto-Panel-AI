from PIL import Image, ImageDraw, ImageFont


def generate_control_page(selected_components):

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

    # =====================================
    # BORDER
    # =====================================

    draw.rectangle((20, 20, WIDTH-20, HEIGHT-20),
                   outline="black", width=3)

    # =====================================
    # COLUMN MARKINGS
    # =====================================

    columns = ["A", "B", "C", "D", "E"]

    x_grid = [250, 650, 1050, 1450, 1850]

    for x, letter in zip(x_grid, columns):
        draw.text((x, 25), letter, fill="black", font=font)

    # =====================================
    # TITLE
    # =====================================

    draw.text((80, 40), "AUTO PANEL AI", fill="black", font=font)
    draw.text((80, 70), "CONTROL CIRCUIT", fill="black", font=font)
    draw.text((80, 100), "230 VAC CONTROL", fill="black", font=small_font)

    # =====================================
    # L and N rails
    # =====================================

    draw.line((100, 120, 100, 1800), fill="red", width=3)
    draw.line((2000, 120, 2000, 1800), fill="blue", width=3)

    draw.text((80, 95), "L", fill="red", font=font)
    draw.text((1980, 95), "N", fill="blue", font=font)

    motors = selected_components["CONTACTOR"]

    y = 220

    for i in range(1, motors + 1):

        draw.text((40, y-10), str(i), fill="black", font=font)

        draw.line((100, y, 2000, y), fill="black", width=2)

        # =====================================
        # Wire Numbers
        # =====================================

        draw.text((150, y-40), f"{i:03}", fill="green", font=small_font)
        draw.text((380, y-40), f"{100+i}", fill="green", font=small_font)
        draw.text((930, y-40), f"{200+i}", fill="green", font=small_font)
        draw.text((1450, y-40), f"{300+i}", fill="green", font=small_font)

        # =====================================
        # STOP PB NC
        # =====================================

        x_stop = 250

        draw.line((x_stop, y-25, x_stop, y+25), fill="black", width=2)
        draw.line((x_stop+40, y-25, x_stop+40, y+25), fill="black", width=2)
        draw.line((x_stop+5, y+20, x_stop+35, y-20), fill="black", width=2)

        draw.text((240, y+35), f"STOP{i}", fill="navy", font=small_font)

        # =====================================
        # START PB NO
        # =====================================

        x_start = 450

        draw.line((x_start, y-25, x_start, y+25), fill="black", width=2)
        draw.line((x_start+40, y-25, x_start+40, y+25), fill="black", width=2)

        draw.text((440, y+35), f"START{i}", fill="navy", font=small_font)

        # =====================================
        # HOLDING CONTACT
        # =====================================

        draw.line((600, y-70, 950, y-70), fill="black", width=2)
        draw.line((600, y-70, 600, y), fill="black", width=2)
        draw.line((950, y-70, 950, y), fill="black", width=2)

        draw.line((820, y-95, 820, y-45), fill="black", width=2)
        draw.line((860, y-95, 860, y-45), fill="black", width=2)

        draw.text((760, y-120),
                  f"KM{i} AUX",
                  fill="purple",
                  font=small_font)

        draw.text((815, y-135), "13", fill="black", font=small_font)
        draw.text((855, y-135), "14", fill="black", font=small_font)

        draw.text((760, y-155),
                  f"Ref P2-R{i}",
                  fill="purple",
                  font=small_font)

        # =====================================
        # OLR NC
        # =====================================

        x_fr = 1050

        draw.line((x_fr, y-25, x_fr, y+25), fill="black", width=2)
        draw.line((x_fr+40, y-25, x_fr+40, y+25), fill="black", width=2)
        draw.line((x_fr+5, y+20, x_fr+35, y-20), fill="black", width=2)

        draw.text((1040, y+35), f"FR{i}", fill="navy", font=small_font)

        draw.text((1100, y-10), "95", fill="black", font=small_font)
        draw.text((1100, y+10), "96", fill="black", font=small_font)

        # =====================================
        # KM Coil
        # =====================================

        coil_x = 1300

        draw.text((1270, y-45), "A1", fill="black", font=small_font)
        draw.text((1375, y-45), "A2", fill="black", font=small_font)

        draw.ellipse((coil_x, y-30, coil_x+70, y+30),
                     outline="black", width=2)

        draw.text((1310, y-8),
                  f"KM{i}",
                  fill="black",
                  font=small_font)

        draw.text((1410, y-5),
                  f"PLC DO{i-1}",
                  fill="green",
                  font=small_font)

        y += 140

    # =====================================
    # TITLE BLOCK
    # =====================================

    draw.rectangle(
        (1650, 1780, 2150, 1950),
        outline="black",
        width=2
    )

    draw.text((1680, 1800),
              "AUTO PANEL AI",
              fill="black",
              font=font)

    draw.text((1680, 1830),
              "CONTROL CIRCUIT",
              fill="black",
              font=font)

    draw.text((1680, 1860),
              "415V DOL PANEL",
              fill="black",
              font=font)

    draw.text((1680, 1890),
              "Sheet : 2 / 3",
              fill="black",
              font=font)

    draw.text((1680, 1920),
              "Rev : 01",
              fill="black",
              font=font)

    return img