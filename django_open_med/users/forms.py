import floppyforms as forms
from patients_clients_staff.utils import generate_random_username
from patients_clients_staff.models import Client
from forms_builder.models import Form

class DatePicker(forms.DateInput):
    class Media:
        js = (
            'js/jquery.min.js',
            'js/jquery-ui.min.js',
        )
        css = {
            'all': (
                'css/jquery-ui.css',
            )
        }
class ClientCreateForm(forms.ModelForm):
    appointment = forms.DateField(widget=DatePicker)
    user_forms = forms.ModelMultipleChoiceField(queryset=Form.objects.none(), required=False)

    class Meta:
        model = Client
        exclude = {}
        widget = {
        }

    def clean(self):
        pass
    def save(self):
        pass
class GuardianCreateForm(forms.ModelForm):
    pass
class NewUserWizard(FormWizard):
    pass
