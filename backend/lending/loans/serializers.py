from rest_framework import serializers

from .models import Loan, Transaction


class LoanSerializer(serializers.ModelSerializer):
    customer_name = serializers.CharField(source='customer', read_only=True)

    class Meta:
        model = Loan
        fields = ['id', 'customer_name', 'category', 'request_date', 'status', 'reason', 'amount', 'term',
                  'frequency', 'interest', 'remark', 'installment_amount']
        read_only_fields = ['customer']


class TransactionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transaction
        fields = '__all__'
