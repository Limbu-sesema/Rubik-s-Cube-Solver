from django.urls import path

from scanner.api.v1.views import CubeStateScannerAPIView

urlpatterns = [
    path("scan/", CubeStateScannerAPIView.as_view(), name="scan-cube"),
]
