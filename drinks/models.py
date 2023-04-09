from django.db import models

class Breed(models.Model):
    SIZE_CHOICES = (
        ('Tiny', 'Tiny'),
        ('Small', 'Small'),
        ('Medium', 'Medium'),
        ('Large', 'Large'),
    )

    INTENSITY_CHOICES = (
        (1, 1),
        (2, 2),
        (3, 3),
        (4, 4),
        (5, 5),
    )

    name = models.CharField(max_length=255)
    size = models.CharField(max_length=255, choices=SIZE_CHOICES)
    friendliness = models.IntegerField(choices=INTENSITY_CHOICES)
    trainability = models.IntegerField(choices=INTENSITY_CHOICES)
    shedding_amount = models.IntegerField(choices=INTENSITY_CHOICES)
    exercise_needs = models.IntegerField(choices=INTENSITY_CHOICES)

    def __str__(self):
        return self.name


class Dog(models.Model):
    name = models.CharField(max_length=255)
    age = models.IntegerField()
    breed = models.ForeignKey('Breed', related_name= 'dogs', on_delete=models.CASCADE)
    gender = models.CharField(max_length=64)
    color = models.CharField(max_length=64)
    favourite_food = models.CharField(max_length=255)
    favourite_toy = models.CharField(max_length=255)

    def __str__(self):
        return self.name
    