from django import forms
from .models import ImageUploadModel

#이미지 업로드를위한 form 클래스
class ImageUploadForm(forms.ModelForm):
    class Meta:
        model = ImageUploadModel
        fields = ("description", "document")