from django.db import models

# Create your models here.
from django.db import models
from .validators import file_size

# Create your models here.
class Video(models.Model):
    caption=models.CharField(max_length=100)
    video=models.FileField(upload_to="video/%y",validators=[file_size])
    def __str__(self):
        return self.caption
    
class Timestamp(models.Model):
    video = models.ForeignKey(Video, on_delete=models.CASCADE)
    timestamp = models.PositiveIntegerField()  # You can adjust this as needed
    comment = models.TextField()
