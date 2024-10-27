from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin
from address.models import Address

CustomUser = get_user_model()

class AddressInline(admin.StackedInline):
    model = Address
    can_delete = False
    verbose_name_plural = 'Endereço'

class CustomUserAdmin(UserAdmin):
    inlines = (AddressInline,)
    list_display = ('username', 'email', 'first_name', 'last_name', 'get_address')
    
    def get_address(self, obj):
        address = Address.objects.filter(user=obj).first()
        if address:
            return f"{address.street}, {address.number}, {address.neighborhood}, {address.city}, {address.state}"
        return "Sem endereço"
    
    get_address.short_description = 'Endereço'

admin.site.unregister(CustomUser)
admin.site.register(CustomUser, CustomUserAdmin)
