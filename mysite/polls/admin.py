
# Register your models here.
from django.contrib import admin

from .models import Choice, Question

# admin.site.register(Question)
# class QuestionAdmin(admin.ModelAdmin):
#     fields = ['pub_date', 'question_text']

# admin.site.register(Question, QuestionAdmin)
# class QuestionAdmin(admin.ModelAdmin):
#     fieldsets = [
#         (None,               {'fields': ['question_text']}),
#         ('Date information', {'fields': ['pub_date']}),
#     ]

# admin.site.register(Question, QuestionAdmin)
# class QuestionAdmin(admin.ModelAdmin):
#     fieldsets = [
#         (None,               {'fields': ['question_text']}),
#         ('Date information', {'fields': ['pub_date'], 'classes': ['collapse']}),
#     ]

# class ChoiceInline(admin.StackedInline):
#     model = Choice
#     extra = 3
class ChoiceInline(admin.TabularInline):
	model = Choice
    # extra = 3
class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,               {'fields': ['question_text']}),
        ('Date information', {'fields': ['pub_date'], 'classes': ['collapse']}),
    ]
    inlines = [ChoiceInline]
    # list_display = ('question_text', 'pub_date')
    list_display = ('question_text', 'pub_date', 'was_published_recently')

# class ChoiceInline(admin.TabularInline):
# 	model = Choice
#     extra = 3
admin.site.register(Question, QuestionAdmin)
admin.site.register(Choice)
