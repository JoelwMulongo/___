
# admin.py
from .models import Blog
admin.site.register(Blog)

# Custom model Admin (admin.py): 
class BlogAdmin(admin.ModelAdmin)
    list_display = ("title", "description")
    ordering("date_created",)
    search_fields("title", "description")

# Register app
admin.site.register(Blog, BlogAdmin)