from rest_framework import serializers
from ..models import Prediction

class PredictionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Prediction
        fields = ('image', 'result')
    


        # response_dict = {"Prediction": prediction}
        # return Response(response_dict, status=200)
