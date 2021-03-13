from django import forms 
from django.forms import ModelForm


from .models import Task


class TaskForm(forms.ModelForm):
    class Meta:
        model = Task 
        fields = ('title','description',)


class CompleteTaskForm(forms.Form):
    completed_picture = forms.ImageField()



class ScrapbookDateForm(forms.Form):
    scrapBook_date = forms.DateField(widget=forms.DateInput(attrs={'type':'date'}))