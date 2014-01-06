from django.shortcuts import get_object_or_404
from django.views.generic import *
from braces.views import LoginRequiredMixin

# Create your views here.
###### Patient Model ######
class PatientListView(LoginRequiredMixin, ListView):
    pass
class PatientDetailView(LoginRequiredMixin, DetailView):
    pass
class PatientCreateView(LoginRequiredMixin, CreateView):
    pass
class PatientUpdateView(LoginRequiredMixin, UpdateView):
    pass
class PatientDeleteView(LoginRequiredMixin, DeleteView):
    pass
##### End PatientModel ######

class ClientListView(LoginRequiredMixin, ListView):
    model = Client
    template_name = 'client_create.html'

class ClientDetailView(LoginRequiredMixin, DetailView):
    model = Client
    template_name = 'client_detail.html'

class ClientCreateView(LoginRequiredMixin, CreateView):
    model = Client
    form_class = ClientCreateForm
    template_name = 'client_create.html'
class ClientUpdateView(LoginRequiredMixin, UpdateView):
    model = Client
    form_class = ClientUpdateForm
    template_name = 'client_update.html'

class ClientDeleteView(LoginRequiredMixin, DeleteView):
    model = Client
    template_name = 'client_delete.html'

class GuardianListView(LoginRequiredMixin, ListView):
    model = Guardian
    template_name = 'guardian_list.html'

class GuardianDetailView(LoginRequiredMixin, DetailView):
    model = Guardian
    template_name = 'guardian_detail.html'

class GuardianCreateView(LoginRequiredMixin, CreateView):
    model = Guardian
    form_class = GuardianCreateForm
    template_name = 'guardian_create.html'

class GuardianUpdateView(LoginRequiredMixin, UpdateView):
    model = Guardian
    form_class = GuardianUpdateForm
    template_name = 'guardian_update.html'

class GuardianDeleteView(LoginRequiredMixin, DeleteView):
    model = Guardian
    template_name = 'guardian_delete.html'

class EmployeeListView(LoginRequiredMixin, ListView):
    model = Employee
    template_name = 'employee_list.html'

class EmployeeDetailView(LoginRequiredMixin, DetailView):
    model = Employee
    template_name = 'employee_detail.html'

class EmployeeCreateView(LoginRequiredMixin, CreateView):
    model = Employee
    form_class = EmployeeCreateForm
    template_name = 'employee_create.html'

class EmployeeUpdateView(LoginRequiredMixin, UpdateView):
    model = Employee
    form_class = EmployeeUpdateForm
    template_name = 'employee_update.html'

class EmployeeDeleteView(LoginRequiredMixin, DeleteView):
    model = Employee
    template_name = 'employee_delete.html'

class AddressListView(LoginRequiredMixin, ListView):
    model = Address
    template_name = 'address_list.html'

class AddressDetailView(LoginRequiredMixin, DetailView):
    model = Address
    template_name = 'address_detail.html'

class AddressCreateView(LoginRequiredMixin, CreateView):
    model = Address
    form_class = AddressCreateForm
    template_name = 'address_create.html'

class AddressUpdateView(LoginRequiredMixin, UpdateView):
    model = Address
    form_class = AddressUpdateForm
    template_name = 'address_update.html'

class AddressDeleteView(LoginRequiredMixin, DeleteView):
    model = Address
    template_name = 'address_delete.html'
