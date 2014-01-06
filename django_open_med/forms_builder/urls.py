from django.conf.urls import include, patterns, url
from forms_builder.views import *

urlpatterns = patterns('forms_builder.views',
    url(r"(?P<slug>.*)/sent/$", "form_sent", name="form_sent"),
    url(r"(?P<slug>.*)/$", "form_detail", name="form_detail"),
)
