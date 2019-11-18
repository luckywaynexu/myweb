from django.contrib import admin

# Register your models here.
from .models import Question
# 问题对象需要被管理
admin.site.register(Question)