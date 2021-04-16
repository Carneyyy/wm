from django.contrib import admin
from crossapp.models import Jldata, Jluser, Tbdata, Tbuser, Wmuser
# Register your models here.
admin.site.register([Jldata, Jluser, Tbdata, Tbuser, Wmuser])
