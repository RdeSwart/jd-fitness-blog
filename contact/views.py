from django.shortcuts import render, redirect
from .forms import ContactForm
from django.contrib import messages
from django.http import HttpResponseRedirect 

# Create your views here.

def contact_form_view(request):
    """
    This view handles both POST and GET requests for the contact form.

    """
    if request.method == "POST":
        contact_form = ContactForm(data=request.POST)
        if contact_form.is_valid():
            contact_form.save()
            messages.add_message(request, messages.SUCCESS,
            'Your message has been recieved' 
            'we will get back to you as soon as possible.')
            return HttpResponseRedirect(request.path_info)
    else:
        contact_form = ContactForm()
    return render(request, 'contact.html', {'contact_form': contact_form})
        