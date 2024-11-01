from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics
from rest_framework.filters import OrderingFilter
from users.models import Payment
from users.serializers import PaymentSerializer
                               # RegisterSerializer, RetrieveSerializer, UpdateSerializer)
from users.models import User
from django.views.generic import CreateView, UpdateView, ListView, DetailView


"""PaymentListView"""


class PaymentListAPIView(generics.ListAPIView):
    serializer_class = PaymentSerializer
    queryset = Payment.objects.all()
    filter_backends = [DjangoFilterBackend, OrderingFilter]
    filterset_fields = ('method', 'course_id', 'lesson_id')
    ordering_fileds = ('date')