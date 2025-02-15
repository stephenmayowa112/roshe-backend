from django.contrib import admin
from .models import CustomUser, Mentor, Mentee, Session, Review, PlatformStats

# Register your models here
admin.site.register(CustomUser)
admin.site.register(Mentor)
admin.site.register(Mentee)
admin.site.register(Session)
admin.site.register(Review)
admin.site.register(PlatformStats)
