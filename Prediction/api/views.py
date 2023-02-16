from rest_framework import viewsets
from ..models import Prediction
from .serializers import PredictionSerializer
from Prediction.apps import PredictionConfig
from PIL import Image
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework.response import Response
import glob
import cv2
import numpy as np
import os
import tensorflow as tf


class PredictionView(APIView):
    def get(self, request, *args, **kwargs):
        queryset = Prediction.objects.all()
        serializer_class = PredictionSerializer(
            queryset, many=True, context={'request': request})
        return Response(serializer_class.data)

    def post(self, request, *args, **kwargs):
        try:
            
        #     image_file = request.FILES['image']
        #     imag_dir = 'media/images/'
        #     ext = ['*.jpg', '*.png', '*.jpeg']
        #     files = []
        #     [files.extend(glob.glob(imag_dir + '*.' + e)) for e in ext]
        #     images = [cv2.imread(file) for file in files]
        #     for img in images:
        #         img = cv2.imdecode(np.fromstring(img.read(), np.uint8), cv2.IMREAD_COLOR)
        #         images = [cv2.imread(file) for file in files]

        # #     # Read the image file using OpenCV

        # #         # Convert the image to a PIL Image object and resize it
        #         img_pil = Image.fromarray(img, 'RGB')
        #         resized_image = img_pil.resize((200, 200))
            image_dir = 'media/images/'
            ext = ['*.jpg', '*.png', '*.jpeg']
            files = []
            [files.extend(glob.glob(image_dir + e)) for e in ext]

            # Read each image file using OpenCV, process it, and make a prediction
            predictions = []
            for file in files:
                img = cv2.imread(file)

                # Convert the image to a PIL Image object and resize it
                img_pil = Image.fromarray(img, 'RGB')
                resized_image = img_pil.resize((200, 200))
                test_image =np.expand_dims(resized_image, axis=0) 


        #         # Pass the resized image to a pre-trained model for prediction
                result = PredictionConfig.model.predict(np.array(test_image))

        #     # Check the predicted result and return the prediction
                if np.argmax(result) >= 0.5:
                    prediction = "Dog"
                else:
                    prediction = "Cat"
                response_dict = {"Prediction": prediction}

                return Response(response_dict, status=200)
        except Exception as e:
            return Response({"Error": str(e)}, status=500)