from rest_framework import serializers


class BaseSolverStep:
    """
    A base class for all layer solvers (bottom, middle, top).
    Provides a reusable method to apply a solving step and validate its result.
    """

    def __init__(self, cube):
        self.cube = cube
        self.sequence = []
        self.sequence_cube = cube.copy()

    def run_step(self, step_func, validate_func, step_name="Unknown Step"):
        """
        Run a solving step and validate the cube state after the step.
        Args:
            step_func (function): The function to apply to the cube. Returns (moves, updated_cube).
            validate_func (function): The function to validate the updated cube. Returns bool.
            step_name (str): A descriptive name of the step for error reporting.

        Raises:
            serializers.ValidationError: If the step or validation fails.
        """
        try:
            moves, updated_cube = step_func()
            if validate_func and not validate_func():
                raise serializers.ValidationError(f"{step_name} validation failed.")

        except Exception as e:
            raise serializers.ValidationError(f"{step_name} failed: {str(e)}")
