from django.contrib import admin
from .models import Offer, Pet, UserRating, PetRating
# Register your models here.


admin.site.register(Offer)
admin.site.register(Pet)
admin.site.register(UserRating)
admin.site.register(PetRating)
