from django.shortcuts import render,redirect
from .import forms
from .import models

def add_author(request):
    if request.method == 'POST':
        author_form = forms.AuthorForm(request.POST)
        if author_form.is_valid():
            author_form.save()
            return redirect('homepage')
    else:
        author_form = forms.AuthorForm()
    return render(request,'add_author.html',{'form':author_form})

def edit_author(request,id):
    author = models.Author.objects.get(pk=id)
    author_form = forms.AuthorForm(instance=author)
    if request.method == 'POST':
        author_form = forms.AuthorForm(request.POST,instance=author)  
        if author_form.is_valid():
            author_form.save()
            return redirect('homepage')  
    return render(request,'add_author.html',{'form':author_form})