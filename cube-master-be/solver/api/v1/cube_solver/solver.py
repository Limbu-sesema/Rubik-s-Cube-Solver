from rest_framework import serializers

from solver.api.v1.cube_solver.layers import moves
from solver.api.v1.cube_solver.layers.bottom import BottomLayerSolver
from solver.api.v1.cube_solver.layers.second import SecondLayerSolver
from solver.api.v1.cube_solver.layers.top import TopLayerSolver


class RubiksCubeSolver:
    def __init__(self, rubiks_cube):
        self.rubiks_cube = rubiks_cube
        self.sequence_cube = rubiks_cube
        self.sequence = []

    def solve(self):
        self._solve_bottom_layer()
        self._solve_second_layer()
        self._solve_top_layer()

        self.sequence = self._optimize(self.sequence)

        for seq in self.sequence:
            self.sequence_cube = moves.execute_move(self.sequence_cube, seq)

        if self.sequence_cube != self.rubiks_cube:
            raise serializers.ValidationError(
                "The cube state does not match the expected solved state. Sequence Error!"
            )

        return self.sequence, self.sequence_cube

    def _solve_bottom_layer(self):
        bottom_solver = BottomLayerSolver(self.rubiks_cube)
        moves, updated_cube = bottom_solver.solve()
        self.sequence.extend(moves)
        self.rubiks_cube = updated_cube

    def _solve_second_layer(self):
        second_solver = SecondLayerSolver(self.rubiks_cube)
        moves, updated_cube = second_solver.solve()
        self.sequence.extend(moves)
        self.rubiks_cube = updated_cube

    def _solve_top_layer(self):
        top_solver = TopLayerSolver(self.rubiks_cube)
        moves, updated_cube = top_solver.solve()
        self.sequence.extend(moves)
        self.rubiks_cube = updated_cube

    def _optimize(self, sequence):
        x = 0
        while x in range(len(sequence)):
            first = sequence[x]
            if x + 1 < len(sequence):
                second = sequence[x + 1]
            else:
                second = None
            if x + 2 < len(sequence):
                third = sequence[x + 2]
            else:
                third = None
            if x + 3 < len(sequence):
                fourth = sequence[x + 3]
            else:
                fourth = None

            e4 = False
            if fourth:
                if first == second == third == fourth:
                    # print(f"remove 4 repeat at index {x}")
                    # print(first, second, third, fourth)
                    # print(sequence)
                    del sequence[x : x + 4]
                    # print(sequence)
                    x -= 1
                    e4 = True

            e3 = False
            if not e4 and third:
                if first == second == third:
                    # print(f"remove 3 repeat at index {x}")
                    # print(first, second, third)
                    # print(sequence)
                    if first.endswith("'"):
                        sequence[x : x + 3] = first[:-1]
                    else:
                        if first == "rl":
                            sequence[x : x + 3] = ["rr"]
                        elif first == "rr":
                            sequence[x : x + 3] = ["rl"]
                        else:
                            sequence[x : x + 3] = [first + "'"]
                    # print(sequence)
                    e3 = True
                    x -= 1

            if not e3 and not e4 and second:
                if (
                    first + "'" == second
                    or first == second + "'"
                    or (first == "rl" and second == "rr")
                    or (first == "rr" and second == "rl")
                ):
                    # print(f"remove two opossite at index {x}")
                    # print(first, second)
                    # print(sequence)
                    del sequence[x : x + 2]
                    # print(sequence)
                    x -= 1

            x += 1
        return sequence
