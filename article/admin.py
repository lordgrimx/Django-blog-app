from django.contrib import admin

from .models import Article,Comment

# Register your models here.

#admin.site.register(Comment) #* Bu kod article isimli classi admin panelinde gormemizi sagliyor.

@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    
    list_display = ["title","author","created_date"]

    list_display_links = ["title","author","created_date"]

    search_fields = ["title"]

    list_filter = ["created_date"]
    
    
    class Meta: # Bu django tarafindan belirlenen bir dacarator yazimi ve bu classin ismi Meta olmak zorunda
        model = Article

@admin.register(Comment)
class ArticleAdmin(admin.ModelAdmin):
    
    list_display = ["comment_author","comment_station","comment_date"]
    
    
    class Meta: # Bu django tarafindan belirlenen bir dacarator yazimi ve bu classin ismi Meta olmak zorunda
        model = Article