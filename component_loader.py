from PIL import Image, ImageChops


# -----------------------------------
# Remove white margins
# -----------------------------------
def crop_white(img):

    bg = Image.new(img.mode, img.size, (255, 255, 255, 0))

    diff = ImageChops.difference(img, bg)

    bbox = diff.getbbox()

    if bbox:
        return img.crop(bbox)

    return img


# -----------------------------------
# Load and resize image
# -----------------------------------
def load_component(path, width, height):

    img = Image.open(path).convert("RGBA")

    # Remove white background
    datas = img.getdata()

    newData = []

    for item in datas:

        # Make white pixels transparent
        if item[0] > 240 and item[1] > 240 and item[2] > 240:
            newData.append((255, 255, 255, 0))
        else:
            newData.append(item)

    img.putdata(newData)

    # Remove extra margins
    img = crop_white(img)

    # Resize while maintaining aspect ratio
    img.thumbnail((width, height))

    return img


# -----------------------------------
# Load all components
# -----------------------------------
def load_all_components():

    components = {}

    components["MCCB"] = load_component(
    "assets/components/MCCB.png",
    120,
    160
    )

    components["MCB"] = load_component(
        "assets/components/MCB.png",
        90,
        140
    )

    components["PLC"] = load_component(
        "assets/components/PLC.png",
        180,
        140
    )

    components["SMPS"] = load_component(
        "assets/components/SMPS.png",
        100,
        140
    )

    components["VAF"] = load_component(
        "assets/components/VAF.png",
        120,
        140
    )

    components["VFD"] = load_component(
        "assets/components/VFD.png",
        130,
        180
    )

    components["CONTACTOR"] = load_component(
        "assets/components/CONTACTOR.png",
        130,
        180
    )

    components["OLR"] = load_component(
        "assets/components/OLR.png",
        120,
        120
    )

    components["TB"] = load_component(
        "assets/components/TB.png",
        450,
        70
    )

    components["HMI"] = load_component(
        "assets/components/HMI.png",
        300,
        150
    )

    return components