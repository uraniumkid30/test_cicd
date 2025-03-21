from django.contrib import admin
from apps.user.models import User, Profile
from django.contrib.auth.admin import UserAdmin

class CustomUserAdmin(UserAdmin):
    
    fieldsets= (
        (None, {
            'fields':('username', 'password', 'is_active', 'is_staff', 'is_superuser' ),
        }),
        ('Personal info', {
            'fields': ('email',),
        }),
        ('Permissions', {
            'fields': ('groups','user_permissions',),
        }),
        ('Important dates', {
            'fields': ('last_login','date_joined',),
        }),
    )

    add_fieldsets = (
        (None, {
            'classes': ('wide',), #wider layout
            'fields': ('username', 'password1', 'password2'),
        }),
    )


    exclude = ('first_name', 'last_name')


    


# Register your models here.
#you register one models at the time
admin.site.register(User, CustomUserAdmin)
admin.site.register(Profile)
