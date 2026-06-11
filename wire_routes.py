def generate_wire_routes(selected_components):

    routes = []

    motors = selected_components["CONTACTOR"]

    # Power wiring
    for i in range(1, motors + 1):

        routes.append({
            "from": "MCCB",
            "to": f"KM{i}",
            "type": "POWER"
        })

        routes.append({
            "from": f"KM{i}",
            "to": f"OL{i}",
            "type": "POWER"
        })

        routes.append({
            "from": f"OL{i}",
            "to": f"TB{i}",
            "type": "POWER"
        })

        routes.append({
            "from": f"TB{i}",
            "to": f"M{i}",
            "type": "POWER"
        })

    # PLC outputs
    if len(selected_components["PLC_SECTION"]) > 0:

        for i in range(1, motors + 1):

            routes.append({
                "from": f"DO{i}",
                "to": f"KM{i}",
                "type": "CONTROL"
            })

    return routes