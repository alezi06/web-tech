from django import forms
from django.shortcuts import get_object_or_404
from .models import Question, Answer


class AskForm(forms.Form):
    title = forms.CharField(max_length=200)
    text = forms.CharField(widget=forms.Textarea)

    def save(self):
        return Question.objects.create(**self.cleaned_data)


class AnswerForm(forms.Form):
    text = forms.CharField(widget=forms.Textarea)
    question = forms.IntegerField(widget=forms.HiddenInput)

    def clean_question(self):
        question_id = self.cleaned_data['question']
        question = get_object_or_404(Question, pk=question_id)
        return question

    def save(self):
        return Answer.objects.create(**self.cleaned_data)
