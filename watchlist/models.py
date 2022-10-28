from email.policy import default
from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

# Create your models here.


class StreamPlatform(models.Model):
    name = models.CharField(max_length=30)
    about = models.CharField(max_length=200)
    website = models.URLField(max_length=200)

    def __str__(self):
        return self.name


class Movie(models.Model):
    title = models.CharField(max_length=50)
    description = models.CharField(max_length=200)
    active = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    platform = models.ForeignKey(
        StreamPlatform, on_delete=models.CASCADE, related_name='movies')

    def __str__(self):
        return self.title


class Review(models.Model):
    rating = models.PositiveIntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(5)])
    desciption = models.CharField(max_length=200, null=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True)
    movie = models.ForeignKey(
        Movie, on_delete=models.CASCADE, related_name='reviews')

    def __str__(self):
        return f"{self.movie} - rating: {self.rating}"
