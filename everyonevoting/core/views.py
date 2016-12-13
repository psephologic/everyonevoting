from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, HttpResponse,\
    HttpResponseRedirect, redirect
from django.views.generic import TemplateView, FormView
from django.core.mail import send_mail
from django.core.urlresolvers import reverse_lazy

from .models import Organization
from .forms import EmailRegistrationForm, OrganizationSearchForm


def email_test(request):
    recipient = request.POST['recipient']
    send_mail('Welcome to the OpenEMS!', 'Please confirm your account.', 'no-reply@psephologic.com',
    [recipient], fail_silently=False)


class IndexView(TemplateView):
    template_name = 'core/index.html'


class WelcomeView(FormView):
    template_name = 'core/welcome.html'
    form_class = EmailRegistrationForm
    success_url = reverse_lazy('success')

    def form_valid(self, form):
        message = "{name} / {email} said: ".format(
            name=form.cleaned_data.get('name'),
            email=form.cleaned_data.get('email'))
        message += "\n\n{0}".format(form.cleaned_data.get('message'))
        send_mail(
            subject=form.cleaned_data.get('subject').strip(),
            message=message,
            from_email='contact-form@myapp.com',
            recipient_list=[''],
        )
        return super(WelcomeView, self).form_valid(form)


class SuccessView(TemplateView):
    template_name='core/success.html'


def organizations(request):
    context = {}
    organizations = Organization.objects.all()
    context['organizations'] = organizations
    return render("core/organizations.html", context)


def organization_lookup(request, args):
    organization = Organization.objects.filter(subdomain=args)
    return HttpResponse(organization)


def organization_search(request, args):
    organization = Organization.objects.filter(name=args)
    return render(request, organization)