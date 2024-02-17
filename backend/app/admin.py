from django.contrib import admin

# Register your models here.
from .models import Scenario, Header, Title

admin.site.register(Scenario)
admin.site.register(Header)
admin.site.register(Title)