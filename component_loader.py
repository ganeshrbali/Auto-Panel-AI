from PIL import Image, ImageChops
import os

# -----------------------------------
# Base directory
# -----------------------------------
BASE_DIR = os.path.dirname(os.path.abspath(__file__))


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

    full_path = os.path.join(BASE_DIR, path)

    img = Image.open(full_path).convert("RGBA")

    # Remove white background
    datas = img.getdata()

    newData = []

    for item in datas:

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

    COMPONENT_FOLDER = "assets/assets/components"

    components["MCCB"] = load_component(
        f"{COMPONENT_FOLDER}/MCCB.png",
        120,
        160
    )

    components["MCB"] = load_component(
        f"{COMPONENT_FOLDER}/MCB.png",
        90,
        140
    )

    components["PLC"] = load_component(
        f"{COMPONENT_FOLDER}/PLC.png",
        180,
        140
    )

    components["SMPS"] = load_component(
        f"{COMPONENT_FOLDER}/SMPS.png",
        100,
        140
    )

    components["VAF"] = load_component(
        f"{COMPONENT_FOLDER}/VAF.png",
        120,
        140
    )

    components["VFD"] = load_component(
        f"{COMPONENT_FOLDER}/VFD.png",
        130,
        180
    )

    components["CONTACTOR"] = load_component(
        f"{COMPONENT_FOLDER}/CONTACTOR.png",
        130,
        180
    )

    components["OLR"] = load_component(
        f"{COMPONENT_FOLDER}/OLR.png",
        120,
        120
    )

    components["TB"] = load_component(
        f"{COMPONENT_FOLDER}/TB.png",
        450,
        70
    )

    components["HMI"] = load_component(
        f"{COMPONENT_FOLDER}/HMI.png",
        300,
        150
    )

    return components
