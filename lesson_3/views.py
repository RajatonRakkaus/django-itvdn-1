from django.shortcuts import render
from django.http import HttpResponse, FileResponse, HttpResponseRedirect, HttpResponseNotAllowed, JsonResponse
from django.templatetags.static import static


from django.views import View

from django.template import loader


class MyView(View):

    def get(self, request):
        if request.GET.get('type') == 'json':
            return JsonResponse({i: i + i for i in range(1, 20)}, safe=False)
        elif request.GET.get('type') == 'redirect':
            return HttpResponseRedirect("http://www.google.com")
        return HttpResponse('This is GET')

    def post(self, request):
        print(request.POST)
        return HttpResponse('This is POST')


def main(request):
    test_template = loader.render_to_string(template_name="templates_example.html",
    context={'str': "Text string", "int": 12})

    return HttpResponse(test_template) 


def text(request):
    return HttpResponse("Backend text")


def file(request):
    return HttpResponse("No file")


def redirect(request):
    return HttpResponseRedirect("http://www.google.com")


def not_allowed(request):
    return HttpResponseNotAllowed("No pasaran!")


def json(request):
    return JsonResponse({i: i + i for i in range(1, 20)}, safe=False)



