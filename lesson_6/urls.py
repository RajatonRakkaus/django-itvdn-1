from django.urls import path
from lesson_6 import views

urlpatterns = [
    path('try-form/', views.my_form, name='try-form'),
    path('class-form/', views.MyFormView.as_view(), name='class-form'),
    path('try-modelform/', views.ModelFormView.as_view(), name='modelform')  
]
