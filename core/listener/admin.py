from core.listener.models import Listener
from django.contrib import admin

# Register your models here.
class ListenerAdmin(admin.ModelAdmin):
    fields = (
        'url',
        'active',
    )
    search_fields = (
        'url',
    )
    list_display = (
        'id',
        'get_url',
        'active',
        'created_at',
        'updated_at'
    )
    date_hierarchy = 'created_at'

    def save_model(self, request, obj, form, change):
        obj.user = request.user
        return super().save_model(request, obj, form, change)

    def get_queryset(self, request):
        qs = super().get_queryset(request)
        if not request.user.is_superuser:
            return qs.filter(user=request.user)
        return qs
    
admin.site.register(Listener, ListenerAdmin)
