from django.contrib import admin

from .models import Contact,Profile,Address

admin.site.register(Profile)
admin.site.register(Contact)
admin.site.register(Address)
