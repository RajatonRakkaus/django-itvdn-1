from django.urls import path
from django.urls.conf import include
from rest_framework import routers

from lesson_10 import views


router = routers.SimpleRouter()
router.register(r'view-set', views.ViewSetAPIView)

urlpatterns = [
    path('', include(router.urls)),
    path('function/', views.view_function, name='function_view'),
    path('class/', views.ClassAPIView.as_view(), name='class_view')
]
