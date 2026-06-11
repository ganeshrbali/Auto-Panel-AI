from PIL import ImageDraw


# ======================================
# GENERIC BOX
# ======================================
def draw_box(draw, x, y, w, h, text):

    draw.rectangle(
        (x, y, x+w, y+h),
        outline="black",
        width=2
    )

    draw.text(
        (x+10, y+h+5),
        text,
        fill="navy"
    )


# ======================================
# MPCB
# ======================================
def draw_mpcb(draw, x, y, name):

    draw.rectangle(
        (x, y, x+100, y+80),
        outline="black",
        width=2
    )

    # 3 poles
    draw.line((x+25, y+20, x+25, y+60), fill="black", width=2)
    draw.line((x+50, y+20, x+50, y+60), fill="black", width=2)
    draw.line((x+75, y+20, x+75, y+60), fill="black", width=2)

    # Terminal numbering
    draw.text((x-20, y+5), "1", fill="black")
    draw.text((x-20, y+30), "3", fill="black")
    draw.text((x-20, y+55), "5", fill="black")

    draw.text((x+105, y+5), "2", fill="black")
    draw.text((x+105, y+30), "4", fill="black")
    draw.text((x+105, y+55), "6", fill="black")

    draw.text(
        (x+10, y+90),
        name,
        fill="navy"
    )

    draw.text(
        (x+28, y+110),
        "20A",
        fill="black"
    )


# ======================================
# CONTACTOR KM
# ======================================
def draw_km(draw, x, y, name):

    draw.rectangle(
        (x, y, x+80, y+80),
        outline="black",
        width=2
    )

    draw.line(
        (x+20, y+20, x+60, y+60),
        fill="black",
        width=2
    )

    draw.line(
        (x+60, y+20, x+20, y+60),
        fill="black",
        width=2
    )

    # Terminal numbers
    draw.text((x-35, y+5), "1L1", fill="black")
    draw.text((x-35, y+30), "3L2", fill="black")
    draw.text((x-35, y+55), "5L3", fill="black")

    draw.text((x+85, y+5), "2T1", fill="black")
    draw.text((x+85, y+30), "4T2", fill="black")
    draw.text((x+85, y+55), "6T3", fill="black")

    draw.text(
        (x+15, y+90),
        name,
        fill="navy"
    )

    draw.text(
        (x+20, y+110),
        "80A",
        fill="black"
    )


# ======================================
# OVERLOAD RELAY
# ======================================
def draw_olr(draw, x, y, name):

    draw.rectangle(
        (x, y, x+80, y+80),
        outline="black",
        width=2
    )

    draw.arc(
        (x+20, y+20, x+60, y+60),
        start=0,
        end=180,
        fill="black",
        width=2
    )

    # Auxiliary contacts
    draw.text((x+85, y+10), "95", fill="black")
    draw.text((x+85, y+25), "96", fill="black")
    draw.text((x+85, y+45), "97", fill="black")
    draw.text((x+85, y+60), "98", fill="black")

    draw.text(
        (x+15, y+90),
        name,
        fill="navy"
    )

    draw.text(
        (x+5, y+110),
        "63-80A",
        fill="black"
    )


# ======================================
# TERMINAL BLOCK
# ======================================
def draw_terminal(draw, x, y, name):

    draw.rectangle(
        (x, y, x+60, y+60),
        outline="black",
        width=2
    )

    draw.line(
        (x+20, y, x+20, y+60),
        fill="black",
        width=2
    )

    draw.line(
        (x+40, y, x+40, y+60),
        fill="black",
        width=2
    )

    # Phase names
    draw.text((x+5, y-20), "U", fill="black")
    draw.text((x+25, y-20), "V", fill="black")
    draw.text((x+45, y-20), "W", fill="black")

    # Terminal numbers
    draw.text((x+5, y+65), "1", fill="black")
    draw.text((x+25, y+65), "2", fill="black")
    draw.text((x+45, y+65), "3", fill="black")

    draw.text(
        (x, y+85),
        name,
        fill="navy"
    )


# ======================================
# TERMINAL BLOCK OLD STYLE
# ======================================
def draw_tb(draw, x, y, name):

    draw_terminal(draw, x, y, name)


# ======================================
# MOTOR
# ======================================
def draw_motor(draw, x, y, name):

    draw.ellipse(
        (x, y, x+90, y+90),
        outline="black",
        width=2
    )

    draw.text(
        (x+33, y+18),
        "M\n3~",
        fill="black"
    )

    # Motor terminals
    draw.text((x+15, y-20), "U", fill="black")
    draw.text((x+40, y-20), "V", fill="black")
    draw.text((x+65, y-20), "W", fill="black")

    draw.text(
        (x+15, y+100),
        name,
        fill="navy"
    )

    draw.text(
        (x+10, y+120),
        "5 HP",
        fill="black"
    )

    draw.text(
        (x+5, y+140),
        "415V",
        fill="black"
    )

    draw.text(
        (x+18, y+160),
        "3~",
        fill="black"
    )


# ======================================
# FUSE
# ======================================
def draw_fuse(draw, x, y, name):

    draw.line(
        (x, y+20, x+20, y+20),
        fill="black",
        width=2
    )

    draw.rectangle(
        (x+20, y+10, x+40, y+30),
        outline="black",
        width=2
    )

    draw.line(
        (x+40, y+20, x+60, y+20),
        fill="black",
        width=2
    )

    draw.text(
        (x+5, y+40),
        name,
        fill="navy"
    )