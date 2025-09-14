def F(rubiks_cube):
    # Step 1: Rotate the front face clockwise
    new_cube = rubiks_cube.copy()
    new_cube["F1"], new_cube["F2"], new_cube["F3"] = (
        rubiks_cube["F7"],
        rubiks_cube["F4"],
        rubiks_cube["F1"],
    )
    new_cube["F4"], new_cube["F5"], new_cube["F6"] = (
        rubiks_cube["F8"],
        rubiks_cube["F5"],
        rubiks_cube["F2"],
    )
    new_cube["F7"], new_cube["F8"], new_cube["F9"] = (
        rubiks_cube["F9"],
        rubiks_cube["F6"],
        rubiks_cube["F3"],
    )

    # Step 2: Update the adjacent edges
    (
        new_cube["U7"],
        new_cube["U8"],
        new_cube["U9"],
        new_cube["R1"],
        new_cube["R4"],
        new_cube["R7"],
        new_cube["D1"],
        new_cube["D2"],
        new_cube["D3"],
        new_cube["L3"],
        new_cube["L6"],
        new_cube["L9"],
    ) = (
        rubiks_cube["L9"],
        rubiks_cube["L6"],
        rubiks_cube["L3"],
        rubiks_cube["U7"],
        rubiks_cube["U8"],
        rubiks_cube["U9"],
        rubiks_cube["R7"],
        rubiks_cube["R4"],
        rubiks_cube["R1"],
        rubiks_cube["D1"],
        rubiks_cube["D2"],
        rubiks_cube["D3"],
    )

    return new_cube


def F_inv(rubiks_cube):
    new_cube = rubiks_cube.copy()
    new_cube["F1"], new_cube["F2"], new_cube["F3"] = (
        rubiks_cube["F3"],
        rubiks_cube["F6"],
        rubiks_cube["F9"],
    )
    new_cube["F4"], new_cube["F5"], new_cube["F6"] = (
        rubiks_cube["F2"],
        rubiks_cube["F5"],
        rubiks_cube["F8"],
    )
    new_cube["F7"], new_cube["F8"], new_cube["F9"] = (
        rubiks_cube["F1"],
        rubiks_cube["F4"],
        rubiks_cube["F7"],
    )

    new_cube["U7"], new_cube["U8"], new_cube["U9"] = (
        rubiks_cube["R1"],
        rubiks_cube["R4"],
        rubiks_cube["R7"],
    )
    new_cube["R1"], new_cube["R4"], new_cube["R7"] = (
        rubiks_cube["D3"],
        rubiks_cube["D2"],
        rubiks_cube["D1"],
    )
    new_cube["D1"], new_cube["D2"], new_cube["D3"] = (
        rubiks_cube["L3"],
        rubiks_cube["L6"],
        rubiks_cube["L9"],
    )
    new_cube["L3"], new_cube["L6"], new_cube["L9"] = (
        rubiks_cube["U9"],
        rubiks_cube["U8"],
        rubiks_cube["U7"],
    )

    return new_cube


def U(rubiks_cube):
    new_cube = rubiks_cube.copy()
    new_cube["U1"], new_cube["U2"], new_cube["U3"] = (
        rubiks_cube["U7"],
        rubiks_cube["U4"],
        rubiks_cube["U1"],
    )
    new_cube["U4"], new_cube["U5"], new_cube["U6"] = (
        rubiks_cube["U8"],
        rubiks_cube["U5"],
        rubiks_cube["U2"],
    )
    new_cube["U7"], new_cube["U8"], new_cube["U9"] = (
        rubiks_cube["U9"],
        rubiks_cube["U6"],
        rubiks_cube["U3"],
    )

    new_cube["F1"], new_cube["F2"], new_cube["F3"] = (
        rubiks_cube["R1"],
        rubiks_cube["R2"],
        rubiks_cube["R3"],
    )
    new_cube["R1"], new_cube["R2"], new_cube["R3"] = (
        rubiks_cube["B1"],
        rubiks_cube["B2"],
        rubiks_cube["B3"],
    )
    new_cube["B1"], new_cube["B2"], new_cube["B3"] = (
        rubiks_cube["L1"],
        rubiks_cube["L2"],
        rubiks_cube["L3"],
    )
    new_cube["L1"], new_cube["L2"], new_cube["L3"] = (
        rubiks_cube["F1"],
        rubiks_cube["F2"],
        rubiks_cube["F3"],
    )

    return new_cube


def U_inv(rubiks_cube):
    new_cube = rubiks_cube.copy()
    new_cube["U1"], new_cube["U2"], new_cube["U3"] = (
        rubiks_cube["U3"],
        rubiks_cube["U6"],
        rubiks_cube["U9"],
    )
    new_cube["U4"], new_cube["U5"], new_cube["U6"] = (
        rubiks_cube["U2"],
        rubiks_cube["U5"],
        rubiks_cube["U8"],
    )
    new_cube["U7"], new_cube["U8"], new_cube["U9"] = (
        rubiks_cube["U1"],
        rubiks_cube["U4"],
        rubiks_cube["U7"],
    )

    new_cube["F1"], new_cube["F2"], new_cube["F3"] = (
        rubiks_cube["L1"],
        rubiks_cube["L2"],
        rubiks_cube["L3"],
    )
    new_cube["L1"], new_cube["L2"], new_cube["L3"] = (
        rubiks_cube["B1"],
        rubiks_cube["B2"],
        rubiks_cube["B3"],
    )
    new_cube["B1"], new_cube["B2"], new_cube["B3"] = (
        rubiks_cube["R1"],
        rubiks_cube["R2"],
        rubiks_cube["R3"],
    )
    new_cube["R1"], new_cube["R2"], new_cube["R3"] = (
        rubiks_cube["F1"],
        rubiks_cube["F2"],
        rubiks_cube["F3"],
    )

    return new_cube


def R(rubiks_cube):
    new_cube = rubiks_cube.copy()

    # Step 1: Rotate the right face clockwise
    new_cube["R1"], new_cube["R2"], new_cube["R3"] = (
        rubiks_cube["R7"],
        rubiks_cube["R4"],
        rubiks_cube["R1"],
    )
    new_cube["R4"], new_cube["R5"], new_cube["R6"] = (
        rubiks_cube["R8"],
        rubiks_cube["R5"],
        rubiks_cube["R2"],
    )
    new_cube["R7"], new_cube["R8"], new_cube["R9"] = (
        rubiks_cube["R9"],
        rubiks_cube["R6"],
        rubiks_cube["R3"],
    )

    # Step 2: Update the adjacent edges
    new_cube["U9"], new_cube["U6"], new_cube["U3"] = (
        rubiks_cube["F9"],
        rubiks_cube["F6"],
        rubiks_cube["F3"],
    )
    new_cube["F9"], new_cube["F6"], new_cube["F3"] = (
        rubiks_cube["D9"],
        rubiks_cube["D6"],
        rubiks_cube["D3"],
    )
    new_cube["D9"], new_cube["D6"], new_cube["D3"] = (
        rubiks_cube["B1"],
        rubiks_cube["B4"],
        rubiks_cube["B7"],
    )
    new_cube["B1"], new_cube["B4"], new_cube["B7"] = (
        rubiks_cube["U9"],
        rubiks_cube["U6"],
        rubiks_cube["U3"],
    )
    return new_cube


def R_inv(rubiks_cube):
    new_cube = rubiks_cube.copy()

    # Step 1: Rotate the right face counter-clockwise
    new_cube["R1"], new_cube["R2"], new_cube["R3"] = (
        rubiks_cube["R3"],
        rubiks_cube["R6"],
        rubiks_cube["R9"],
    )
    new_cube["R4"], new_cube["R5"], new_cube["R6"] = (
        rubiks_cube["R2"],
        rubiks_cube["R5"],
        rubiks_cube["R8"],
    )
    new_cube["R7"], new_cube["R8"], new_cube["R9"] = (
        rubiks_cube["R1"],
        rubiks_cube["R4"],
        rubiks_cube["R7"],
    )

    # Step 2: Update the adjacent edges
    new_cube["F9"], new_cube["F6"], new_cube["F3"] = (
        rubiks_cube["U9"],
        rubiks_cube["U6"],
        rubiks_cube["U3"],
    )
    new_cube["U9"], new_cube["U6"], new_cube["U3"] = (
        rubiks_cube["B1"],
        rubiks_cube["B4"],
        rubiks_cube["B7"],
    )
    new_cube["B1"], new_cube["B4"], new_cube["B7"] = (
        rubiks_cube["D9"],
        rubiks_cube["D6"],
        rubiks_cube["D3"],
    )
    new_cube["D9"], new_cube["D6"], new_cube["D3"] = (
        rubiks_cube["F9"],
        rubiks_cube["F6"],
        rubiks_cube["F3"],
    )

    return new_cube


def L(rubiks_cube):
    new_cube = rubiks_cube.copy()
    new_cube["L1"], new_cube["L2"], new_cube["L3"] = (
        rubiks_cube["L7"],
        rubiks_cube["L4"],
        rubiks_cube["L1"],
    )
    new_cube["L4"], new_cube["L5"], new_cube["L6"] = (
        rubiks_cube["L8"],
        rubiks_cube["L5"],
        rubiks_cube["L2"],
    )
    new_cube["L7"], new_cube["L8"], new_cube["L9"] = (
        rubiks_cube["L9"],
        rubiks_cube["L6"],
        rubiks_cube["L3"],
    )

    (
        new_cube["U1"],
        new_cube["U4"],
        new_cube["U7"],
        new_cube["F1"],
        new_cube["F4"],
        new_cube["F7"],
        new_cube["D1"],
        new_cube["D4"],
        new_cube["D7"],
        new_cube["B3"],
        new_cube["B6"],
        new_cube["B9"],
    ) = (
        rubiks_cube["B9"],
        rubiks_cube["B6"],
        rubiks_cube["B3"],
        rubiks_cube["U1"],
        rubiks_cube["U4"],
        rubiks_cube["U7"],
        rubiks_cube["F1"],
        rubiks_cube["F4"],
        rubiks_cube["F7"],
        rubiks_cube["D7"],
        rubiks_cube["D4"],
        rubiks_cube["D1"],
    )

    return new_cube


def L_inv(rubiks_cube):
    new_cube = rubiks_cube.copy()
    new_cube["L1"], new_cube["L2"], new_cube["L3"] = (
        rubiks_cube["L3"],
        rubiks_cube["L6"],
        rubiks_cube["L9"],
    )
    new_cube["L4"], new_cube["L5"], new_cube["L6"] = (
        rubiks_cube["L2"],
        rubiks_cube["L5"],
        rubiks_cube["L8"],
    )
    new_cube["L7"], new_cube["L8"], new_cube["L9"] = (
        rubiks_cube["L1"],
        rubiks_cube["L4"],
        rubiks_cube["L7"],
    )

    (
        new_cube["U1"],
        new_cube["U4"],
        new_cube["U7"],
        new_cube["F1"],
        new_cube["F4"],
        new_cube["F7"],
        new_cube["D1"],
        new_cube["D4"],
        new_cube["D7"],
        new_cube["B3"],
        new_cube["B6"],
        new_cube["B9"],
    ) = (
        rubiks_cube["F1"],
        rubiks_cube["F4"],
        rubiks_cube["F7"],
        rubiks_cube["D1"],
        rubiks_cube["D4"],
        rubiks_cube["D7"],
        rubiks_cube["B9"],
        rubiks_cube["B6"],
        rubiks_cube["B3"],
        rubiks_cube["U7"],
        rubiks_cube["U4"],
        rubiks_cube["U1"],
    )

    return new_cube


def B(rubiks_cube):
    new_cube = rubiks_cube.copy()
    new_cube["B1"], new_cube["B2"], new_cube["B3"] = (
        rubiks_cube["B7"],
        rubiks_cube["B4"],
        rubiks_cube["B1"],
    )
    new_cube["B4"], new_cube["B5"], new_cube["B6"] = (
        rubiks_cube["B8"],
        rubiks_cube["B5"],
        rubiks_cube["B2"],
    )
    new_cube["B7"], new_cube["B8"], new_cube["B9"] = (
        rubiks_cube["B9"],
        rubiks_cube["B6"],
        rubiks_cube["B3"],
    )

    new_cube["U1"], new_cube["U2"], new_cube["U3"] = (
        rubiks_cube["R3"],
        rubiks_cube["R6"],
        rubiks_cube["R9"],
    )
    new_cube["L1"], new_cube["L4"], new_cube["L7"] = (
        rubiks_cube["U3"],
        rubiks_cube["U2"],
        rubiks_cube["U1"],
    )
    new_cube["D7"], new_cube["D8"], new_cube["D9"] = (
        rubiks_cube["L1"],
        rubiks_cube["L4"],
        rubiks_cube["L7"],
    )
    new_cube["R3"], new_cube["R6"], new_cube["R9"] = (
        rubiks_cube["D9"],
        rubiks_cube["D8"],
        rubiks_cube["D7"],
    )

    return new_cube


def B_inv(rubiks_cube):
    new_cube = rubiks_cube.copy()
    new_cube["B7"], new_cube["B4"], new_cube["B1"] = (
        rubiks_cube["B1"],
        rubiks_cube["B2"],
        rubiks_cube["B3"],
    )
    new_cube["B8"], new_cube["B5"], new_cube["B2"] = (
        rubiks_cube["B4"],
        rubiks_cube["B5"],
        rubiks_cube["B6"],
    )
    new_cube["B9"], new_cube["B6"], new_cube["B3"] = (
        rubiks_cube["B7"],
        rubiks_cube["B8"],
        rubiks_cube["B9"],
    )

    new_cube["R3"], new_cube["R6"], new_cube["R9"] = (
        rubiks_cube["U1"],
        rubiks_cube["U2"],
        rubiks_cube["U3"],
    )
    new_cube["U3"], new_cube["U2"], new_cube["U1"] = (
        rubiks_cube["L1"],
        rubiks_cube["L4"],
        rubiks_cube["L7"],
    )
    new_cube["L1"], new_cube["L4"], new_cube["L7"] = (
        rubiks_cube["D7"],
        rubiks_cube["D8"],
        rubiks_cube["D9"],
    )
    new_cube["D9"], new_cube["D8"], new_cube["D7"] = (
        rubiks_cube["R3"],
        rubiks_cube["R6"],
        rubiks_cube["R9"],
    )

    return new_cube


def D(rubiks_cube):
    new_cube = rubiks_cube.copy()
    new_cube["D1"], new_cube["D2"], new_cube["D3"] = (
        rubiks_cube["D7"],
        rubiks_cube["D4"],
        rubiks_cube["D1"],
    )
    new_cube["D4"], new_cube["D5"], new_cube["D6"] = (
        rubiks_cube["D8"],
        rubiks_cube["D5"],
        rubiks_cube["D2"],
    )
    new_cube["D7"], new_cube["D8"], new_cube["D9"] = (
        rubiks_cube["D9"],
        rubiks_cube["D6"],
        rubiks_cube["D3"],
    )

    new_cube["F7"], new_cube["F8"], new_cube["F9"] = (
        rubiks_cube["L7"],
        rubiks_cube["L8"],
        rubiks_cube["L9"],
    )
    new_cube["L7"], new_cube["L8"], new_cube["L9"] = (
        rubiks_cube["B7"],
        rubiks_cube["B8"],
        rubiks_cube["B9"],
    )
    new_cube["B7"], new_cube["B8"], new_cube["B9"] = (
        rubiks_cube["R7"],
        rubiks_cube["R8"],
        rubiks_cube["R9"],
    )
    new_cube["R7"], new_cube["R8"], new_cube["R9"] = (
        rubiks_cube["F7"],
        rubiks_cube["F8"],
        rubiks_cube["F9"],
    )

    return new_cube


def D_inv(rubiks_cube):
    new_cube = rubiks_cube.copy()
    new_cube["D7"], new_cube["D4"], new_cube["D1"] = (
        rubiks_cube["D1"],
        rubiks_cube["D2"],
        rubiks_cube["D3"],
    )
    new_cube["D8"], new_cube["D5"], new_cube["D2"] = (
        rubiks_cube["D4"],
        rubiks_cube["D5"],
        rubiks_cube["D6"],
    )
    new_cube["D9"], new_cube["D6"], new_cube["D3"] = (
        rubiks_cube["D7"],
        rubiks_cube["D8"],
        rubiks_cube["D9"],
    )

    new_cube["L7"], new_cube["L8"], new_cube["L9"] = (
        rubiks_cube["F7"],
        rubiks_cube["F8"],
        rubiks_cube["F9"],
    )
    new_cube["B7"], new_cube["B8"], new_cube["B9"] = (
        rubiks_cube["L7"],
        rubiks_cube["L8"],
        rubiks_cube["L9"],
    )
    new_cube["R7"], new_cube["R8"], new_cube["R9"] = (
        rubiks_cube["B7"],
        rubiks_cube["B8"],
        rubiks_cube["B9"],
    )
    new_cube["F7"], new_cube["F8"], new_cube["F9"] = (
        rubiks_cube["R7"],
        rubiks_cube["R8"],
        rubiks_cube["R9"],
    )

    return new_cube


def rotateRight(rubiks_cube):
    new_cube = rubiks_cube.copy()
    new_cube["F4"], new_cube["F5"], new_cube["F6"] = (
        rubiks_cube["L4"],
        rubiks_cube["L5"],
        rubiks_cube["L6"],
    )

    new_cube["L4"], new_cube["L5"], new_cube["L6"] = (
        rubiks_cube["B4"],
        rubiks_cube["B5"],
        rubiks_cube["B6"],
    )

    new_cube["B4"], new_cube["B5"], new_cube["B6"] = (
        rubiks_cube["R4"],
        rubiks_cube["R5"],
        rubiks_cube["R6"],
    )

    new_cube["R4"], new_cube["R5"], new_cube["R6"] = (
        rubiks_cube["F4"],
        rubiks_cube["F5"],
        rubiks_cube["F6"],
    )

    new_cube = U_inv(new_cube)
    new_cube = D(new_cube)
    return new_cube


def rotateLeft(rubiks_cube):
    new_cube = rubiks_cube.copy()
    new_cube["L4"], new_cube["L5"], new_cube["L6"] = (
        rubiks_cube["F4"],
        rubiks_cube["F5"],
        rubiks_cube["F6"],
    )
    new_cube["B4"], new_cube["B5"], new_cube["B6"] = (
        rubiks_cube["L4"],
        rubiks_cube["L5"],
        rubiks_cube["L6"],
    )
    new_cube["R4"], new_cube["R5"], new_cube["R6"] = (
        rubiks_cube["B4"],
        rubiks_cube["B5"],
        rubiks_cube["B6"],
    )
    new_cube["F4"], new_cube["F5"], new_cube["F6"] = (
        rubiks_cube["R4"],
        rubiks_cube["R5"],
        rubiks_cube["R6"],
    )
    new_cube = U(new_cube)
    new_cube = D_inv(new_cube)
    return new_cube


def rotateUp(rubiks_cube):
    new_cube = rubiks_cube.copy()
    new_cube["D2"], new_cube["D5"], new_cube["D8"] = (
        rubiks_cube["B8"],
        rubiks_cube["B5"],
        rubiks_cube["B2"],
    )
    new_cube["B2"], new_cube["B5"], new_cube["B8"] = (
        rubiks_cube["U8"],
        rubiks_cube["U5"],
        rubiks_cube["U2"],
    )
    new_cube["U2"], new_cube["U5"], new_cube["U8"] = (
        rubiks_cube["F2"],
        rubiks_cube["F5"],
        rubiks_cube["F8"],
    )
    new_cube["F2"], new_cube["F5"], new_cube["F8"] = (
        rubiks_cube["D2"],
        rubiks_cube["D5"],
        rubiks_cube["D8"],
    )
    new_cube = R(new_cube)
    new_cube = L_inv(new_cube)
    return new_cube


def rotateDown(rubiks_cube):
    new_cube = rubiks_cube.copy()
    new_cube["B2"], new_cube["B5"], new_cube["B8"] = (
        rubiks_cube["D8"],
        rubiks_cube["D5"],
        rubiks_cube["D2"],
    )
    new_cube["U2"], new_cube["U5"], new_cube["U8"] = (
        rubiks_cube["B8"],
        rubiks_cube["B5"],
        rubiks_cube["B2"],
    )
    new_cube["F2"], new_cube["F5"], new_cube["F8"] = (
        rubiks_cube["U2"],
        rubiks_cube["U5"],
        rubiks_cube["U8"],
    )
    new_cube["D2"], new_cube["D5"], new_cube["D8"] = (
        rubiks_cube["F2"],
        rubiks_cube["F5"],
        rubiks_cube["F8"],
    )

    new_cube = R_inv(new_cube)
    new_cube = L(new_cube)
    return new_cube


MOVE_FUNCTIONS = {
    "f": F,
    "f'": F_inv,
    "r": R,
    "r'": R_inv,
    "l": L,
    "l'": L_inv,
    "u": U,
    "u'": U_inv,
    "d": D,
    "d'": D_inv,
    "b": B,
    "b'": B_inv,
    "rr": rotateRight,
    "rl": rotateLeft,
    "ru": rotateUp,
    "rd": rotateDown,
}


def execute_move(rubiks_cube, move):
    func = MOVE_FUNCTIONS.get(move)
    if not func:
        raise ValueError(f"Invalid move: {move}")
    return func(rubiks_cube)


def print_2d_cube(cube):
    # Print the Upper face (U)
    print("       {} {} {}".format(cube["U1"], cube["U2"], cube["U3"]))
    print("       {} {} {}".format(cube["U4"], cube["U5"], cube["U6"]))
    print("       {} {} {}".format(cube["U7"], cube["U8"], cube["U9"]))

    # Print the Left (L), Front (F), Right (R), and Back (B) faces in a row
    print(
        "{} {} {}  {} {} {}  {} {} {}  {} {} {}".format(
            cube["L1"],
            cube["L2"],
            cube["L3"],  # Left face
            cube["F1"],
            cube["F2"],
            cube["F3"],  # Front face
            cube["R1"],
            cube["R2"],
            cube["R3"],  # Right face
            cube["B1"],
            cube["B2"],
            cube["B3"],  # Back face
        )
    )
    print(
        "{} {} {}  {} {} {}  {} {} {}  {} {} {}".format(
            cube["L4"],
            cube["L5"],
            cube["L6"],  # Left face
            cube["F4"],
            cube["F5"],
            cube["F6"],  # Front face
            cube["R4"],
            cube["R5"],
            cube["R6"],  # Right face
            cube["B4"],
            cube["B5"],
            cube["B6"],  # Back face
        )
    )
    print(
        "{} {} {}  {} {} {}  {} {} {}  {} {} {}".format(
            cube["L7"],
            cube["L8"],
            cube["L9"],  # Left face
            cube["F7"],
            cube["F8"],
            cube["F9"],  # Front face
            cube["R7"],
            cube["R8"],
            cube["R9"],  # Right face
            cube["B7"],
            cube["B8"],
            cube["B9"],  # Back face
        )
    )

    # Print the Down face (D)
    print("       {} {} {}".format(cube["D1"], cube["D2"], cube["D3"]))
    print("       {} {} {}".format(cube["D4"], cube["D5"], cube["D6"]))
    print("       {} {} {}".format(cube["D7"], cube["D8"], cube["D9"]))
