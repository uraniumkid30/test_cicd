from django.contrib import admin
from apps.resources import models

# Register your models here.

class CustomResources(admin.ModelAdmin): #extend the behavior of  the ModelAdmin, an inherited class 
    #the list_filter option add filters to list view
    list_display = (
        "username",
        "link",
        "get_tags",
        "description",
    )
    
    @admin.display(description="Tags") #---> class decorator
    def get_tags(self, obj):
        return ",".join([tag.name for tag in obj.tags.all()])



#I need to register 
admin.site.register(models.Tag)
admin.site.register(models.Category)
admin.site.register(models.Resources, CustomResources)
admin.site.register(models.ResourcesTag)
