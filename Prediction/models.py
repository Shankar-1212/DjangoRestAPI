from django.db import models

# Create your models here.
class Prediction(models.Model):
    image = models.ImageField(upload_to='images')
    result = models.CharField(max_length=10,blank=True)

    # def __str__(self):
    #     return str(self.result)
    
    # def save(self, *args, **kwargs):
    #     return super().save(*args, **kwargs)