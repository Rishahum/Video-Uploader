from .models import Video
from .models import Timestamp
from django import forms

class Video_form(forms.ModelForm):
    class Meta:
        model=Video
        fields=("caption","video")

class TimestampForm(forms.ModelForm):
    class Meta:
        model = Timestamp
        fields = ('timestamp', 'comment')