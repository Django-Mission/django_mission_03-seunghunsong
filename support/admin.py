from django.contrib import admin
from .models import Faq, Inquiry, Answer

class FaqInline(admin.TabularInline):
    model = Answer
    min_num = 1
    max_num = 1
    verbose_name = '답변'
    verbose_name_plural = '답변'

@admin.register(Faq)
class FaqModelAdmin(admin.ModelAdmin):
    list_display = ('title', 'categroy', 'update_at')
    search_fields = ('title',)
    list_filter = ('categroy',)

@admin.register(Inquiry)
class InquiryModelAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_at', 'writer')
    search_fields = ('title', 'phone_number', 'get_email',)
    list_filter = ('categroy',)
    inlines = [FaqInline]