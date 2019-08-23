from django.contrib import admin
from .models import Genre, Movie, Slider, EditorsChoice, Popular

admin.site.register(Genre)
admin.site.register(Movie)
admin.site.register(Slider)
admin.site.register(Popular)
admin.site.register(EditorsChoice)
