from solver.api.v1.cube_solver.layers import moves
from solver.api.v1.cube_solver.layers.base import BaseSolverStep
from solver.api.v1.cube_solver.layers.second_cases import second_layer_cases


class SecondLayerSolver(BaseSolverStep):
    """
    Solver for the second layer of a Rubik's Cube.
    """

    def solve(self):
        """
        Solve the second layer of the Rubik's Cube.
        """

        self.run_step(
            self.second_layer_step, self.second_layer_validator, "Second Layer"
        )

        return self.sequence, self.cube

    def second_layer_step(self):
        """
        Step to solve the second layer.
        Returns a tuple of (moves, updated_cube).
        """

        # moves.print_2d_cube(rubiks_cube)

        for x in range(4):
            if (
                self.cube["F4"] == self.cube["F5"]
                and self.cube["F6"] == self.cube["F5"]
                and self.cube["R4"] == self.cube["R5"]
                and self.cube["R6"] == self.cube["R5"]
                and self.cube["B4"] == self.cube["B5"]
                and self.cube["B6"] == self.cube["B5"]
                and self.cube["L4"] == self.cube["L5"]
                and self.cube["L6"] == self.cube["L5"]
            ):
                return self.sequence, self.cube

            # first search top for top pieces
            top_pieces = second_layer_cases.dectect_top_pieces(self.cube)
            # print(top_pieces)

            if top_pieces:
                correct_position_moves, self.cube = (
                    second_layer_cases.top_to_correct_position(self.cube, top_pieces)
                )
                self.sequence.extend(correct_position_moves)

            # if no top pieces decide if solved or not. if not solved find the unsolved piece
            else:
                is_solved, unsolved_piece = second_layer_cases.state(self.cube)
                if is_solved == True:
                    # moves.print_2d_cube(rubiks_cube)
                    return self.sequence, self.cube
                else:
                    print(unsolved_piece)
                    bringing_moves = second_layer_cases.bring_piece_to_top(
                        self.cube, unsolved_piece
                    )
                    print(bringing_moves)
                    for move in bringing_moves:
                        self.cube = moves.execute_move(self.cube, move)
                        # moves.print_2d_cube(self.cube)
                    self.sequence.extend(bringing_moves)

                    top_pieces = second_layer_cases.dectect_top_pieces(self.cube)
                    # print(top_pieces)

                    correct_position_moves, self.cube = (
                        second_layer_cases.top_to_correct_position(
                            self.cube, top_pieces
                        )
                    )
                    self.sequence.extend(correct_position_moves)

        return self.sequence, self.cube

    def second_layer_validator(self):
        faces = ["F", "L", "R", "B"]
        for face in faces:
            if not all(
                self.cube[f"{face}5"] == self.cube[f"{face}{x}"]
                for x in ["4", "6", "7", "8", "9"]
            ):
                return False
        if not all(
            self.cube["D5"] == self.cube[f"D{x}"]
            for x in ["1", "2", "3", "4", "6", "8", "9"]
        ):
            return False
        return True

    # Below are the helper methods for the second_layer_step method.
    def _bring_piece_to_top(self, rubiks_cube, unsolved_piece):
        """
        Bring the unsolved piece to the top layer for insertion into the second layer.
        Args:
            rubiks_cube (dict): Dictionary representing the Rubik's Cube state.
            unsolved_piece (list): List containing the positions of the unsolved piece.
        Returns:
            list: Sequence of moves to bring the unsolved piece to the top layer.
        """

        if unsolved_piece == ["F4", "L6"]:
            return second_layer_cases.piece_on_frontLeft(rubiks_cube)
        elif unsolved_piece == ["F6", "R4"]:
            return second_layer_cases.piece_on_frontRight(rubiks_cube)
        elif unsolved_piece == ["B4", "R6"]:
            return second_layer_cases.piece_on_rightRight(rubiks_cube)
        elif unsolved_piece == ["B6", "L4"]:
            return second_layer_cases.piece_on_leftLeft(rubiks_cube)

    def _state(self, rubiks_cube):
        """
        Check if the second layer is solved or not.
        If not solved, return the unsolved piece.
        Args:
            rubiks_cube (dict): Dictionary representing the Rubik's Cube state.
        Returns:
            tuple: (is_solved (bool), unsolved_piece (list))
        """

        check_solve_cube = rubiks_cube.copy()
        is_solved = True
        unsolved_piece = []
        for x in range(4):
            if (
                check_solve_cube["F4"] != check_solve_cube["F5"]
                or check_solve_cube["L6"] != check_solve_cube["L5"]
            ):
                is_solved = False
                if x == 0:
                    unsolved_piece = ["F4", "L6"]
                elif x == 1:
                    unsolved_piece = ["F6", "R4"]
                elif x == 2:
                    unsolved_piece = ["B4", "R6"]
                else:
                    unsolved_piece = ["B6", "L4"]
                break
            check_solve_cube = moves.execute_move(check_solve_cube, "rl")
        return is_solved, unsolved_piece

    def _move_for_required_face(self, rubiks_cube, top_pieces):
        """
        Move the top edge pieces to the correct face color.

        Args:
            rubiks_cube (dict): Dictionary representing the Rubik's Cube state.
            top_pieces (list): List of top edge piece pairs to match with the front face

        Returns:
            list: Sequence of moves to align the top edge pieces with the front face.
        """
        sequence = []
        face_move = []
        top_move = []

        # find the color of a top piece
        for position in top_pieces[0]:  # Iterate over each position in the current pair
            if position in {"F2", "R2", "L2", "B2"}:
                color = rubiks_cube[position]

        # move to the color of the top face color
        if rubiks_cube["R5"] == color:
            face_move = ["rl"]
        elif rubiks_cube["L5"] == color:
            face_move = ["rr"]
        elif rubiks_cube["B5"] == color:
            face_move = ["rl", "rl"]
        for move in face_move:
            rubiks_cube = moves.execute_move(rubiks_cube, move)
            sequence.append(move)

        # move the top piece until it matches the front
        attempt = 0
        while (
            rubiks_cube["F2"] != rubiks_cube["F5"]
            or (
                rubiks_cube["U8"] != rubiks_cube["L5"]
                and rubiks_cube["U8"] != rubiks_cube["R5"]
            )
            and attempt < 4
        ):
            attempt += 1
            rubiks_cube = moves.execute_move(rubiks_cube, "u")
            top_move.append("u")

        if top_move == ["u", "u", "u"]:
            top_move = ["u'"]

        sequence.extend(face_move)
        sequence.extend(top_move)

        return sequence

    def _top_to_correct_position(self, rubiks_cube, top_pieces):
        """
        Move top layer edge pieces to their correct position in the second layer.

        Args:
            rubiks_cube (dict): Dictionary representing the Rubik's Cube state.
            top_pieces (list): List of top edge piece pairs to position correctly.

        Returns:
            tuple: (list of moves executed, updated cube state)
        """
        sequence = []

        # Align top pieces with their respective center face
        matching_face_moves = self._move_for_required_face(rubiks_cube, top_pieces)
        for move in matching_face_moves:
            rubiks_cube = moves.execute_move(rubiks_cube, move)
            sequence.append(move)

        # moves.print_2d_cube(rubiks_cube)

        # Insert the aligned piece into the second layer
        insertion_moves = second_layer_cases.piece_on_front_top(rubiks_cube)
        for move in insertion_moves:
            rubiks_cube = moves.execute_move(rubiks_cube, move)
            sequence.append(move)

        # moves.print_2d_cube(rubiks_cube)
        return sequence, rubiks_cube

    def _detect_top_pieces(self, rubiks_cube):
        """
        Detect and return top edge piece pairs that do NOT include white (U5 or D5 center color).

        Args:
            rubiks_cube (dict): Dictionary representing the Rubik's cube state with positions as keys and colors as values.

        Returns:
            list: List of top edge piece pairs that do not contain white pieces.
        """
        pieces_on_top = [["F2", "U8"], ["U4", "L2"], ["U6", "R2"], ["U2", "B2"]]
        top_center_colors = [rubiks_cube["U5"], rubiks_cube["D5"]]

        valid_top_pieces = []

        for pair in pieces_on_top:
            # Add pair if neither of the pieces has a white (U5 or D5) color
            if all(rubiks_cube[pos] not in top_center_colors for pos in pair):
                valid_top_pieces.append(pair)

        return valid_top_pieces
