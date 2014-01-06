from django.conf.urls import include, patterns, url
from django.views.generic import TemplateView
from patients_clients_staff.views import *

urlpatterns = patterns('patients_clients_staff.views',
        url(r'client/create$', ClientCreateView.as_view()),
        url(r'employee/create$', EmployeeCreateView.as_view()),
        url(r'guardian/create$', GuardianCreateView.as_view()),
        url(r'address/create$', AddressCreateView.as_view()),
        url(r'clients/create$', ClientListView.as_view()),
        url(r'employees$', EmployeeListView.as_view()),
        url(r'guardians$', GuardianListView.as_view()),
        url(r'addresses$', AddressListView.as_view()),
        url(r'client/(?P<slug>\d+)/update$', ClientUpdateView.as_view()),
        url(r'employee/(?P<slug>\d+)/update$', EmployeeUpdateView.as_view()),
        url(r'guardian/(?P<slug>\d+)/update$', GuardianUpdateView.as_view()),
        url(r'address/(?P<slug>\d+)/update$', AddressUpdateView.as_view()),
        url(r'client/(?P<slug>\d+)/delete$', ClientDeleteView.as_view()),
        url(r'employee/(?P<slug>\d+)/delete$', EmployeeDeleteView.as_view()),
        url(r'guardian/(?P<slug>\d+)/delete$', GuardianDeleteView.as_view()),
        url(r'address/(?P<slug>\d+/delete$', AddressDeleteView.as_view()),
        url(r'^clients/(?P<slug>\d+)/$', ClientDetailView.as_view()),
        url(r'^employees/(?P<slug>\d+)/$', EmployeeDetailView.as_view()),
        url(r'^guardians/(?P<slug>\d+)/$', GuardianDetailView.as_view()),
        url(r'^addresses/(?P<slug>\d+)/$', AddressDetailView.as_view()),
)
