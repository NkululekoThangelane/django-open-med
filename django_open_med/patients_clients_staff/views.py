from django.shortcuts import get_object_or_404
from patients_clients_staff.serializers import *
from patients_clients_staff.models import *
from rest_framework import viewsets
from rest_framework.response import Response

# Create your views here.
class PatientViewSet(viewsets.ModelViewSet):
    pass
class ClientViewSet(viewsets.ModelViewSet):
    serializer_class = ClientSerializer
    queryset = Client.objects.all()
class GuardianViewSet(viewsets.ModelViewSet):
    serializer_class = GuardianSerializer
    queryset = Guardian.objects.all()
class EmployeeViewSet(viewsets.ModelViewSet):
    serializer_class = EmployeeSerializer
    queryset = Employee.objects.all()
class PhysicianViewSet(viewsets.ModelViewSet):
    pass
class TherapistViewSet(viewsets.ModelViewSet):
    pass
