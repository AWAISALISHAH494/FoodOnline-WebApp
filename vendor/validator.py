from django.core.exceptions import ValidationError
import os

def allow_only_image_validator(value):
    ext=os.path.splitext(value.name)[1]
    valid_ext=[".png",".jpg",".jpeg"]
    if not ext.lower() in valid_ext:
        raise ValidationError("Unsupported file - Allowed extensions :" + str(valid_ext))