from rest_framework import generics
from rest_framework.permissions import IsAdminUser

from .models import Loan, Transaction
from .serializers import LoanSerializer, TransactionSerializer


class ListCreateLoan(generics.ListCreateAPIView):
    queryset = Loan.objects.all()
    serializer_class = LoanSerializer

    def get_queryset(self):
        """
        filter loans based on authenticated user.
        """
        customer = self.request.user
        return Loan.objects.filter(customer=customer)


class AdminListLoans(generics.ListAPIView):
    permission_classes = [IsAdminUser]
    queryset = Loan.objects.all()
    serializer_class = LoanSerializer


class AdminUpdateLoan(generics.RetrieveUpdateAPIView):
    permission_classes = [IsAdminUser]
    queryset = Loan.objects.all()
    serializer_class = LoanSerializer


class AdminListCreatePayment(generics.ListCreateAPIView):
    permission_classes = [IsAdminUser]
    serializer_class = TransactionSerializer

    def get_queryset(self):
        """
        filter all transactions per loan
        """
        queryset = Transaction.objects.all()
        loan_id = self.request.query_params.get('loan_id', None)
        if loan_id is not None:
            queryset = Transaction.objects.filter(loan=loan_id)
        return queryset
