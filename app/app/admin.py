from django.contrib import admin
from .models import Article, Summary, Evaluation

admin.site.register(Article)
admin.site.register(Summary)
admin.site.register(Evaluation)