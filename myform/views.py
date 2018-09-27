from django.shortcuts import render, redirect
from django.forms import ModelForm, Textarea
from django import forms
from myform.models import Contact
from django.template import RequestContext
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse

class ContactForm(ModelForm):
    class Meta:
        model = Contact
        fields = ('name', 'firstname', 'email', 'message')
        widgets = {
            'message' : Textarea(attrs={'cols' : 40, 'rows' : 3}),
        }
        labels = {
            'name' : 'Nom',
            'firstname' : 'Prénom',
        }

#liste tous les contacts
def list(request):
    contacts = Contact.objects.all()
    form = ContactForm()
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            new_contact = form.save()
            return redirect(reverse('list'))
    contexte = {'contacts' : contacts, 'form' : form}
    return render(request, 'contact.html', contexte)

def edit(request, cid):
    contacts = Contact.objects.all()
    contact = Contact.objects.get(pk=cid)
    form = ContactForm(instance=contact)
    if request.method == 'POST':
        form = ContactForm(request.POST, instance=contact)
        if form.is_valid():
            form.save()
            return redirect(reverse('list'))
    contexte = {'form': form, 'path' : '/contacts/edit/' + str(cid), 'contacts' : contacts}
    return render(request, 'contact.html', contexte)

def remove(request, cid):
    Contact.objects.get(pk=cid).delete()
    return redirect(reverse('list'))

def detail(request, cid):
    contact = Contact.objects.get(pk=cid)
    return HttpResponse('<p>Nouveau Contact</p>' + contact.name)

def editdetail(request, cid):
    contact = Contact.objects.get(pk=cid)
    return HttpResponse('<p>Contact modifiét</p>' + contact.name)