from PIL import ImageDraw


# ==========================================
# DYNAMIC WIRE DUCTS
# ==========================================

def draw_wire_ducts(
        draw,
        active_sections):

    for y in active_sections:

        draw.rectangle(

            (
                80,
                y - 100,
                1700,
                y - 85
            ),

            fill="lightgray"

        )


# ==========================================
# DYNAMIC DIN RAILS
# ==========================================

def draw_din_rails(
        draw,
        active_sections):

    for y in active_sections:

        draw.line(

            (
                150,
                y,
                1600,
                y
            ),

            fill="gray",

            width=8

        )


# ==========================================
# VERTICAL DUCT
# ==========================================

def draw_vertical_ducts(
        draw,
        contactor_y):

    if contactor_y is None:

        return

    draw.rectangle(

        (
            800,
            contactor_y - 90,
            815,
            contactor_y + 90
        ),

        fill="lightgray"

    )


# ==========================================
# LEFT MAIN DUCT
# ==========================================

def draw_left_duct(
        draw,
        panel_height):

    draw.rectangle(

        (
            70,
            50,
            85,
            panel_height - 250
        ),

        fill="lightgray"

    )