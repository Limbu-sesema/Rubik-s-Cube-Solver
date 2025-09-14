from django.urls import path

from solver.api.v1.views import CubeSolverAPIView, KociembaCubeSolverAPIView

urlpatterns = [
    path("solve/", CubeSolverAPIView.as_view(), name="solve-cube"),
    path("solve-kociemba/", KociembaCubeSolverAPIView.as_view(), name="solve-kociemba"),
]