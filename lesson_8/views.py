import csv
import datetime

from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import ListView

from lesson_8.models import GameModel, GamerModel


def upload_data(request):
    with open('vgsales.csv') as f:
        reader = csv.reader(f)

        for row in reader:
            try:
                _, created = GameModel.objects.get_or_create(
                    name = row[1],
                    platform = row[2],
                    year = datetime.date(int(row[3]), 1, 1),
                    genre = row[4],
                    publisher = row[5],
                    na_sales = row[6],
                    eu_sales = row[7],
                    jp_sales = row[8],
                    other_sales = row[9],
                    global_sales = row[10],
                )
            except:
                pass
    return HttpResponse('Done!')
    

class FilterView(ListView):
    template_name = 'gamemodel_list.html'
    queryset = GameModel.objects.filter(name__contains = 'Hitman')


class ExcludeView(ListView):
    template_name = 'gamemodel_list.html'
    queryset = GameModel.objects.exclude(name = 'Hitman')


class OrderByView(ListView):
    template_name = 'gamemodel_list.html'
    queryset = GameModel.objects.exclude(name = 'Hitman').order_by('year')


class AllView(ListView):
    template_name = 'gamemodel_list.html'
    queryset = GameModel.objects.all()


class UnionView(ListView):
    template_name = 'gamemodel_list.html'
    queryset = GameModel.objects.filter(name__contains = 'Hitman').union(
        GameModel.objects.filter(name__contains = 'Tetris')
    )


class NoneView(ListView):
    template_name = 'gamemodel_list.html'
    queryset = GameModel.objects.none()


class ValuesView(ListView):
    template_name = 'gamemodel_list.html'
    queryset = GameModel.objects.filter(name = 'Hitman (2016)').values()

    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)



def date_view(request):
    pass


def get_view(request):
    pass


def create_view(request):
    myself = GamerModel()
    myself.email = "admin@admin.com"
    myself.nickname = "SomeNick"
    myself.save()

    return HttpResponse(myself)





