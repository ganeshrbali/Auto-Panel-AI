def assign_wire_numbers(routes):

    wire_no = 1

    for route in routes:

        route["wire"] = f"W{wire_no}"

        wire_no += 1

    return routes 