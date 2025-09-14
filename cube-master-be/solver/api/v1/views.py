from drf_spectacular.utils import extend_schema, OpenApiExample, OpenApiTypes
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from solver.api.v1.kociemba_solver.solver import KociembaSolver
from solver.api.v1.serializers import RubiksCubeSerializer
from solver.api.v1.cube_solver.solver import RubiksCubeSolver


class CubeSolverAPIView(APIView):
    serializer_class = RubiksCubeSerializer

    @extend_schema(
        request=RubiksCubeSerializer,
        responses={200: OpenApiTypes.OBJECT},
        examples=[
            OpenApiExample(
                name="Rubik's Cube Full State Example",
                value={
                    "rubiks_cube": {
                        "F1": "B",
                        "F2": "Y",
                        "F3": "R",
                        "F4": "W",
                        "F5": "O",
                        "F6": "R",
                        "F7": "O",
                        "F8": "W",
                        "F9": "B",
                        "B1": "Y",
                        "B2": "R",
                        "B3": "W",
                        "B4": "B",
                        "B5": "R",
                        "B6": "O",
                        "B7": "R",
                        "B8": "O",
                        "B9": "G",
                        "L1": "O",
                        "L2": "G",
                        "L3": "Y",
                        "L4": "G",
                        "L5": "G",
                        "L6": "R",
                        "L7": "Y",
                        "L8": "W",
                        "L9": "W",
                        "R1": "W",
                        "R2": "B",
                        "R3": "B",
                        "R4": "Y",
                        "R5": "B",
                        "R6": "R",
                        "R7": "R",
                        "R8": "B",
                        "R9": "G",
                        "U1": "G",
                        "U2": "G",
                        "U3": "O",
                        "U4": "Y",
                        "U5": "Y",
                        "U6": "Y",
                        "U7": "R",
                        "U8": "O",
                        "U9": "G",
                        "D1": "B",
                        "D2": "B",
                        "D3": "W",
                        "D4": "G",
                        "D5": "W",
                        "D6": "O",
                        "D7": "O",
                        "D8": "W",
                        "D9": "Y",
                    }
                },
                request_only=True,
                description="A complete scrambled cube using facelet notation and color codes (W, Y, R, O, B, G).",
            )
        ],
        description="Submit a full Rubik's Cube state. Input should include all 54 facelets labeled as 'F1'–'D9' with color codes.",
        operation_id="submit_rubiks_cube_state",
        tags=["Rubik's Cube"],
    )
    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)

        rubiks_cube = serializer.validated_data["rubiks_cube"]

        # Solve the rubik's cube
        solver = RubiksCubeSolver(rubiks_cube)
        sequence, sequence_cube = solver.solve()

        return Response(
            {
                "message": "Solved Rubik's Cube successfully.",
                "sequence": sequence,
            },
            status=status.HTTP_200_OK,
        )


class KociembaCubeSolverAPIView(APIView):
    serializer_class = RubiksCubeSerializer

    @extend_schema(
        request=RubiksCubeSerializer,
        responses={200: OpenApiTypes.OBJECT},
        examples=[
            OpenApiExample(
                name="Rubik's Cube Full State Example",
                value={
                    "rubiks_cube": {
                        "F1": "B",
                        "F2": "Y",
                        "F3": "R",
                        "F4": "W",
                        "F5": "O",
                        "F6": "R",
                        "F7": "O",
                        "F8": "W",
                        "F9": "B",
                        "B1": "Y",
                        "B2": "R",
                        "B3": "W",
                        "B4": "B",
                        "B5": "R",
                        "B6": "O",
                        "B7": "R",
                        "B8": "O",
                        "B9": "G",
                        "L1": "O",
                        "L2": "G",
                        "L3": "Y",
                        "L4": "G",
                        "L5": "G",
                        "L6": "R",
                        "L7": "Y",
                        "L8": "W",
                        "L9": "W",
                        "R1": "W",
                        "R2": "B",
                        "R3": "B",
                        "R4": "Y",
                        "R5": "B",
                        "R6": "R",
                        "R7": "R",
                        "R8": "B",
                        "R9": "G",
                        "U1": "G",
                        "U2": "G",
                        "U3": "O",
                        "U4": "Y",
                        "U5": "Y",
                        "U6": "Y",
                        "U7": "R",
                        "U8": "O",
                        "U9": "G",
                        "D1": "B",
                        "D2": "B",
                        "D3": "W",
                        "D4": "G",
                        "D5": "W",
                        "D6": "O",
                        "D7": "O",
                        "D8": "W",
                        "D9": "Y",
                    }
                },
                request_only=True,
                description="A complete scrambled cube using facelet notation and color codes (W, Y, R, O, B, G).",
            )
        ],
        description="Submit a full Rubik's Cube state. Input should include all 54 facelets labeled as 'F1'–'D9' with color codes.",
        operation_id="submit_rubiks_cube_state_kociemba",
        tags=["Rubik's Cube"],
    )
    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)

        rubiks_cube = serializer.validated_data["rubiks_cube"]

        # Solve the rubik's cube using Kociemba's algorithm
        solver = KociembaSolver(rubiks_cube)
        sequence, is_solved, error = solver.solve()

        return Response(
            {
                "message": "Solved Rubik's Cube successfully using Kociemba's algorithm.",
                "sequence": sequence,
            },
            status=status.HTTP_200_OK,
        )
