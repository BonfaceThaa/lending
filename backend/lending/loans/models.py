from django.db import models

from accounts.models import Account


class Loan(models.Model):
    """
    Class representing a Loan.
    """
    StatusType = models.TextChoices('StatusType', 'Approved Denied Pending Processing')
    CategoryType = models.TextChoices('CategoryType', 'Personal Business Health Other')
    customer = models.ForeignKey(Account, on_delete=models.CASCADE, related_name='loans')
    category = models.CharField(max_length=25, blank=True, choices=CategoryType.choices)
    request_date = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=25, blank=True, choices=StatusType.choices)
    reason = models.TextField(max_length=500, blank=True)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    term = models.IntegerField(blank=True, null=True)
    frequency = models.IntegerField(blank=True, null=True)
    interest = models.IntegerField(blank=True, null=True)
    remark = models.TextField(max_length=500, blank=True)
    installment_amount = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f'{self.customer.first_name} - {self.amount} - {self.category.name}'


class CustomerLoan(models.Model):
    """
    Class representing the current loan status.
    """
    customer = models.ForeignKey(Account, on_delete=models.CASCADE)
    total_loan = models.DecimalField(max_digits=10, decimal_places=2)
    payable_loan = models.DecimalField(max_digits=10, decimal_places=2)



class Transaction(models.Model):
    """
    Class representing payment transactions for settling or paying loans.
    """
    loan = models.ForeignKey(Loan, on_delete=models.CASCADE, related_name='transactions')
    customer = models.ForeignKey(Account, on_delete=models.CASCADE, related_name='payments')
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    payment_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.amount} - {self.payment_date}'


