from PIL import ImageDraw


# ==========================================
# DRAW ACTIVE SECTIONS ONLY
# ==========================================

def draw_sections(
        draw,
        active_sections,
        panel_height):

    # --------------------------------------
    # OUTER BORDER
    # --------------------------------------

    draw.rectangle(

        (
            20,
            20,
            1780,
            panel_height-20
        ),

        outline="black",

        width=5

    )

    # --------------------------------------
    # DRAW EACH ACTIVE SECTION
    # --------------------------------------

    for y in active_sections:

        top = y - 60

        bottom = y + 100

        draw.rectangle(

            (
                80,
                top,
                1700,
                bottom
            ),

            outline="blue",

            width=2

        )

        # Upper cable duct

        draw.rectangle(

            (
                80,
                top - 20,
                1700,
                top - 7
            ),

            fill="lightgray"

        )


# ==========================================
# CONTACTOR / OLR SPLIT
# ==========================================

def draw_contactor_split(
        draw,
        contactor_y):

    if contactor_y is None:

        return

    draw.line(
    (
        820,
        contactor_y - 35,
        820,
        contactor_y + 45
    ),

        fill="blue",

        width=2

    )


# ==========================================
# TITLE BLOCK
# ==========================================

def draw_title_box(
        draw,
        panel_height):

    draw.rectangle(

        (
            1280,
            panel_height-110,
            1700,
            panel_height-20
        ),

        outline="black",

        width=2

    )