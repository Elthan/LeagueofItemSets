from django.contrib import admin 
from .models import Question

# Register your models here.
class QuestionAdmin(admin.ModelAdmin):
	list_display = ('question_text', 'pub_date')
	list_filter = ['pub_date']
	search_fields = ['question_text']
	
	
admin.site.register(Question, QuestionAdmin)