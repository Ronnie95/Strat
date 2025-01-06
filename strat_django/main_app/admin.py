from django.contrib import admin
from . models import Objective, KeyResult, Swot, SwotItem, MindMap, Ideas
# Register your models here.

admin.site.register(Objective)
admin.site.register(KeyResult)
admin.site.register(SwotItem)
admin.site.register(Swot)
admin.site.register(MindMap)
admin.site.register(Ideas)