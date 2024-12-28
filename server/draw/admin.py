from django.contrib import admin
from draw.models import DrawingModel, FileModel
from django.utils.safestring import mark_safe


class FileAdmin(admin.ModelAdmin):

    list_display = ('name', 'link', )
    search_fields = ('name', 'link')
    list_filter = ('name', 'link')
    # readonly_fields = ('name', 'link',)
    fieldsets = (
        (None, {
            'fields': ('name', 'link',)
        }),
    )


class DrawingAdmin(admin.ModelAdmin):
    
        list_display = ('name', 'order_by', 'status', 'created_at', )
        search_fields = ('name', 'created_at', 'status', 'link', 'pdf', 'webp', 'prw', )
        list_filter = ('created_at', 'status', )
        readonly_fields = ('created_at',)
        list_editable = ('status', 'order_by',)
        fieldsets = (
            (None, {
                'fields': ('name', 'status', 'created_at', 'link', 'pdf', 'webp', 'prw', )
            }),
        )


admin.site.register(FileModel, FileAdmin)
admin.site.register(DrawingModel, DrawingAdmin)
