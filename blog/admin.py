from django.contrib import admin
from .models import Post

class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_at', 'published_at')
    search_fields = ('title',)
    list_filter = ('published_at',)

    # Добавим возможность редактировать заголовок статьи
    def save_model(self, request, obj, form, change):
        super().save_model(request, obj, form, change)

admin.site.register(Post, PostAdmin)