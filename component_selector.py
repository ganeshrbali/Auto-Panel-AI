def select_components(
        motors,
        motor_rating,
        starting_method,
        plc_required,
        hmi_required):

    components = {}

    # ======================================
    # Calculate approximate full load current
    # ======================================

    # 3-phase 415V assumption
    current_per_motor = (motor_rating * 746) / (1.732 * 415 * 0.85 * 0.8)

    total_current = motors * current_per_motor

    # ======================================
    # TOP SECTION
    # ======================================

    top = []

    # Main incomer protection

    if total_current <= 63:
        top.append("MCB")

    else:
        top.append("MCCB")

    # SMPS always required if PLC or HMI used
    if plc_required == "Yes" or hmi_required == "Yes":
        top.append("SMPS")

    # VAF / Multifunction meter
    if total_current >= 20:
        top.append("VAF")

    # PLC
    if plc_required == "Yes":
        top.append("PLC")

    # HMI
    if hmi_required == "Yes":
        top.append("HMI")

    components["TOP"] = top

    # ======================================
    # STARTING METHOD
    # ======================================

    if starting_method == "VFD":

        components["VFD"] = motors

        # Bypass contactor for each VFD
        components["CONTACTOR"] = motors

        components["OLR"] = 0

    elif starting_method == "DOL":

        components["VFD"] = 0

        components["CONTACTOR"] = motors

        components["OLR"] = motors

    elif starting_method == "Star Delta":

        components["VFD"] = 0

        # Main + Star + Delta
        components["CONTACTOR"] = motors * 3

        components["OLR"] = motors

    # ======================================
    # PLC SECTION
    # ======================================

    if plc_required == "Yes":

        plc_modules = []

        plc_modules.append("PLC_CPU")

        # Number of IO modules according to motors

        io_modules = max(1, (motors + 7)//8)

        for i in range(io_modules):
            plc_modules.append(f"DI_MODULE_{i+1}")

        for i in range(io_modules):
            plc_modules.append(f"DO_MODULE_{i+1}")

        components["PLC_SECTION"] = plc_modules

    else:

        components["PLC_SECTION"] = []

    # ======================================
    # TERMINAL BLOCKS
    # ======================================

    # Approximation:
    # 4 TB per motor + 10 spare terminals

    tb_groups = max(1, (motors * 4 + 10 + 9) // 10)

    components["TB"] = tb_groups

    

    # ======================================
    # RELAYS
    # ======================================

    components["RELAY"] = motors

    # ======================================
    # CONTROL MCB
    # ======================================

    components["CONTROL_MCB"] = 1

    # ======================================
    # CURRENT TRANSFORMER
    # ======================================

    if total_current >= 50:
        components["CT"] = 3
    else:
        components["CT"] = 0

    # ======================================
    # TOTAL CURRENT
    # ======================================

    components["TOTAL_CURRENT"] = round(total_current, 2)

    return components