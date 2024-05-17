from django.contrib import admin
from .models import Transaction

# Register your models here.

class transactionAdmin(admin.ModelAdmin):
    list_display=['id','user','transaction_id']

admin.site.register(Transaction,transactionAdmin)
