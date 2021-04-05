from django.contrib import admin
from django.db.models.query import QuerySet
from django.http.request import HttpRequest
from app.gallery.models import Gallery

# Register your models here.
@admin.register(Gallery)
class GalleryAdmin(admin.ModelAdmin):
    search_fields = (
        'caption',
    )
    list_display = (
        'id',
        'get_file',
        'caption',
        'user',
        'created_at',
        'updated_at',
    )
    list_filter = (
        'content_type',
    )
    readonly_fields = (
        'content_type',
        'user',
    )
    list_per_page=20
    date_hierarchy='created_at'

    def get_queryset(self, request):
        qs = super(GalleryAdmin, self).get_queryset(request)
        return qs.filter(user=request.user)

    def save_model(self, request, obj, form, change):
        file = request.FILES.get('file')
        content_type = file.content_type
        obj.user = request.user
        obj.content_type = content_type
        return super().save_model(request, obj, form, change)
