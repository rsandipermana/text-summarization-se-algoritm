from django.contrib import admin
from .models import Article, Summary, Evaluation
class ArticleAdmin(admin.ModelAdmin):
    list_display = ['title']
    
admin.site.register(Article, ArticleAdmin)
admin.site.register(Summary)
admin.site.register(Evaluation)