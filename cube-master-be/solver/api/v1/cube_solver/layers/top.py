from solver.api.v1.cube_solver.layers import moves
from solver.api.v1.cube_solver.layers.base import BaseSolverStep
from solver.api.v1.cube_solver.layers.top_cases import (
    top_cross_cases,
    top_cross_orientation_cases,
    top_corners_cases,
)


class TopLayerSolver(BaseSolverStep):
    """
    Solver for the top layer of a Rubik's Cube.
    """

    def solve(self):
        """
        Solve the top layer of the Rubik's Cube.
        """

        self.run_step(
            self.top_cross_step,
            self.top_cross_validator,
            "Top Cross",
        )

        self.run_step(
            self.top_cross_orientation_step,
            self.top_cross_orientation_validator,
            "Top Cross Orientation",
        )

        self.run_step(
            self.top_corners_step,
            self.top_corners_validator,
            "Top Corners",
        )

        self.run_step(
            self.top_corners_orientation_step,
            self.top_corners_orientation_validator,
            "Top Corners Orientation",
        )

        return self.sequence, self.cube

    def top_cross_step(self):
        """
        Step to solve the top cross.
        Returns a tuple of (moves, updated_cube).
        """

        top_cross_sequence, self.cube = self._top_cross_sequence(self.cube)
        self.sequence.extend(top_cross_sequence)

        return self.sequence, self.cube

    def top_cross_validator(self):
        """
        Validator for the top cross is correctly formed.
        """
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

        if not all(self.cube["U5"] == self.cube[f"U{x}"] for x in ["2", "4", "6", "8"]):
            return False

        return True

    def top_cross_orientation_step(self):
        """
        Step to orient the top cross.
        Returns a tuple of (moves, updated_cube).
        """
        top_cross_orientation_sequence, self.cube = (
            self._top_cross_orientation_sequence(self.cube)
        )
        self.sequence.extend(top_cross_orientation_sequence)

        return self.sequence, self.cube

    def top_cross_orientation_validator(self):
        """
        Validator for the top cross orientation is correctly formed.
        """
        faces = ["F", "L", "R", "B"]

        for face in faces:
            if not all(
                self.cube[f"{face}5"] == self.cube[f"{face}{x}"]
                for x in ["2", "4", "6", "7", "8", "9"]
            ):
                return False

        if not all(
            self.cube["D5"] == self.cube[f"D{x}"]
            for x in ["1", "2", "3", "4", "6", "8", "9"]
        ):
            return False

        if not all(self.cube["U5"] == self.cube[f"U{x}"] for x in ["2", "4", "6", "8"]):
            return False

        return True

    def top_corners_step(self):
        """
        Step to solve the top corners.
        Returns a tuple of (moves, updated_cube).
        """

        top_corners_sequence, self.cube = self._top_corners_sequence(self.cube)
        self.sequence.extend(top_corners_sequence)

        return self.sequence, self.cube

    def top_corners_validator(self):
        """
        Validator for the top corners is correctly formed.
        """
        faces = ["F", "L", "R", "B"]
        for face in faces:
            if not all(
                self.cube[f"{face}5"] == self.cube[f"{face}{x}"]
                for x in ["2", "4", "6", "7", "8", "9"]
            ):
                return False

        if not all(
            self.cube["D5"] == self.cube[f"D{x}"]
            for x in ["1", "2", "3", "4", "6", "8", "9"]
        ):
            return False

        if not all(self.cube["U5"] == self.cube[f"U{x}"] for x in ["2", "4", "6", "8"]):
            return False

        for _ in range(4):
            if {self.cube["F5"], self.cube["U5"], self.cube["L5"]} != {
                self.cube["F1"],
                self.cube["U7"],
                self.cube["L3"],
            }:
                return False
            self.cube = moves.execute_move(self.cube, "rl")
        return True

    def top_corners_orientation_step(self):
        """
        Step to solve the orientation of the top corners.
        Returns a tuple of (moves, updated_cube).
        """

        top_corners_orientation_sequence, self.cube = (
            self._top_corners_orientation_sequence(self.cube)
        )
        self.sequence.extend(top_corners_orientation_sequence)

        return self.sequence, self.cube

    def top_corners_orientation_validator(self):
        """
        Validator for the top corners orientation is correctly formed.
        """
        faces = ["F", "L", "R", "B", "U", "D"]
        for face in faces:
            if not all(
                self.cube[f"{face}5"] == self.cube[f"{face}{x}"]
                for x in ["2", "4", "6", "7", "8", "9"]
            ):
                return False
        return True

    # Below are the helper methods used by the top_corners_orientation_step method.
    def _top_corners_orientation_sequence(self, rubiks_cube):
        sequence = []
        for x in range(4):
            # check if top corners are solved
            if (
                rubiks_cube["U1"] == rubiks_cube["U5"]
                and rubiks_cube["U3"] == rubiks_cube["U5"]
                and rubiks_cube["U7"] == rubiks_cube["U5"]
                and rubiks_cube["U9"] == rubiks_cube["U5"]
            ):
                break

            cornerMatchSequence = []
            # do it until top color matches with the top center
            # print("matching top corner")
            attempt = 0
            while rubiks_cube["U3"] != rubiks_cube["U5"] and attempt < 4:
                cornerMatchSequence.extend(["r", "d", "r'", "d'"])
                for x in ["r", "d", "r'", "d'"]:
                    rubiks_cube = moves.execute_move(rubiks_cube, x)
                    # moves.print_2d_cube(rubiks_cube)
            sequence.extend(cornerMatchSequence)

            # check if top corners are solved
            if (
                rubiks_cube["U1"] == rubiks_cube["U5"]
                and rubiks_cube["U3"] == rubiks_cube["U5"]
                and rubiks_cube["U7"] == rubiks_cube["U5"]
                and rubiks_cube["U9"] == rubiks_cube["U5"]
            ):
                break

            rubiks_cube = moves.execute_move(rubiks_cube, "u")
            sequence.append("u")

        # then rotate the top do the move again
        lastOrientation = []
        # print("lastOrientation")
        testCube = rubiks_cube
        attempt = 0
        while testCube["F2"] != testCube["F5"] and attempt < 4:
            attempt += 1
            lastOrientation.append("u")
            testCube = moves.execute_move(testCube, "u")

        if lastOrientation == ["u", "u", "u"]:
            lastOrientation = ["u'"]
        # print(lastOrientation)
        for x in lastOrientation:
            rubiks_cube = moves.execute_move(rubiks_cube, x)
            # moves.print_2d_cube(rubiks_cube)

        sequence.extend(lastOrientation)

        return sequence, rubiks_cube

    # Below are the helper methods used by the top_corners_step method.
    def _top_corners_sequence(self, rubiks_cube):
        sequence = []
        # if oriented correctly returns as it is
        if top_corners_cases.checkTopCorners(rubiks_cube):
            return sequence, rubiks_cube

        # find the correct corner if it exists
        requiredCornerExists, cornerToFSequence = top_corners_cases.findRequiredCorner(
            rubiks_cube
        )
        if requiredCornerExists:
            for x in cornerToFSequence:
                rubiks_cube = moves.execute_move(rubiks_cube, x)
                # moves.print_2d_cube(rubiks_cube)
            sequence.extend(cornerToFSequence)

        # if correct corner does not exits then do a sune and go to the corrected corner
        else:
            # print("making one correct corner")
            sequence.extend(["r", "u'", "l'", "u", "r'", "u'", "l", "u"])
            for x in sequence:
                rubiks_cube = moves.execute_move(rubiks_cube, x)
                # moves.print_2d_cube(rubiks_cube)
            requiredCornerExists, cornerToFSequence = (
                top_corners_cases.findRequiredCorner(rubiks_cube)
            )
            for x in cornerToFSequence:
                rubiks_cube = moves.execute_move(rubiks_cube, x)
                # moves.print_2d_cube(rubiks_cube)
            sequence.extend(cornerToFSequence)

        # if left side move is to be done or right side move is to be done decide
        niklas = top_corners_cases.rightOrLeftNiklas(rubiks_cube)
        for x in niklas:
            rubiks_cube = moves.execute_move(rubiks_cube, x)
            # moves.print_2d_cube(rubiks_cube)
        sequence.extend(niklas)

        return sequence, rubiks_cube

    # Below are the helper methods used by the top_cross_orientation_step method.
    def _top_cross_orientation_sequence(self, rubiks_cube):
        sequence = []
        if top_cross_orientation_cases.check_correct(rubiks_cube):
            sequence.extend(
                top_cross_orientation_cases.correct_orientation(rubiks_cube)
            )
            for x in sequence:
                rubiks_cube = moves.execute_move(rubiks_cube, x)
                # moves.print_2d_cube(rubiks_cube)
            return sequence, rubiks_cube

        opossite, opossite_sequence = top_cross_orientation_cases.opossite_colors(
            rubiks_cube
        )

        if opossite:
            sequence.extend(opossite_sequence)
            for x in opossite_sequence:
                rubiks_cube = moves.execute_move(rubiks_cube, x)
                # moves.print_2d_cube(rubiks_cube)

        adjacent, adjacent_sequence = top_cross_orientation_cases.adjacent_colors(
            rubiks_cube
        )
        if adjacent:
            sequence.extend(adjacent_sequence)
            for x in adjacent_sequence:
                rubiks_cube = moves.execute_move(rubiks_cube, x)
                # moves.print_2d_cube(rubiks_cube)
        orientation_moves = top_cross_orientation_cases.correct_orientation(rubiks_cube)
        sequence.extend(orientation_moves)
        for x in orientation_moves:
            rubiks_cube = moves.execute_move(rubiks_cube, x)
            # moves.print_2d_cube(rubiks_cube)
        return sequence, rubiks_cube

    # Below are the helper methods used by the top_cross_step method.
    def _top_cross_sequence(self, rubiks_cube):
        """
        Solves the top cross on a Rubik's Cube's U (Up) face.

        Args:
            rubiks_cube (dict): The current state of the Rubik's Cube.
        Returns:
            tuple: A tuple containing the sequence of moves and the updated cube state.
        """
        sequence = []

        # moves.print_2d_cube(rubiks_cube)
        count = 0

        # Count how many edge pieces on the U face match the U center (U5)
        for pos in ["U2", "U4", "U6", "U8"]:
            if rubiks_cube[pos] == rubiks_cube["U5"]:
                count += 1

        # If already solved
        if count == 4:
            return sequence, rubiks_cube

        # If two edges are correct
        if count == 2:
            # Check if it's a line case (U2-U8 or U4-U6)
            if all(
                rubiks_cube[pos] == rubiks_cube["U5"] for pos in ["U2", "U8"]
            ) or all(rubiks_cube[pos] == rubiks_cube["U5"] for pos in ["U4", "U6"]):
                sequence = top_cross_cases.line(rubiks_cube)
            else:
                # It's an L-shape (corner) case
                sequence = top_cross_cases.L(rubiks_cube)

        # If no edges match, it's a dot case
        if count == 0:
            sequence = top_cross_cases.dot(rubiks_cube)

        # Apply each move in the sequence
        for x in sequence:
            rubiks_cube = moves.execute_move(rubiks_cube, x)

        return sequence, rubiks_cube
