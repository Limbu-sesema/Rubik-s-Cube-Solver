from solver.api.v1.cube_solver.layers import moves


def checkTopCorners(rubiks_cube):
    checkCorrect = False
    for x in range(4):
        # check subset
        if {rubiks_cube["F5"], rubiks_cube["U5"], rubiks_cube["L5"]} <= {
            rubiks_cube["F1"],
            rubiks_cube["U7"],
            rubiks_cube["L3"],
        }:
            rubiks_cube = moves.execute_move(rubiks_cube, "rl")
            checkCorrect = True
        else:
            checkCorrect = False
            return checkCorrect
    return checkCorrect


def findRequiredCorner(rubiks_cube):
    sequence = []
    requiredCornerExists = False
    # moves.print_2d_cube(rubiks_cube)
    for x in range(4):
        if {rubiks_cube["F5"], rubiks_cube["U5"], rubiks_cube["L5"]} <= {
            rubiks_cube["F1"],
            rubiks_cube["U7"],
            rubiks_cube["L3"],
        }:
            requiredCornerExists = True
            if x == 0:
                sequence = []
            elif x == 1:
                sequence = ["rl"]
            elif x == 2:
                sequence = ["rl", "rl"]
            elif x == 3:
                sequence = ["rr"]
            break
        else:
            rubiks_cube = moves.execute_move(rubiks_cube, "rl")
    return requiredCornerExists, sequence


def rightOrLeftNiklas(rubiks_cube):
    sequence = []
    if {rubiks_cube["F5"], rubiks_cube["R5"], rubiks_cube["U5"]} <= {
        rubiks_cube["U1"],
        rubiks_cube["B3"],
        rubiks_cube["L1"],
    }:
        sequence = ["r", "u'", "l'", "u", "r'", "u'", "l", "u"]
    else:
        sequence = ["rr", "l'", "u", "r", "u'", "l", "u", "r'", "u'"]
    return sequence
