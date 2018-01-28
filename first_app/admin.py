from django.contrib import admin
from .models import Topic, AccessRecord, WebPage

admin.site.register(Topic)
admin.site.register(AccessRecord)
admin.site.register(WebPage)

