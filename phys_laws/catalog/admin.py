from django.contrib import admin

from .models import Authors, Laws, Sections

admin.site.register(Authors)

admin.site.register(Laws)

admin.site.register(Sections)
