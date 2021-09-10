from django import forms
from durationwidget.widgets import TimeDurationWidget

from lesson_5.models import Client

class MyForm(forms.Form):
    name = forms.CharField(label='Username')
    email = forms.EmailField(required=False, error_messages={'required': 'Please input your available email'})
    password = forms.CharField(max_length=20, min_length=4, 
        widget=forms.PasswordInput())
    age = forms.IntegerField(required=False, help_text='Enter your age')
    agreement = forms.BooleanField(required=False)
    average_score = forms.FloatField(initial=10.1)

    birthday = forms.DateTimeField(required=False, 
        widget=forms.SelectDateWidget)
    work_experience = forms.DurationField(required=False, 
        widget=TimeDurationWidget(show_seconds=False, show_minutes=False))
    gender = forms.ChoiceField(required=False, 
        choices=[('male', 'male'), ('female', 'female')])

    profile_picture = forms.ImageField(widget=forms.FileInput)
    additional_file = forms.FileField(widget=forms.FileInput)


class FormFromModel(forms.ModelForm):
    class Meta:
        model = Client
        fields = '__all__'