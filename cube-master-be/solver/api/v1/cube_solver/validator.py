from rest_framework import serializers


class CubeStateValidator:
    CENTER_POSITIONS = ["F5", "L5", "R5", "B5", "U5", "D5"]
    FACE_NAMES = ["F", "R", "B", "L", "U", "D"]

    def __init__(self, rubiks_cube):
        self.rubiks_cube = rubiks_cube

    def validate(self):
        if not self._has_all_centers():
            raise serializers.ValidationError("Missing one or more center facelets.")
        if not self._has_unique_center_colors():
            raise serializers.ValidationError("There must be 6 distinct center colors.")
        if not self._has_nine_of_each_color():
            raise serializers.ValidationError(self.error_message)
        if not self._validate_side_pieces():
            raise serializers.ValidationError("The side (edge) pieces are incorrect.")
        if not self._validate_corner_pieces():
            raise serializers.ValidationError("The corner pieces are incorrect.")

    def _has_all_centers(self):
        return all(facelet in self.rubiks_cube for facelet in self.CENTER_POSITIONS)

    def _has_unique_center_colors(self):
        center_colors = {self.rubiks_cube[pos] for pos in self.CENTER_POSITIONS}
        return len(center_colors) == 6

    def _has_nine_of_each_color(self):
        try:
            color_count = {}
            for face in self.FACE_NAMES:
                for i in range(1, 10):
                    key = f"{face}{i}"
                    color = self.rubiks_cube[key]
                    color_count[color] = color_count.get(color, 0) + 1
        except KeyError as e:
            self.error_message = f"Missing facelet key: {str(e)}"
            return False

        wrong_colors = {
            color: count for color, count in color_count.items() if count != 9
        }
        if wrong_colors:
            self.error_message = (
                "Each color must appear exactly 9 times. Incorrect counts: "
                + ", ".join(
                    f"{color}: {count}" for color, count in wrong_colors.items()
                )
            )
            return False
        return True

    def _validate_side_pieces(self):
        try:
            needed = {
                frozenset({self.rubiks_cube["F5"], self.rubiks_cube["L5"]}),
                frozenset({self.rubiks_cube["F5"], self.rubiks_cube["R5"]}),
                frozenset({self.rubiks_cube["F5"], self.rubiks_cube["U5"]}),
                frozenset({self.rubiks_cube["F5"], self.rubiks_cube["D5"]}),
                frozenset({self.rubiks_cube["R5"], self.rubiks_cube["U5"]}),
                frozenset({self.rubiks_cube["R5"], self.rubiks_cube["D5"]}),
                frozenset({self.rubiks_cube["L5"], self.rubiks_cube["U5"]}),
                frozenset({self.rubiks_cube["L5"], self.rubiks_cube["D5"]}),
                frozenset({self.rubiks_cube["B5"], self.rubiks_cube["L5"]}),
                frozenset({self.rubiks_cube["B5"], self.rubiks_cube["R5"]}),
                frozenset({self.rubiks_cube["B5"], self.rubiks_cube["U5"]}),
                frozenset({self.rubiks_cube["B5"], self.rubiks_cube["D5"]}),
            }

            actual = {
                frozenset({self.rubiks_cube["F4"], self.rubiks_cube["L6"]}),
                frozenset({self.rubiks_cube["F6"], self.rubiks_cube["R4"]}),
                frozenset({self.rubiks_cube["F2"], self.rubiks_cube["U8"]}),
                frozenset({self.rubiks_cube["F8"], self.rubiks_cube["D2"]}),
                frozenset({self.rubiks_cube["B4"], self.rubiks_cube["R6"]}),
                frozenset({self.rubiks_cube["B6"], self.rubiks_cube["L4"]}),
                frozenset({self.rubiks_cube["B2"], self.rubiks_cube["U2"]}),
                frozenset({self.rubiks_cube["B8"], self.rubiks_cube["D8"]}),
                frozenset({self.rubiks_cube["R2"], self.rubiks_cube["U6"]}),
                frozenset({self.rubiks_cube["R8"], self.rubiks_cube["D6"]}),
                frozenset({self.rubiks_cube["L2"], self.rubiks_cube["U4"]}),
                frozenset({self.rubiks_cube["L8"], self.rubiks_cube["D4"]}),
            }

            return actual == needed
        except KeyError as e:
            raise serializers.ValidationError(
                f"Missing facelet key in side pieces: {str(e)}"
            )

    def _validate_corner_pieces(self):
        try:
            needed = {
                frozenset(
                    {
                        self.rubiks_cube["F5"],
                        self.rubiks_cube["L5"],
                        self.rubiks_cube["U5"],
                    }
                ),  # FLU
                frozenset(
                    {
                        self.rubiks_cube["F5"],
                        self.rubiks_cube["L5"],
                        self.rubiks_cube["D5"],
                    }
                ),  # FLD
                frozenset(
                    {
                        self.rubiks_cube["F5"],
                        self.rubiks_cube["R5"],
                        self.rubiks_cube["U5"],
                    }
                ),  # FRU
                frozenset(
                    {
                        self.rubiks_cube["F5"],
                        self.rubiks_cube["R5"],
                        self.rubiks_cube["D5"],
                    }
                ),  # FRD
                frozenset(
                    {
                        self.rubiks_cube["B5"],
                        self.rubiks_cube["L5"],
                        self.rubiks_cube["U5"],
                    }
                ),  # BLU
                frozenset(
                    {
                        self.rubiks_cube["B5"],
                        self.rubiks_cube["L5"],
                        self.rubiks_cube["D5"],
                    }
                ),  # BLD
                frozenset(
                    {
                        self.rubiks_cube["B5"],
                        self.rubiks_cube["R5"],
                        self.rubiks_cube["U5"],
                    }
                ),  # BRU
                frozenset(
                    {
                        self.rubiks_cube["B5"],
                        self.rubiks_cube["R5"],
                        self.rubiks_cube["D5"],
                    }
                ),  # BRD
            }

            actual = {
                frozenset(
                    {
                        self.rubiks_cube["F1"],
                        self.rubiks_cube["L3"],
                        self.rubiks_cube["U7"],
                    }
                ),  # FLU
                frozenset(
                    {
                        self.rubiks_cube["F7"],
                        self.rubiks_cube["L9"],
                        self.rubiks_cube["D1"],
                    }
                ),  # FLD
                frozenset(
                    {
                        self.rubiks_cube["F3"],
                        self.rubiks_cube["R1"],
                        self.rubiks_cube["U9"],
                    }
                ),  # FRU
                frozenset(
                    {
                        self.rubiks_cube["F9"],
                        self.rubiks_cube["R7"],
                        self.rubiks_cube["D3"],
                    }
                ),  # FRD
                frozenset(
                    {
                        self.rubiks_cube["B3"],
                        self.rubiks_cube["L1"],
                        self.rubiks_cube["U1"],
                    }
                ),  # BLU
                frozenset(
                    {
                        self.rubiks_cube["B9"],
                        self.rubiks_cube["L7"],
                        self.rubiks_cube["D7"],
                    }
                ),  # BLD
                frozenset(
                    {
                        self.rubiks_cube["B1"],
                        self.rubiks_cube["R3"],
                        self.rubiks_cube["U3"],
                    }
                ),  # BRU
                frozenset(
                    {
                        self.rubiks_cube["B7"],
                        self.rubiks_cube["R9"],
                        self.rubiks_cube["D9"],
                    }
                ),  # BRD
            }

            return actual == needed
        except KeyError as e:
            raise serializers.ValidationError(
                f"Missing facelet key in corner pieces: {str(e)}"
            )
