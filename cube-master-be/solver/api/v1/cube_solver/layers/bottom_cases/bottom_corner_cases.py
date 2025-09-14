from solver.api.v1.cube_solver.layers import moves


def lefty_algorithm():
    return ["l'", "u'", "l", "u"]


def righty_algorithm():
    return ["r", "u", "r'", "u'"]


def front_top_left(rubiks_cube):
    sequence = []

    # Decide on the sequence of moves based on the condition
    if rubiks_cube["F1"] == rubiks_cube["D5"]:
        sequence = ["f", "u", "f'"]
    elif rubiks_cube["L3"] == rubiks_cube["D5"]:
        sequence = ["l'", "u'", "l"]
    else:
        for x in range(3):
            sequence.extend(["l'", "u'", "l", "u"])

    return sequence


def front_bottom_left(rubiks_cube):
    sequence = []
    rubiks_cube_copy = rubiks_cube.copy()

    # Decide on the sequence of moves based on the condition
    if rubiks_cube["D1"] == rubiks_cube["D5"]:
        sequence = []
    else:
        sequence.extend(["l'", "u'", "l", "u"])
        for move in sequence:
            rubiks_cube_copy = moves.execute_move(rubiks_cube_copy, move)
        sequence.extend(front_top_left(rubiks_cube_copy))
    return sequence


def front_top_right(rubiks_cube):
    sequence = []
    rubiks_cube_copy = rubiks_cube.copy()

    # Decide on the sequence of moves based on the condition
    sequence.append("u")
    for move in sequence:
        rubiks_cube_copy = moves.execute_move(rubiks_cube_copy, move)
    sequence.extend(front_top_left(rubiks_cube_copy))
    return sequence


def front_bottom_right(rubiks_cube):
    sequence = []
    rubiks_cube_copy = rubiks_cube.copy()

    # Decide on the sequence of moves based on the condition
    sequence.extend(["r", "u", "r'"])
    for move in sequence:
        rubiks_cube_copy = moves.execute_move(rubiks_cube_copy, move)
    sequence.extend(front_top_left(rubiks_cube_copy))
    return sequence


def right_right_top(rubiks_cube):
    sequence = []
    rubiks_cube_copy = rubiks_cube.copy()

    # Decide on the sequence of moves based on the condition
    sequence.extend(["u", "u"])
    for move in sequence:
        rubiks_cube_copy = moves.execute_move(rubiks_cube_copy, move)
    sequence.extend(front_top_left(rubiks_cube_copy))
    return sequence


def right_right_bottom(rubiks_cube):
    sequence = []
    rubiks_cube_copy = rubiks_cube.copy()

    # Decide on the sequence of moves based on the condition
    sequence.extend(["b", "u", "u", "b'"])
    for move in sequence:
        rubiks_cube_copy = moves.execute_move(rubiks_cube_copy, move)
    sequence.extend(front_top_left(rubiks_cube_copy))
    return sequence


def left_left_top(rubiks_cube):
    sequence = []
    rubiks_cube_copy = rubiks_cube.copy()

    # Decide on the sequence of moves based on the condition
    sequence.append("u'")
    for move in sequence:
        rubiks_cube_copy = moves.execute_move(rubiks_cube_copy, move)
    sequence.extend(front_top_left(rubiks_cube_copy))
    return sequence


def left_left_bottom(rubiks_cube):
    sequence = []
    rubiks_cube_copy = rubiks_cube.copy()

    # Decide on the sequence of moves based on the condition
    sequence.extend(["b'", "u'", "b"])
    for move in sequence:
        rubiks_cube_copy = moves.execute_move(rubiks_cube_copy, move)
    sequence.extend(front_top_left(rubiks_cube_copy))
    return sequence
