from django.forms import ModelForm, Form, CharField, TextInput

from .models import Movie, Cinema, Screening

class MovieForm(ModelForm):
    class Meta:
        model = Movie
        fields = "__all__"

class CinemaForm(ModelForm):
    class Meta:
        model = Cinema
        fields = '__all__'


class ScreeningForm(ModelForm):
    class Meta:
        model = Screening
        fields = '__all__'
        
        

# class MovieForm(Form):
#     title = CharField(label="Title: ", max_length=100, id=)

# class AuthorForm(ModelForm):
#     fullname = CharField(
#         max_length=60,
#         min_length=3,
#         widget=TextInput(attrs={"class": "form-control "}))