from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .models import Employee
from .serializers import EmployeeSerializer, EmployeeCreateSerializer, EmployeeUpdateSerializer, EmployeeDetailSerializer
from companies.models import Company
from accounts.models import User

class EmployeeListCreateView(generics.ListCreateAPIView):
    queryset = Employee.objects.all()
    permission_classes = [IsAuthenticated]

    def get_serializer_class(self):
        if self.request.method == 'POST':
            return EmployeeCreateSerializer
        return EmployeeSerializer

    def get_queryset(self):
        user = self.request.user
        if user.is_parent:
            # Parent users can see employees of companies they own
            return Employee.objects.filter(company__owner=user)
        elif user.is_admin:
            # Admin users can see employees within their company
            return Employee.objects.filter(company=user.company)
        elif user.is_employee:
            # Employees can only see their own profile
            return Employee.objects.filter(user=user)
        return Employee.objects.none() # Or handle as unauthorized
    
    def perform_create(self, serializer):
        # The create logic is already handled in EmployeeCreateSerializer.create method
        serializer.save()


class EmployeeDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Employee.objects.all()
    permission_classes = [IsAuthenticated]
    lookup_field = 'id' # Use 'id' field for lookup

    def get_serializer_class(self):
        if self.request.method in ['PUT', 'PATCH']:
            return EmployeeUpdateSerializer
        return EmployeeDetailSerializer

    def get_queryset(self):
        user = self.request.user
        if user.is_parent:
            # Parent users can manage employees of companies they own
            return Employee.objects.filter(company__owner=user)
        elif user.is_admin:
            # Admin users can manage employees within their company
            return Employee.objects.filter(company=user.company)
        elif user.is_employee:
            # Employees can only retrieve their own profile
            return Employee.objects.filter(user=user)
        return Employee.objects.none()

    def perform_destroy(self, instance):
        # Also delete the associated User object
        user = instance.user
        instance.delete()
        user.delete() 