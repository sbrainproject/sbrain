from django.core.validators import MaxValueValidator, MinValueValidator
from django.contrib.auth.models import User
from django.db import models

from core.model import BaseModel


class Dedication(BaseModel):
    date = models.ForeignKey(
        'Date',
        on_delete=models.CASCADE
    )
    type = models.ForeignKey(
        'TypeDedication',
        on_delete=models.CASCADE
    )
    cycle = models.PositiveSmallIntegerField(
        default=1,
        validators=[
            MaxValueValidator(8),
            MinValueValidator(1)
        ]
    )
    time = models.PositiveSmallIntegerField(
        validators=[
            MinValueValidator(10)
        ]
    )
    comment = models.CharField(max_length=150)
