from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView

from .forms import UserRegistrationForm


# Create your views here.
class UserRegistration(CreateView):
    template_name = "Registration.html"
    form_class = UserRegistrationForm
    success_url = reverse_lazy('homepage')     # The URL to redirect to when the form is successfully processed

    #Constructs a form, checks the form for validity, and handles it accordingly.
    def post(self, request, *args, **kwargs):
        """
        Handle POST requests: instantiate a form instance with the passed
        POST variables and then check if it's valid.
        """
        form = self.get_form()
        # check whether it's valid:
        if form.is_valid():
            # Get User object
            user = form.save()

            # Use set_password here with Cleaned(normalized) data.
            # (it's a method which save password into encrypted form)
            user.set_password(form.cleaned_data['password'])
            user.save()
            return self.form_valid(form)  # Redirects to get_success_url().
        else:
            return self.form_invalid(form)  # Renders a response, providing the invalid form as context.


def buyerlogin(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        # import pdb;pdb.set_trace()
        user = authenticate(email=email, password=password)

        # when user is valid then allow it for the respective page.
        if user is not None:
            login(request, user)  # redirect to the login in-built method.
            return redirect('/')

        # else redirect it to the login page.
        else:
            return redirect("/user-login/")

def sellerlogin(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        user = authenticate(username=email, password=password)

        # when user is valid then allow it for the respective page.
        if user is not None:
            login(request, user)  # redirect to the login in-built method.
            return redirect('/')

        # else redirect it to the login page.
        else:
            return redirect("/seller-login/")
