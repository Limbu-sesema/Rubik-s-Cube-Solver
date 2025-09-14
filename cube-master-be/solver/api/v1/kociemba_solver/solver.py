import kociemba


class KociembaSolver:
    def __init__(self, rubiks_cube):
        self.rubiks_cube = rubiks_cube
        self.sequence = []

    def solve(self):
        # Map cube colors to Kociemba notation
        color_to_notation = {
            self.rubiks_cube["B5"]: "B",
            self.rubiks_cube["U5"]: "U",
            self.rubiks_cube["F5"]: "F",
            self.rubiks_cube["L5"]: "L",
            self.rubiks_cube["R5"]: "R",
            self.rubiks_cube["D5"]: "D",
        }

        order = ["U", "R", "F", "D", "L", "B"]
        kociemba_string = ""

        for face in order:
            for no in range(1, 10):
                position = f"{face}{no}"
                color = self.rubiks_cube[position]
                kociemba_string += color_to_notation[color]

        try:
            solution = kociemba.solve(kociemba_string)
            sequence_kociemba_format = solution.split(" ")
            self.sequence = self._transform_format(sequence_kociemba_format)
            return self.sequence, True, ""
        except Exception as e:
            return [], False, "The cube is impossible to solve."

    def _transform_format(self, moves):
        result = []
        for move in moves:
            move = move.lower()
            if "2" in move:
                move_without_2 = move.replace("2", "")
                result.extend([move_without_2] * 2)
            else:
                result.append(move)
        return result
