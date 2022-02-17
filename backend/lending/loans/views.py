from rest_framework import generics

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
    queryset = Loan.objects.all()
    serializer_class = LoanSerializer


class AdminUpdateLoan(generics.RetrieveUpdateAPIView):
    queryset = Loan.objects.all()
    serializer_class = LoanSerializer


class AdminListCreatePayment(generics.ListCreateAPIView):

    serializer_class = TransactionSerializer

    def get_queryset(self):
        queryset = Transaction.objects.all()
        loan_id = self.request.query_params.get('loan_id', None)
        if loan_id is not None:
            queryset = Transaction.objects.filter(loan=loan_id)
        return queryset
