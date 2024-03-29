from django.contrib import admin

from .models import Choice, Question
# Register your models here.


class QuestionAdmin(admin.ModelAdmin):
    fields = ['pub_date', 'question_text']


admin.site.register(Choice)
admin.site.register(Question, QuestionAdmin)
