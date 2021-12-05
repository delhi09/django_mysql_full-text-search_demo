from django.contrib import admin

from .models import Novel


class NovelAdmin(admin.ModelAdmin):
    readonly_fields = ["search_text"]

    def save_model(self, request, obj, form, change):
        obj.search_text = f"{obj.title},{obj.content}"
        super().save_model(request, obj, form, change)


admin.site.register(Novel, NovelAdmin)
