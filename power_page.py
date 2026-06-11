from PIL import Image, ImageDraw, ImageFont
from symbol_library import (
    draw_fuse,
    draw_mpcb,
    draw_km,
    draw_olr,
    draw_terminal,
    draw_motor
)


def generate_power_page(selected_components):

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

    draw.rectangle(
        (20,20,WIDTH-20,HEIGHT-20),
        outline="black",
        width=3
    )

    # =====================================
    # TOP GRID
    # =====================================

    columns = ["A","B","C","D","E"]
    x_grid = [250,650,1050,1450,1850]

    for x, letter in zip(x_grid, columns):
        draw.text((x,25), letter, fill="black", font=font)

    # =====================================
    # LEFT GRID
    # =====================================

    for i in range(1,11):
        draw.text((25,150+i*160), str(i), fill="black", font=font)

    # =====================================
    # TITLE
    # =====================================

    draw.text((80,40), "AUTO PANEL AI", fill="black", font=font)
    draw.text((80,70), "POWER CIRCUIT", fill="black", font=font)

    # =====================================
    # MAIN MCCB
    # =====================================

    draw.rectangle(
        (950,40,1150,100),
        outline="black",
        width=3
    )

    draw.text(
        (1020,50),
        "QF1",
        fill="blue",
        font=font
    )

    draw.text(
        (985,75),
        "MCCB 100A",
        fill="black",
        font=small_font
    )

    draw.line(
        (1050,100,1050,100),
        fill="black",
        width=3
    )

    # =====================================
    # BUSBARS
    # =====================================

    draw.line((100,100,2000,100), fill="red", width=3)
    draw.line((100,120,2000,120), fill="gold", width=3)
    draw.line((100,140,2000,140), fill="blue", width=3)

    draw.text((40,90), "L1", fill="red", font=font)
    draw.text((40,110), "L2", fill="gold", font=font)
    draw.text((40,130), "L3", fill="blue", font=font)

    motors = selected_components["CONTACTOR"]

    y = 250

    for i in range(1, motors+1):

        branch_x = 170

        # =====================================
        # DROP FROM BUSBAR
        # =====================================

        draw.line((branch_x,140,branch_x,y+60),fill="black",width=2)
        draw.line((branch_x+8,140,branch_x+8,y+60),fill="black",width=2)
        draw.line((branch_x+16,140,branch_x+16,y+60),fill="black",width=2)

        # =====================================
        # COMPONENTS
        # =====================================

        draw_fuse(draw,120,y+20,f"F{i}")

        draw_mpcb(draw,220,y,f"Q{i}")

        draw_km(draw,620,y,f"KM{i}")

        draw_olr(draw,1020,y,f"FR{i}")

        draw_terminal(draw,1320,y+10,f"XT{i}")

        draw_motor(draw,1520,y,f"M{i}")

        # =====================================
        # R PHASE
        # =====================================

        draw.line((320,y+25,620,y+25),fill="red",width=2)
        draw.line((700,y+25,1020,y+25),fill="red",width=2)
        draw.line((1100,y+25,1320,y+25),fill="red",width=2)
        draw.line((1380,y+25,1600,y+25),fill="red",width=2)

        # Y PHASE

        draw.line((320,y+40,620,y+40),fill="gold",width=2)
        draw.line((700,y+40,1020,y+40),fill="gold",width=2)
        draw.line((1100,y+40,1320,y+40),fill="gold",width=2)
        draw.line((1380,y+40,1600,y+40),fill="gold",width=2)

        # B PHASE

        draw.line((320,y+55,620,y+55),fill="blue",width=2)
        draw.line((700,y+55,1020,y+55),fill="blue",width=2)
        draw.line((1100,y+55,1320,y+55),fill="blue",width=2)
        draw.line((1380,y+55,1600,y+55),fill="blue",width=2)

        # =====================================
        # WIRE NUMBERS
        # =====================================

        base = 100 + (i-1)*10

        draw.text(
            (430,y+8),
            f"{base+1}R",
            fill="green",
            font=small_font
        )

        draw.text(
            (430,y+23),
            f"{base+2}Y",
            fill="green",
            font=small_font
        )

        draw.text(
            (430,y+38),
            f"{base+3}B",
            fill="green",
            font=small_font
        )

        # =====================================
        # CABLE ID
        # =====================================

        draw.text(
            (1305,y+95),
            f"C{i:02d}",
            fill="black",
            font=small_font
        )

        draw.text(
            (1285,y+115),
            "4C x 4sq",
            fill="black",
            font=small_font
        )

        # =====================================
        # CROSS REFERENCE
        # =====================================

        draw.text(
            (1680,y+20),
            f"(A{i})",
            fill="purple",
            font=small_font
        )

        draw.text(
            (1680,y+40),
            "Page2",
            fill="purple",
            font=small_font
        )

        # =====================================
        # EARTH
        # =====================================

        draw.line((1560,y+80,1560,y+120),fill="green",width=2)

        draw.line((1545,y+120,1575,y+120),fill="black",width=2)
        draw.line((1550,y+127,1570,y+127),fill="black",width=2)
        draw.line((1555,y+134,1565,y+134),fill="black",width=2)

        y += 170

    # =====================================
    # TITLE BLOCK
    # =====================================

    draw.rectangle(
        (1650,1780,2150,1950),
        outline="black",
        width=2
    )

    draw.text((1680,1800),"AUTO PANEL AI",fill="black",font=font)
    draw.text((1680,1830),"POWER CIRCUIT",fill="black",font=font)
    draw.text((1680,1860),"415V DOL PANEL",fill="black",font=font)
    draw.text((1680,1890),"Sheet : 1 / 3",fill="black",font=font)
    draw.text((1680,1920),"Rev : 01",fill="black",font=font)
    draw.text((1900,1920),"IEC 81346",fill="black",font=small_font)

    return img