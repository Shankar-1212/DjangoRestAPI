from django.apps import AppConfig
from joblib import load
import pandas as pd
import numpy as np
import os
import tensorflow as tf

class PredictionConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'Prediction'
    model = tf.keras.models.load_model(os.getcwd() + '/my_h5_model.h5') 