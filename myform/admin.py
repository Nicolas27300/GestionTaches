from django.contrib import admin
from myform.models import Contact

class ContactAdmin(admin.ModelAdmin):
    list_display = ('name', 'firstname', 'email', 'message')

admin.site.register(Contact, ContactAdmin)
