from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Offer(models.Model):
    localization = models.CharField(max_length=30)
    postal_code = models.CharField(max_length=6)
    active = models.BooleanField(null=True, default=True)
    pet_kind = models.CharField(max_length=5)
    contact_number = models.CharField(max_length=11)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return '{}, {}'.format(self.author, self.localization)


    class Meta:
        ordering = ('localization',)



class Pet(models.Model):
    name = models.CharField(max_length=30)
    weight = models.CharField(max_length=3)
    pet_kind = models.CharField(max_length=4)
    additional_care = models.BooleanField(null=True, default=False)
    sociability_to_human = models.CharField(max_length=30)
    sociability_to_pets = models.CharField(max_length=30)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return '{}, {}'.format(self.pet_kind, self.name)



class UserRating(models.Model):
    USER_RATING_CHOICES = [
        ('1','Best'),
        ('2','Good'),
        ('3','Could be better'),
        ('4','Bad')
    ]
    communication = models.CharField(
        max_length=2,
        choices=USER_RATING_CHOICES,
        default=None)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return '{}'.format(self.user)



class PetRating(models.Model):
    USER_RATING_CHOICES = [
        ('1','Best'),
        ('2','Good'),
        ('3','Could be better'),
        ('4','Bad')
    ]
    communication = models.CharField(
        max_length=2,
        choices=USER_RATING_CHOICES,
        default=None)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    pet = models.ForeignKey(Pet, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return '{}'.format(self.pet)
