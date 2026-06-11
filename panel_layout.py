from PIL import Image, ImageDraw, ImageFont

from component_loader import load_all_components
from wire_duct import (
    draw_left_duct,
    draw_vertical_ducts
)
from title_duct import draw_title_duct


# ==========================================
# MOUNT COMPONENT ON DIN RAIL
# ==========================================

def mount_on_rail(
        img,
        rail_y,
        overlap=20):

    w, h = img.size

    return rail_y - h + overlap


# ==========================================
# MAIN PANEL FUNCTION
# ==========================================

def generate_panel_layout(
        selected_components):

    WIDTH = 1800

    # ==========================================
    # DYNAMIC SECTION ENGINE
    # ==========================================

    current_y = 180

    top_y = current_y

    current_y += 220

    # ----------------------------------

    if selected_components["VFD"] > 0:

        vfd_y = current_y

        current_y += 250

    else:

        vfd_y = None

            # ----------------------------------
    # CONTACTOR + OLR
    # ----------------------------------

    if (
        selected_components["CONTACTOR"] > 0
        or
        selected_components["OLR"] > 0
    ):

        contactor_y = current_y

        current_y += 260

    else:

        contactor_y = None

    # ----------------------------------
    # PLC SECTION
    # ----------------------------------

    if len(
            selected_components["PLC_SECTION"]
    ) > 0:

        plc_y = current_y

        current_y += 220

    else:

        plc_y = None

    # ----------------------------------
    # TB SECTION
    # ----------------------------------

    tb_y = current_y

    current_y += 220

    HEIGHT = current_y + 150


        # ==========================================
    # CREATE PANEL
    # ==========================================

    panel = Image.new(

        "RGB",

        (
            WIDTH,
            HEIGHT
        ),

        (
            245,
            245,
            245
        )
    )

    draw = ImageDraw.Draw(panel)

    try:

        font = ImageFont.truetype(
            "arial.ttf",
            18
        )

    except:

        font = ImageFont.load_default()

    comp = load_all_components()

    motor_count = max(

        selected_components["CONTACTOR"],

        selected_components["OLR"],

        selected_components["VFD"]

    )


        # ==========================================
    # LEFT MAIN DUCT
    # ==========================================

    draw_left_duct(

        draw,

        tb_y + 120

    )

    # ==========================================
    # ACTIVE SECTIONS
    # ==========================================

    active_sections = []

    active_sections.append(
        top_y
    )

    if vfd_y is not None:

        active_sections.append(
            vfd_y
        )

    if contactor_y is not None:

        active_sections.append(
            contactor_y
        )

    if plc_y is not None:

        active_sections.append(
            plc_y
        )

    active_sections.append(
        tb_y
    )

        # ==========================================
    # OUTER PANEL BORDER
    # ==========================================

    draw.rectangle(

        (
            20,
            20,
            1780,
            HEIGHT-20
        ),

        outline="black",

        width=5

    )

    # ==========================================
    # DRAW SECTION BORDERS
    # ==========================================

    for y in active_sections:

        draw.rectangle(

            (
                60,
                y-80,
                1700,
                y+120
            ),

            outline="blue",

            width=2

        )

        draw.rectangle(

            (
                60,
                y-95,
                1700,
                y-82
            ),

            fill="lightgray"

        )

            # ==========================================
    # DIN RAILS
    # ==========================================

    for y in active_sections:

        draw.line(

            (
                140,
                y,
                1600,
                y
            ),

            fill="gray",

            width=7

        )

    # ==========================================
    # VERTICAL DUCT
    # ==========================================

    draw_vertical_ducts(

        draw,

        contactor_y

    )

    # ==========================================
    # TITLE BLOCK
    # ==========================================

    draw_title_duct(

        draw,

        motor_count

    )


        # ==========================================
    # TOP SECTION
    # ==========================================

    rail_y = top_y

    top_devices = selected_components["TOP"]

    spacing = 250

    total_width = (len(top_devices)-1)*spacing

    start_x = (1800-total_width)//2 - 100

    for i, name in enumerate(top_devices):

        x = start_x + i*spacing

        img = comp[name]

        if name == "MCCB":

            y = mount_on_rail(
                img,
                rail_y,
                overlap= +60
            )

        elif name == "MCB":

            y = mount_on_rail(
                img,
                rail_y,
                overlap=60
            )

        else:

            y = mount_on_rail(
                img,
                rail_y,
                overlap=60
            )

        panel.paste(
            img,
            (x, y),
            img
        )

        draw.text(
            (
                x+15,
                rail_y+60
            ),
            name,
            fill="blue",
            font=font
        )

            # ==========================================
    # VFD SECTION
    # ==========================================

    if vfd_y is not None:

        rail_y = vfd_y

        vfd_count = selected_components["VFD"]

        spacing = min(
            350,
            1200//max(
                vfd_count,
                1
            )
        )

        for i in range(vfd_count):

            x = 250 + i*spacing

            img = comp["VFD"]

            y = mount_on_rail(
                img,
                rail_y,
                overlap=30
            )

            panel.paste(
                img,
                (
                    x,
                    y
                ),
                img
            )

            draw.text(
                (
                    x+10,
                    rail_y+20
                ),
                f"VFD{i+1}",
                fill="blue",
                font=font
            )

                # ==========================================
    # CONTACTOR SECTION
    # ==========================================

    if contactor_y is not None:

        rail_y = contactor_y + 80

        contactor_count = selected_components["CONTACTOR"]

        km_spacing = 55

        total_width = (contactor_count-1)*km_spacing

        start_x = (800-total_width)//2

        for i in range(contactor_count):

            x = start_x + i*km_spacing

            img = comp["CONTACTOR"]

            y = mount_on_rail(
                img,
                rail_y,
                overlap=10
            )

            panel.paste(
                img,
                (x, y),
                img
            )

            draw.text(
                (
                    x+10,
                    rail_y+15
                ),
                f"KM{i+1}",
                fill="blue",
                font=font
            )

        # -----------------------

        olr_count = selected_components["OLR"]

        olr_spacing = 45

        total_width = (olr_count-1)*olr_spacing

        start_x = 900 + ((700-total_width)//2)

        for i in range(olr_count):

            x = start_x + i*olr_spacing

            img = comp["OLR"]

            y = mount_on_rail(
                img,
                rail_y,
                overlap=-30
            )

            panel.paste(
                img,
                (
                    x,
                    y
                ),
                img
            )

            draw.text(
                (
                    x+10,
                    rail_y+15
                ),
                f"OL{i+1}",
                fill="blue",
                font=font
            )


                # ==========================================
    # PLC SECTION
    # ==========================================

    if plc_y is not None:

        rail_y = plc_y

        plc_modules = selected_components["PLC_SECTION"]

        plc_spacing = 220

        total_width = (len(plc_modules)-1)*plc_spacing

        start_x = (1800-total_width)//2 - 100

        for i, module in enumerate(plc_modules):

            x = start_x + i*plc_spacing

            img = comp["PLC"]

            y = mount_on_rail(
                img,
                rail_y,
                overlap=60
            )

            panel.paste(
                img,
                (
                    x,
                    y
                ),
                img
            )

            draw.text(
                (
                    x+5,
                    rail_y+60
                ),
                module,
                fill="blue",
                font=font
            )

    # ==========================================
    # TERMINAL BLOCK SECTION
    # ==========================================

    rail_y = tb_y

    tb = comp["TB"]

    tb_count = selected_components["TB"]

    tb_spacing = 180

    total_width = (tb_count-1)*tb_spacing

    start_x = (1800-total_width)//2 - 120

    for i in range(tb_count):

        x = start_x + i*tb_spacing

        y = mount_on_rail(
            tb,
            rail_y,
            overlap=35
        )

        panel.paste(
            tb,
            (
                x,
                y
            ),
            tb
        )

        draw.text(
            (
                x+20,
                rail_y+35
            ),
            f"XT{i*10+1}-{(i+1)*10}",
            fill="blue",
            font=font
        )

    return panel