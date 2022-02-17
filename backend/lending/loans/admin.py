from django.contrib import admin

from .models import Loan, Transaction


class LoanAdmin(admin.ModelAdmin):
    pass


class TransactionAdmin(admin.ModelAdmin):
    pass


admin.site.register(Loan, LoanAdmin)
admin.site.register(Transaction, TransactionAdmin)
