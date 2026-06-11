import streamlit as st
import math
import pandas as pd

from panel_layout import generate_panel_layout
from power_page import generate_power_page
from control_page import generate_control_page
from plc_page import generate_plc_page
from component_selector import select_components
from reportlab.platypus import SimpleDocTemplate, Spacer, Image
from reportlab.platypus import Paragraph
from reportlab.lib.styles import getSampleStyleSheet
from io import BytesIO

# ==========================================
# PAGE CONFIG
# ==========================================

st.set_page_config(
    page_title="AutoPanel AI",
    page_icon="⚡",
    layout="wide"
)

# ==========================================
# BACKGROUND
# ==========================================

st.markdown("""
<style>

/* ===========================================================
MAIN BACKGROUND
=========================================================== */

.stApp{
background: linear-gradient(135deg,#0B1120,#162033,#1E293B);
background-attachment: fixed;
}

/* ===========================================================
HEADINGS
=========================================================== */

h1{
color:white !important;
font-weight:700;
}

h2{
color:#E2E8F0 !important;
}

h3{
color:#CBD5E1 !important;
}

p,label,span{
color:#E5E7EB !important;
}

/* ===========================================================
TABS (ABB/EPLAN STYLE)
=========================================================== */

.stTabs [data-baseweb="tab-list"]{
gap:20px;
}

.stTabs [data-baseweb="tab"]{
background-color:rgba(255,255,255,0.08);
border-radius:12px;
padding:12px 20px;
color:#D1D5DB;
font-weight:600;
transition:0.3s;
}

.stTabs [aria-selected="true"]{
background:linear-gradient(90deg,#2563EB,#38BDF8);
color:white !important;
box-shadow:0px 0px 20px rgba(56,189,248,0.5);
}

/* ===========================================================
GLASSMORPHISM CARDS
=========================================================== */

div[data-testid="metric-container"]{
background:rgba(255,255,255,0.08);
backdrop-filter:blur(18px);
border:1px solid rgba(255,255,255,0.15);
padding:20px;
border-radius:20px;
box-shadow:0 8px 32px rgba(0,0,0,0.3);
}

/* ===========================================================
NUMBER INPUTS
=========================================================== */

.stNumberInput{
background:rgba(255,255,255,0.08);
border-radius:15px;
padding:10px;
backdrop-filter:blur(15px);
}

/* ===========================================================
SELECT BOX
=========================================================== */

.stSelectbox{
background:rgba(255,255,255,0.08);
border-radius:15px;
padding:10px;
backdrop-filter:blur(15px);
}

/* ===========================================================
DATAFRAME CARD
=========================================================== */

div[data-testid="stDataFrame"]{
background:rgba(255,255,255,0.95);
padding:15px;
border-radius:20px;
box-shadow:0px 8px 25px rgba(0,0,0,0.4);
}

/* ===========================================================
IMAGE CARD (POWER PAGE / PLC PAGE / PANEL LAYOUT)
=========================================================== */

[data-testid="stImage"]{
background:white;
padding:25px;
border-radius:25px;
box-shadow:
0 10px 30px rgba(0,0,0,0.35);
}

/* ===========================================================
SUCCESS BOX
=========================================================== */

.stSuccess{
background:rgba(16,185,129,0.2);
border-radius:15px;
}

/* ===========================================================
BUTTONS
=========================================================== */

.stButton>button{
background:linear-gradient(90deg,#2563EB,#38BDF8);
color:white;
border:none;
border-radius:15px;
height:50px;
font-size:16px;
font-weight:bold;
box-shadow:0px 5px 20px rgba(56,189,248,0.5);
}

.stButton>button:hover{
transform:scale(1.02);
}

/* ===========================================================
SIDEBAR
=========================================================== */

section[data-testid="stSidebar"]{
background:#111827;
}

/* ===========================================================
SCROLLBAR
=========================================================== */

::-webkit-scrollbar{
width:10px;
}

::-webkit-scrollbar-thumb{
background:#2563EB;
border-radius:10px;
}

/* ===========================================================
EXPANDERS
=========================================================== */

.streamlit-expanderHeader{
background:rgba(255,255,255,0.08);
border-radius:15px;
}

/* ===========================================================
CONTAINER EFFECT
=========================================================== */

.block-container{
padding-top:2rem;
padding-left:3rem;
padding-right:3rem;
}

</style>
""", unsafe_allow_html=True)


# ==========================================
# TITLE
# ==========================================

st.title("⚡ AutoPanel AI")

st.subheader(
    "Intelligent Control Panel Design Automation System"
)

# ==========================================
# TABS
# ==========================================

tab1,tab2,tab3,tab4,tab5,tab6,tab7 = st.tabs(
[
"⚙ Inputs",
"📦 Components",
"📐 Panel Layout",
"⚡ Power Circuit",
"🎛 Control Circuit",
"🔌 PLC I/O",
"📋 Summary"
]
)

# ==========================================
# INPUT TAB
# ==========================================

with tab1:

    col1,col2 = st.columns(2)

    with col1:

        motors = st.number_input(
            "Number of Motors",
            min_value=1,
            value=5
        )

        hp = st.number_input(
            "Motor Rating (HP)",
            min_value=1,
            value=3
        )

        starting_method = st.selectbox(
            "Motor Starting Method",
            [
                "DOL",
                "Star Delta",
                "VFD"
            ]
        )

    with col2:

        voltage = st.selectbox(
            "Supply Voltage",
            [415]
        )

        plc = st.selectbox(
            "PLC Required",
            [
                "Yes",
                "No"
            ]
        )

        hmi = st.selectbox(
            "HMI Required",
            [
                "Yes",
                "No"
            ]
        )

# ==========================================
# LOAD CALCULATIONS
# ==========================================

power_watts = motors*hp*746

power_kw = power_watts/1000

power_factor = 0.8

current = power_watts/(
    math.sqrt(3)
    *voltage
    *power_factor
)


# ==========================================
# COMPONENT SELECTION
# ==========================================

if current <= 25:

    protection = "MCB 32A"
    contactor = "25A Contactor"
    olr = "18-25A OLR"

elif current <= 50:

    protection = "MCCB 63A"
    contactor = "40A Contactor"
    olr = "30-40A OLR"

else:

    protection = "MCCB 100A"
    contactor = "80A Contactor"
    olr = "63-80A OLR"

# ==========================================
# MONITORING DEVICES
# ==========================================

monitoring_devices = []

if power_kw >= 5:
    monitoring_devices.append(
        "VAF Meter"
    )

if power_kw >= 10:
    monitoring_devices.append(
        "Energy Meter"
    )

if power_kw >= 15:

    monitoring_devices.append(
        "Digital Ammeter"
    )

    monitoring_devices.append(
        "Digital Voltmeter"
    )

if power_kw >= 25:

    monitoring_devices.append(
        "Multifunction Meter"
    )

# ==========================================
# BOM
# ==========================================

bom = []

bom.append(
{
"Component": protection,
"Quantity": 1
}
)

if plc == "Yes":

    bom.append(
    {
    "Component": "ABB AC500-eCo PLC",
    "Quantity": 1
    }
    )

if hmi == "Yes":

    bom.append(
    {
    "Component": "ABB CP600 HMI",
    "Quantity": 1
    }
    )

bom.append(
{
"Component": contactor,
"Quantity": motors
}
)

bom.append(
{
"Component": olr,
"Quantity": motors
}
)

for device in monitoring_devices:

    bom.append(
    {
    "Component": device,
    "Quantity": 1
    }
    )

bom_df = pd.DataFrame(
    bom
)

# ==========================================
# COST ESTIMATION
# ==========================================

estimated_cost = (

    motors*2500

    +15000

    +12000

    +len(
        monitoring_devices
    )*3000

)

# ==========================================
# COMPONENT TAB
# ==========================================

with tab2:

    st.header(
        "Load Calculation"
    )

    col1,col2 = st.columns(2)

    with col1:

        st.metric(
            "Connected Load (kW)",
            round(
                power_kw,
                2
            )
        )

    with col2:

        st.metric(
            "Estimated Current (A)",
            round(
                current,
                2
            )
        )

    st.markdown("---")

    st.header(
        "Recommended Components"
    )

    st.write(
        "Protection Device"
    )

    st.write(
        protection
    )

    st.write(
        "Contactor"
    )

    st.write(
        contactor
    )

    st.write(
        "Overload Relay"
    )

    st.write(
        olr
    )

    if plc=="Yes":

        st.write(
            "PLC : ABB AC500-eCo"
        )

    if hmi=="Yes":

        st.write(
            "HMI : ABB CP600"
        )

    st.markdown("---")

    st.header(
        "Monitoring Devices"
    )

    for device in monitoring_devices:

        st.write(
            "✅",
            device
        )

    st.markdown("---")

    st.header(
        "Bill of Materials"
    )

    st.dataframe(
        bom_df,
        use_container_width=True
    )

    st.markdown("---")

    st.metric(
        "Estimated Panel Cost (₹)",
        f"{estimated_cost:,}"
    )

    # ==========================================
# COMPONENT SELECTION ENGINE
# ==========================================

selected_components = select_components(
    motors=motors,
    motor_rating=hp,
    starting_method=starting_method,
    plc_required=plc,
    hmi_required=hmi
)

# ==========================================
# IMAGE GENERATION
# ==========================================

panel_image = generate_panel_layout(
    selected_components
)

power_img = generate_power_page(
    selected_components
)

control_img = generate_control_page(
    selected_components
)

plc_img = generate_plc_page(
    selected_components
)

# ==========================================
# PANEL LAYOUT TAB
# ==========================================

with tab3:

    st.header(
        "2D Panel Layout"
    )

    st.image(
        panel_image,
        caption="Auto Generated Panel Layout",
        use_container_width=True
    )

# ==========================================
# POWER CIRCUIT TAB
# ==========================================

with tab4:

    st.header(
        "Power Circuit"
    )

    st.image(
        power_img,
        use_container_width=True
    )

    # ==========================================
# CONTROL CIRCUIT TAB
# ==========================================

with tab5:

    st.header(
        "Control Circuit"
    )

    st.image(
        control_img,
        use_container_width=True
    )

# ==========================================
# PLC I/O TAB
# ==========================================

with tab6:

    st.header(
        "PLC I/O Wiring"
    )

    st.image(
        plc_img,
        use_container_width=True
    )

# ==========================================
# SUMMARY TAB
# ==========================================

with tab7:

    st.header(
        "Project Summary"
    )

    col1, col2 = st.columns(2)

    with col1:

        st.write(
            f"Number of Motors : {motors}"
        )

        st.write(
            f"Motor Rating : {hp} HP"
        )

        st.write(
            f"Starting Method : {starting_method}"
        )

        st.write(
            f"Connected Load : {round(power_kw,2)} kW"
        )

    with col2:

        st.write(
            f"Supply Voltage : {voltage} V"
        )

        st.write(
            f"PLC Required : {plc}"
        )

        st.write(
            f"HMI Required : {hmi}"
        )

        st.write(
            f"Estimated Current : {round(current,2)} A"
        )

    st.markdown("---")

    st.metric(
        "Estimated Panel Cost (₹)",
        f"{estimated_cost:,}"
    )

    st.markdown("---")

    st.success(
        "AutoPanel AI Design Generated Successfully"
    )


    st.markdown("---")
    if st.button("📄 Generate PDF"):
        panel_image.save("panel_layout.png")
        power_img.save("power_page.png")
        control_img.save("control_page.png")
        plc_img.save("plc_page.png")
        pdf = SimpleDocTemplate("AutoPanelAI_Report.pdf")
        styles = getSampleStyleSheet()
        story = []
        story.append(
        Paragraph(
            "AUTOPANEL AI REPORT",
            styles['Title']
        )
    )
        story.append(Spacer(1,20))
        story.append(
        Paragraph(
            "2D PANEL LAYOUT",
            styles['Heading2']
        )
    )
        story.append(
        Image(
            "panel_layout.png",
            width=500,
            height=350
        )
    )
        story.append(Spacer(1,20))
        story.append(
        Paragraph(
            "POWER CIRCUIT",
            styles['Heading2']
        )
    )
        story.append(
        Image(
            "power_page.png",
            width=500,
            height=350
        )
    )
        story.append(Spacer(1,20))
        story.append(
        Paragraph(
            "CONTROL CIRCUIT",
            styles['Heading2']
        )
    )
        story.append(
        Image(
            "control_page.png",
            width=500,
            height=350
        )
    )
        story.append(Spacer(1,20))
        story.append(
        Paragraph(
            "PLC I/O WIRING",
            styles['Heading2']
        )
    )
        story.append(
        Image(
            "plc_page.png",
            width=500,
            height=350
        )
    )
        pdf.build(story)
        with open("AutoPanelAI_Report.pdf","rb") as file:
            st.download_button(
            label="⬇ Download PDF",
            data=file,
            file_name="AutoPanelAI_Report.pdf",
            mime="application/pdf"
        )

