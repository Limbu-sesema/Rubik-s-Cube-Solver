from solver.api.v1.cube_solver.layers.base import BaseSolverStep
from solver.api.v1.cube_solver.layers import moves
from solver.api.v1.cube_solver.layers.bottom_cases import (
    bottom_corner_cases,
    bottom_cross_cases,
)


class BottomLayerSolver(BaseSolverStep):
    """
    Solver for the bottom layer of the Rubik's Cube.
    """

    def solve(self):
        """
        Solve the bottom layer of the Rubik's Cube.
        """

        self.run_step(
            self.bottom_cross_step,
            self.bottom_cross_validator,
            "Bottom Cross",
        )

        self.run_step(
            self.bottom_corners_step,
            self.bottom_corners_validator,
            "Bottom Corners",
        )
        return self.sequence, self.cube

    def bottom_cross_step(self):
        """
        Step to solve the bottom cross.
        Returns a tuple of (moves, updated_cube).
        """
        side_pieces = [
            ["F2", "U8"],
            ["F4", "L6"],
            ["F6", "R4"],
            ["F8", "D2"],
            ["U2", "B2"],
            ["U4", "L2"],
            ["U6", "R2"],
            ["B4", "R6"],
            ["B6", "L4"],
            ["B8", "D8"],
            ["R8", "D6"],
            ["L8", "D4"],
        ]

        # moves.print_2d_cube(self.cube)

        for _ in range(4):
            if (
                self.cube["F8"] == self.cube["F5"]
                and self.cube["R8"] == self.cube["R5"]
                and self.cube["B8"] == self.cube["B5"]
                and self.cube["L8"] == self.cube["L5"]
                and self.cube["D2"] == self.cube["D5"]
                and self.cube["D4"] == self.cube["D5"]
                and self.cube["D6"] == self.cube["D5"]
                and self.cube["D8"] == self.cube["D5"]
            ):
                return self.sequence, self.cube

            required_side_pieces = self._detect_side_pieces_matching_center_color(
                self.cube, side_pieces, "D5"
            )
            # print(required_side_pieces)

            required_piece = self._find_pair_with_front_center_color(
                self.cube, required_side_pieces
            )
            # print(required_piece)

            face_moves = self._bring_piece_to_F8(self.cube, side_pieces, required_piece)
            # print(face_moves)

            for move in face_moves:
                # print(move)
                self.cube = moves.execute_move(self.cube, move)
                # moves.print_2d_cube(rubiks_cube)

            # RL
            self.cube = moves.rotateLeft(self.cube)
            # moves.print_2d_cube(self.cube)
            self.sequence.extend(face_moves + ["rl"])

        return self.sequence, self.cube

    def bottom_cross_validator(self):
        """
        Validate if the bottom cross is correctly formed.
        """
        faces = ["F", "L", "R", "B"]
        for face in faces:
            if self.cube[f"{face}5"] != self.cube[f"{face}8"]:
                return False
        if not all(self.cube["D5"] == self.cube[f"D{x}"] for x in ["2", "4", "6", "8"]):
            return False
        return True

    def bottom_corners_step(self):
        """
        Step to solve the bottom corners.
        Returns a tuple of (moves, updated_cube).
        """
        corner_pieces = [
            ["F1", "U7", "L3"],
            ["F3", "U9", "R1"],
            ["F7", "L9", "D1"],
            ["F9", "R7", "D3"],
            ["U1", "L1", "B3"],
            ["U3", "R3", "B1"],
            ["L7", "D7", "B9"],
            ["R9", "D9", "B7"],
        ]
        # moves.print_2d_cube(self.cube)

        for _ in range(4):
            if (
                self.cube["L9"] == self.cube["L5"]
                and self.cube["F7"] == self.cube["F5"]
                and self.cube["D1"] == self.cube["D5"]
                and self.cube["F9"] == self.cube["F5"]
                and self.cube["R7"] == self.cube["R5"]
                and self.cube["D3"] == self.cube["D5"]
                and self.cube["R9"] == self.cube["R5"]
                and self.cube["B7"] == self.cube["B5"]
                and self.cube["D9"] == self.cube["D5"]
                and self.cube["L7"] == self.cube["L5"]
                and self.cube["B9"] == self.cube["B5"]
                and self.cube["D7"] == self.cube["D5"]
            ):
                return self.sequence, self.cube

            required_corner_pieces = self._detect_corner_pieces_matching_center_color(
                self.cube, corner_pieces, "D5"
            )
            # print(required_corner_pieces)

            left_corner_piece = self._find_left_corner_matching_front_and_left_colors(
                self.cube,
                required_corner_pieces,
            )
            # print(left_corner_piece)

            face_moves = self._bring_piece_to_F7(
                self.cube, corner_pieces, left_corner_piece
            )
            # print(face_moves)

            for move in face_moves:
                # print(move)
                self.cube = moves.execute_move(self.cube, move)
                # moves.print_2d_cube(rubiks_cube)

            # RL
            self.cube = moves.rotateLeft(self.cube)
            # moves.print_2d_cube(self.cube)
            self.sequence.extend(face_moves + ["rl"])

        return self.sequence, self.cube

    def bottom_corners_validator(self):
        """
        Validate if the bottom corners are correctly positioned.
        """
        faces = ["F", "L", "R", "B"]
        for face in faces:
            if not all(
                self.cube[f"{face}5"] == self.cube[f"{face}{x}"]
                for x in ["7", "8", "9"]
            ):
                return False
        if not all(
            self.cube["D5"] == self.cube[f"D{x}"]
            for x in ["1", "2", "3", "4", "6", "8", "9"]
        ):
            return False
        return True

    # Below are the helper methods used in the bottom_corners_step method.
    def _bring_piece_to_F7(self, rubiks_cube, corner_pieces, moving_piece):
        """
        Determines and returns the move sequence to bring a specific corner piece to the F7 position.

        Args:
            rubiks_cube (dict): Current state of the Rubik's Cube.
            corner_pieces (list): Ordered list of known corner piece positions.
            moving_piece (list): The triplet of positions representing the corner piece to move.

        Returns:
            list: A sequence of moves to bring the given piece to F7.
        """
        if moving_piece == corner_pieces[0]:
            return bottom_corner_cases.front_top_left(rubiks_cube)
        elif moving_piece == corner_pieces[1]:
            return bottom_corner_cases.front_top_right(rubiks_cube)
        elif moving_piece == corner_pieces[2]:
            return bottom_corner_cases.front_bottom_left(rubiks_cube)
        elif moving_piece == corner_pieces[3]:
            return bottom_corner_cases.front_bottom_right(rubiks_cube)
        elif moving_piece == corner_pieces[4]:
            return bottom_corner_cases.left_left_top(rubiks_cube)
        elif moving_piece == corner_pieces[5]:
            return bottom_corner_cases.right_right_top(rubiks_cube)
        elif moving_piece == corner_pieces[6]:
            return bottom_corner_cases.left_left_bottom(rubiks_cube)
        elif moving_piece == corner_pieces[7]:
            return bottom_corner_cases.right_right_bottom(rubiks_cube)

    def _find_left_corner_matching_front_and_left_colors(
        self, cube, corner_triplets, front_center_pos="F5", left_center_pos="L5"
    ):
        """
        Find and return the corner triplet that includes both the front and left center colors.

        Args:
            cube (dict): Dictionary representing the Rubik's Cube state with positions as keys and colors as values.
            corner_triplets (list of list): List of corner triplets (each with 3 positions).
            front_center_pos (str): Position of the front center piece (default 'F5').
            left_center_pos (str): Position of the left center piece (default 'L5').

        Returns:
            list or None: The first corner triplet that includes both front and left center colors. None if not found.
        """
        front_color = cube[front_center_pos]
        left_color = cube[left_center_pos]

        for triplet in corner_triplets:
            colors = [cube[pos] for pos in triplet]
            if front_color in colors and left_color in colors:
                return triplet

        return None

    def _detect_corner_pieces_matching_center_color(
        self, cube, corner_piece_triplets, center_position
    ):
        """
        Detect and return the corner piece triplets that contain the same color as the center piece at `center_position`.

        Args:
            cube (dict): Dictionary representing the Rubik's cube state with positions as keys and colors as values.
            corner_piece_triplets (list of list): List of triplets (3 positions) representing corner pieces on the cube.
            center_position (str): The position of the center piece whose color is used as reference.

        Returns:
            list: List of corner piece triplets that include the center color.
        """
        matching_triplets = []

        center_color = cube[center_position]

        for triplet in corner_piece_triplets:
            # Check if any position in the triplet matches the center color
            if any(cube[pos] == center_color for pos in triplet):
                matching_triplets.append(triplet)

        return matching_triplets

    # Below are the helper methods used in the bottom_cross_step method.
    def _detect_side_pieces_matching_center_color(
        self, cube, side_piece_pairs, center_position
    ):
        """
        Detect and return the side piece pairs that contain the same color as the center piece at `center_position`.

        Args:
            cube (dict): Dictionary representing the Rubik's cube state with positions as keys and colors as values.
            side_piece_pairs (list of list): List of pairs of positions to check on the cube.
            center_position (str): The position of the center piece whose color is the reference.

        Returns:
            list: List of side piece pairs that include the center color.
        """
        matching_pairs = []

        center_color = cube[center_position]

        for pair in side_piece_pairs:
            # Check if any position in the pair matches the center color
            if any(cube[pos] == center_color for pos in pair):
                matching_pairs.append(pair)

        return matching_pairs

    def _find_pair_with_front_center_color(self, cube, side_piece_pairs):
        """
        Finds and returns the first side piece pair that contains a piece
        matching the front center color of the Rubik's cube.

        Args:
            rubiks_cube (dict): Cube state dictionary with positions as keys and colors as values.
            side_piece_pairs (list of lists): List of pairs of positions to check.

        Returns:
            list: The first pair containing a piece with the front center color.
                Returns an empty list if no such pair is found.
        """
        front_center_color = cube["F5"]

        for pair in side_piece_pairs:
            if any(cube[pos] == front_center_color for pos in pair):
                return pair

        return []

    def _bring_piece_to_F8(self, rubiks_cube, side_pieces, moving_piece):
        """
        Determines and returns the move sequence to bring a specific side piece to the F8 position.

        Args:
            rubiks_cube (dict): Current state of the Rubik's Cube.
            side_pieces (list): Ordered list of known side piece positions.
            moving_piece (list): The pair of positions representing the side piece to move.

        Returns:
            list: A sequence of moves to bring the given piece to F8.
        """

        if moving_piece == side_pieces[0]:
            return bottom_cross_cases.piece_on_front_top(rubiks_cube)
        elif moving_piece == side_pieces[1]:
            return bottom_cross_cases.piece_on_front_left(rubiks_cube)
        elif moving_piece == side_pieces[2]:
            return bottom_cross_cases.piece_on_front_right(rubiks_cube)
        elif moving_piece == side_pieces[3]:
            return bottom_cross_cases.piece_on_front_bottom(rubiks_cube)
        elif moving_piece == side_pieces[4]:
            return bottom_cross_cases.piece_on_back_top(rubiks_cube)
        elif moving_piece == side_pieces[5]:
            return bottom_cross_cases.piece_on_left_top(rubiks_cube)
        elif moving_piece == side_pieces[6]:
            return bottom_cross_cases.piece_on_right_top(rubiks_cube)
        elif moving_piece == side_pieces[7]:
            return bottom_cross_cases.piece_on_right_right(rubiks_cube)
        elif moving_piece == side_pieces[8]:
            return bottom_cross_cases.piece_on_left_left(rubiks_cube)
        elif moving_piece == side_pieces[9]:
            return bottom_cross_cases.piece_on_back_bottom(rubiks_cube)
        elif moving_piece == side_pieces[10]:
            return bottom_cross_cases.piece_on_right_bottom(rubiks_cube)
        elif moving_piece == side_pieces[11]:
            return bottom_cross_cases.piece_on_left_bottom(rubiks_cube)
        else:
            raise ValueError("Moving piece not found in side_pieces list.")
