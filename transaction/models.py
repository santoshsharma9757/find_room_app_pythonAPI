from django.db import models
import uuid
from account.models import User

# Create your models here.
class Transaction(models.Model):
        id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
        user = models.ForeignKey(User, on_delete=models.CASCADE,related_name='transaction')
        is_payment_success= models.BooleanField(default=False)
        transaction_id=models.CharField(max_length=200)

        # def __str__(self):
        #         return self.id