from django.conf import settings
from django.contrib.auth import REDIRECT_FIELD_NAME
from django.contrib.sites.models import Site
from django.core.urlresolvers import reverse
from django.shortcuts import get_object_or_404, redirect, render_to_response
from django.template import RequestContext
from django.utils.http import urlquote
from django.dispatch import receiver

from forms_builder.forms import FormForForm
from forms_builder.models import Form
from forms_builder.settings import SEND_FROM_SUBMITTER, USE_SITES
from forms_builder.signals import form_invalid, form_valid
from forms_builder.utils import split_choices


def form_detail(request, slug, template="forms_builder/form_detail.html"):
    """
    Display a built form and handle submission.
    """
    published = Form.objects.published(for_user=request.user)
    form = get_object_or_404(published, slug=slug)
    if form.login_required and not request.user.is_authenticated():
        return redirect("%s?%s=%s" % (settings.LOGIN_URL, REDIRECT_FIELD_NAME,
                        urlquote(request.get_full_path())))
    request_context = RequestContext(request)
    args = (form, request_context, request.POST or None, request.FILES or None)
    form_for_form = FormForForm(*args)
    if request.method == "POST":
        if not form_for_form.is_valid():
            form_invalid.send(sender=request, form=form_for_form)
        else:
            entry = form_for_form.save(request)
            form_valid.send(sender=request, form=form_for_form, entry=entry)
            return redirect(reverse("form_sent", kwargs={"slug": form.slug}))
    context = {"form": form}
    return render_to_response(template, context, request_context)


def form_sent(request, slug, template="forms_builder/form_sent.html"):
    """
    Show the response message.
    """
    published = Form.objects.published(for_user=request.user)
    form = get_object_or_404(published, slug=slug)
    context = {"form": form}
    return render_to_response(template, context, RequestContext(request))

@receiver(form_valid)
def set_username(sender=None, form=None, entry=None, **kwargs):
    request = sender
    if request.user.is_authenticated():
        field = entry.form.fields.get_or_create(label="Username", required=False,visible=False,field_type=12 )
	field = field[0]
        field_entry, _ = entry.fields.get_or_create(field_id=field.id)
        field_entry.value = request.user.username
        field_entry.save()
