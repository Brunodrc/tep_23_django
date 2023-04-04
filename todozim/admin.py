from django.contrib import admin
from .models import ListOfTasks, Task

# Register your models here.

admin.site.register([ListOfTasks,Task])

"""
Username: admin
Email address: admin@example.com
Password: 2023admin
"""