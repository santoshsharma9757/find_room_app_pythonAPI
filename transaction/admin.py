from django.contrib import admin
from .models import Transaction

# Register your models here.

class transactionAdmin(admin.ModelAdmin):
    list_display=['id','user','transaction_id',"is_payment_success"]

admin.site.register(Transaction,transactionAdmin)
