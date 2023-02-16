# from django.shortcuts import render
# from django.http import HttpResponse, JsonResponse
# from django.shortcuts import render
# from rest_framework.decorators import api_view
# from rest_framework.response import Response
# from django.shortcuts import render
# from .apps import PredictionConfig 
# from django.shortcuts import get_object_or_404
# from rest_framework.views import APIView
# from rest_framework import generics
# from rest_framework import status
# import requests
# import numpy as np
# import pandas as pd
# import os
# import tensorflow as tf
# # Create your views here.
# class api_add(generics.ListCreateAPIView):
#     def get(self, request):
#         if request.method == 'POST':
#             image = BytesIO(requests.get(data['url']).content)
#             image = Image.open(image)
#             image = image.resize((224, 224))
#             image = np.array(image)
#             image = image / 255
#             image = image.reshape(1, 224, 224, 3)
#             prediction = PredictionConfig.model.predict(image)
#             if prediction>=0.5:
#                 result='Dog'
#             else:
#                 result='Cat'
#             return Response({'Prediction':result})
#         elif request.method == 'GET':
#             # params=request.GET.get('params')
#             response=PredictionConfig.model.predict()
#             return Response({'message':'Hello World!'})
#     # elif request.method == 'POST':
