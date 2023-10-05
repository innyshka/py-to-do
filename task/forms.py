from django import forms

from task.models import Task, Tag
from django.utils import timezone


class TaskForm(forms.ModelForm):
    tags = forms.ModelMultipleChoiceField(
        queryset=Tag.objects.all(),
        widget=forms.CheckboxSelectMultiple,
    )

    deadline_time = forms.DateTimeField(
        required=False,
        widget=forms.DateTimeInput(attrs={'type': 'datetime-local'}),
        input_formats=['%Y-%m-%dT%H:%M'],
    )

    class Meta:
        model = Task
        fields = ("content", "deadline_time", "tags")

    def clean_deadline_time(self):
        deadline = self.cleaned_data.get("deadline_time")
        if deadline:
            if timezone.now() >= deadline:
                raise forms.ValidationError("Invalid date for deadline")
        return deadline
