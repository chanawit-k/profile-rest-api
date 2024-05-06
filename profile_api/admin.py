from django.contrib import admin

from profile_api import models

admin.site.register(models.Userprofile)
admin.site.register(models.ProfileFeedItem)