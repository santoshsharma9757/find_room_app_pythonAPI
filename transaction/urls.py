from django.urls import path
from .views import TransactionView,TransactionValidate

urlpatterns = [
    path("verify/transaction/", TransactionView.as_view()),
    path("verify/transaction/validate/", TransactionValidate.as_view(),name='verify_transaction'),
    

]