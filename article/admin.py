from typing import ContextManager
from django.contrib import admin

from .models import Article,Comment

admin.site.register(Comment)
# Register your models here.
@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    
    #Sitenin article sayfasını özelleştirmeye yarayan kodlar;
    list_display = ["title","author","created_date"] #article sayfasını özelleştirmede kullandığımız kod
    list_display_links = ["title","created_date"] #link görevi görmesini istediğimiz yerlerin kodu
    search_fields = ["title"] #arama çubuğu koymamızı sağlayan kod
    list_filter = ["created_date"] #zaman filtresi koymamızı sağlayan kod
    
    class Meta:
        model = Article