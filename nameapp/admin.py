from django.contrib import admin
from .models import Address , ContactDetail


@admin.register(Address)
class AddressAdmin(admin.ModelAdmin):
    list_display = ('id','address','created_at')
    search_fields = ('address',)


# @admin.register(ContactDetail)
# class ContactDetailAdmin(admin.ModelAdmin):
#     list_display = ('id','Name','Phone','address','created_at')
#     search_fields = ('Name','Phone','address')


admin.site.register(ContactDetail)