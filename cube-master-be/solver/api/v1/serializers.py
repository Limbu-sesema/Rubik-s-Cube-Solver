from rest_framework import serializers

from solver.api.v1.cube_solver.validator import CubeStateValidator


class RubiksCubeSerializer(serializers.Serializer):
    rubiks_cube = serializers.DictField(
        child=serializers.CharField(),
        help_text="A dictionary mapping facelets like 'F1', 'R2', etc. to their colors (e.g., 'W', 'R').",
    )

    def validate(self, data):
        validator = CubeStateValidator(data["rubiks_cube"])
        validator.validate()
        return data
