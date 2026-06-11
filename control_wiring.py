def generate_control_routes(selected_components):

    routes = []

    motor_count = selected_components["CONTACTOR"]

    if len(selected_components["PLC_SECTION"]) > 0:

        for i in range(1, motor_count + 1):

            routes.append({
                "from": f"DO{i}",
                "to": f"KM{i}",
                "wire_type": "CONTROL"
            })

    return routes