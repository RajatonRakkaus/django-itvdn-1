from django import template
from django.template import loader
from django.http import HttpResponse
from django.views.generic.base import TemplateView


# This code block is no longer necessary because TemplateView does
#
# that automatically
# def index_post(request):
#     latest_question_list = [
#         {'id': 2, 'question_text': 'How can I call you?'},
#         {'id': 3, 'question_text': 'How do you do?'},
#         {'id': 1, 'question_text': 'What is your name?'},
#         {'id': 4, 'question_text': ''},
#     ]

#     template = loader.get_template('post_page.html')
#     context = {'latest_question_list': latest_question_list}
#     print(context)
#     return HttpResponse(template.render(context, request))


def post_page(request, number):
    if number == 1:
        return HttpResponse("My name is Giovanni Giorgio")
    elif number == 2:
        return HttpResponse("But people usually call me Giorgio")
    elif number == 3:
        return HttpResponse("*electronic music playing*")
    else:
        return HttpResponse("Wrong question")


class MyTemplateView(TemplateView):
    template_name = "post_page.html"

    def get_context_data(self, **kwargs) :
        return {'latest_question_list': [
        {'id': 2, 'question_text': 'How can I call you?'},
        {'id': 3, 'question_text': 'How do you do?'},
        {'id': 1, 'question_text': 'What is your name?'},
        {'id': 4, 'question_text': ''},
    ]}




