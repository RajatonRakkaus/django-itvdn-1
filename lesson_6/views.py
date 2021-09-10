import os

from  django.conf import settings
from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic.edit import FormView
from django.urls import reverse_lazy

from lesson_6.forms import MyForm


def my_form(request):

    form = MyForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        print(form.cleaned_data)
        print(form.errors)
        file_path = os.path.join(settings.MEDIA_ROOT,
                                form.cleaned_data['profile_picture'].name)

        with open(file_path, 'wb+') as local_file:
            for chunk in form.cleaned_data['profile_picture']:
                local_file.write(chunk)

    return render(request, 'form_page.html', context={'form': form})


class MyFormView(FormView):
    form = MyForm
    template_name = 'form_page.html'

    def get(self, request):
        print(request.GET)
        
        return super().get(request)


class ModelFormView(FormView):
    form_class = MyForm
    template_name = 'model_from_page.html'
    success_url = reverse_lazy('modelform')

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)
