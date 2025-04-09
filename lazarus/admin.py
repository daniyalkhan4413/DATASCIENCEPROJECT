from django.contrib import admin

from .models import User,JobPosting

admin.site.register(User)

admin.site.register(JobPosting)