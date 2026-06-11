# =====================================
# CONNECTION ENGINE
# =====================================

def generate_connections(selected_components):

    connections = []

    motor_count = max(
        selected_components["CONTACTOR"],
        selected_components["OLR"],
        selected_components["VFD"]
    )

    # =====================================
    # POWER CIRCUIT
    # =====================================

    power_device = "MCCB"

    if "MCB" in selected_components["TOP"]:
        power_device = "MCB"

    # DOL / STAR-DELTA
    if selected_components["CONTACTOR"] > 0:

        for i in range(motor_count):

            km = f"KM{i+1}"
            ol = f"OL{i+1}"
            motor = f"M{i+1}"

            connections.append(
                (power_device, km)
            )

            connections.append(
                (km, ol)
            )

            connections.append(
                (ol, motor)
            )

    # VFD
    elif selected_components["VFD"] > 0:

        for i in range(motor_count):

            vfd = f"VFD{i+1}"
            motor = f"M{i+1}"

            connections.append(
                (power_device, vfd)
            )

            connections.append(
                (vfd, motor)
            )

    # =====================================
    # CONTROL CIRCUIT
    # =====================================

    if "SMPS" in selected_components["TOP"]:

        connections.append(
            ("SMPS", "+24V")
        )

    if len(selected_components["PLC_SECTION"]) > 0:

        connections.append(
            ("+24V", "PLC_CPU")
        )

        connections.append(
            ("PLC_CPU", "DI_MODULE")
        )

        connections.append(
            ("PLC_CPU", "DO_MODULE")
        )

    # =====================================
    # PLC OUTPUT TO CONTACTOR COIL
    # =====================================

    if len(selected_components["PLC_SECTION"]) > 0:

        for i in range(motor_count):

            connections.append(
                (
                    f"DO{i+1}",
                    f"KM{i+1}_A1"
                )
            )

    # =====================================
    # TERMINAL BLOCKS
    # =====================================

    tb_count = selected_components["TB"]

    for i in range(tb_count):

        connections.append(
            (
                f"XT{i+1}",
                "FIELD"
            )
        )

    return connections