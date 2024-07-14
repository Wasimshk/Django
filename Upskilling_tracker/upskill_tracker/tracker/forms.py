from django import forms
from .models import Goal, Progress

class GoalForm(forms.ModelForm):
    class Meta:
        model = Goal
        fields = ['title', 'description', 'start_date', 'end_date']
        widgets = {
            'start_date': forms.DateInput(format='%d/%m/%Y', attrs={'type': 'date'}),
            'end_date': forms.DateInput(format='%d/%m/%Y', attrs={'type': 'date'}),
        }

# forms.py

class ProgressForm(forms.ModelForm):
    completion_date = forms.DateField(label='Goal Completion Date', required=True, widget=forms.DateInput(format='%d/%m/%Y', attrs={'type': 'date'}))

    class Meta:
        model = Progress
        fields = ['goal', 'completion_date', 'progress']
        widgets = {
            'completion_date': forms.DateInput(format='%d/%m/%Y', attrs={'type': 'date'}),
        }

