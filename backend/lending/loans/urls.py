from django.urls import path

from .views import ListCreateLoan, AdminUpdateLoan, AdminListCreatePayment, AdminListLoans

app_name = 'loan'

urlpatterns = [
    path('customer/', ListCreateLoan.as_view(), name='list_customer_loans'),
    path('', AdminListLoans.as_view(), name='list_all_loan'),
    path('<pk>/', AdminUpdateLoan.as_view(), name='update_loan'),
    path('pay', AdminListCreatePayment.as_view(), name='pay_loan'),
]
