from django.contrib import admin
from user_app.models import User
# Register your models here.
class UserAdmin(admin.ModelAdmin):
    list_display = ['first_name','last_name','email','phone','password',]
    
admin.site.register(User,UserAdmin)
