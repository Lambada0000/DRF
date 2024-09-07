from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters
from rest_framework.viewsets import ModelViewSet

from users.models import Payments
from users.serializers import PaymentsSerializer


class PaymentsViewSet(ModelViewSet):
    queryset = Payments.objects.all()
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter]
    serializer_class = PaymentsSerializer
    filterset_fields = (
        "course",
        "lesson",
        "payment_type",
    )
    ordering_fields = ("payment_date",)
