import os
import json

import base64
import numpy as np
import cv2

from django.conf import settings
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response


from scanner.api.v1.utils import get_dominant_rgb_color


class CubeStateScannerAPIView(APIView):
    def post(self, request):
        save_dir = os.path.join(settings.BASE_DIR, "decoded_images")
        os.makedirs(save_dir, exist_ok=True)

        data = json.loads(request.body)
        face = data.get("face")
        colors = []

        for idx, image_data in enumerate(face):
            if "," in image_data:
                image_data = image_data.split(",")[1]

            missing_padding = len(image_data) % 4
            if missing_padding:
                image_data += "=" * (4 - missing_padding)

            img_decoded = base64.b64decode(image_data)
            img_array = np.frombuffer(img_decoded, np.uint8)

            image = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            filename = f"decoded_image_{idx + 1}.jpg"
            save_path = os.path.join(save_dir, filename)
            cv2.imwrite(save_path, image)

            blurredFrame = cv2.blur(image, (3, 3))
            color = get_dominant_rgb_color(blurredFrame)
            colors.append(color)

        return Response(
            {"message": "Scanned Result", "colors": colors}, status=status.HTTP_200_OK
        )
