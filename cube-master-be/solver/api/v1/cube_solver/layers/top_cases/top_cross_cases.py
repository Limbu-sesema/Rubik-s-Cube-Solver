from solver.api.v1.cube_solver.layers import moves


def line(rubiks_cube):
    sequence = []
    # print("line")
    if (
        rubiks_cube["U2"] == rubiks_cube["U5"]
        and rubiks_cube["U8"] == rubiks_cube["U5"]
    ):
        sequence = ["r", "b", "u", "b'", "u'", "r'"]
    if (
        rubiks_cube["U4"] == rubiks_cube["U5"]
        and rubiks_cube["U6"] == rubiks_cube["U5"]
    ):
        sequence.extend(["f", "r", "u", "r'", "u'", "f'"])
    # print(sequence)
    for x in sequence:
        rubiks_cube = moves.execute_move(rubiks_cube, x)
        # moves.print_2d_cube(rubiks_cube)

    return sequence


def L(rubiks_cube):
    sequence = []
    # print("L")
    if (
        rubiks_cube["U2"] == rubiks_cube["U5"]
        and rubiks_cube["U4"] == rubiks_cube["U5"]
    ):
        sequence.extend(["f", "r", "u", "r'", "u'", "f'"])
    elif (
        rubiks_cube["U2"] == rubiks_cube["U5"]
        and rubiks_cube["U6"] == rubiks_cube["U5"]
    ):
        sequence.extend(["l", "f", "u", "f'", "u'", "l'"])
    elif (
        rubiks_cube["U6"] == rubiks_cube["U5"]
        and rubiks_cube["U8"] == rubiks_cube["U5"]
    ):
        sequence.extend(["b", "l", "u", "l'", "u'", "b'"])
    elif (
        rubiks_cube["U4"] == rubiks_cube["U5"]
        and rubiks_cube["U8"] == rubiks_cube["U5"]
    ):
        sequence.extend(["r", "b", "u", "b'", "u'", "r'"])
    # print(sequence)
    for x in sequence:
        rubiks_cube = moves.execute_move(rubiks_cube, x)
        # moves.print_2d_cube(rubiks_cube)

    sequence.extend(line(rubiks_cube))
    return sequence


def dot(rubiks_cube):
    # print("dot")
    sequence = []
    sequence.extend(["b", "l", "u", "l'", "u'", "b'"])
    # print(sequence)
    for x in sequence:
        rubiks_cube = moves.execute_move(rubiks_cube, x)
        # moves.print_2d_cube(rubiks_cube)
    sequence.extend(L(rubiks_cube))
    return sequence
