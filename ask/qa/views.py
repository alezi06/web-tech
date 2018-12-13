from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from .models import Question
from .forms import AskForm, AnswerForm


def new(request):
    new_questions = Question.objects.new()
    paginator = Paginator(new_questions, 10)

    page = request.GET.get('page')
    try:
        questions = paginator.page(page)
    except PageNotAnInteger:
        questions = paginator.page(1)
    except EmptyPage:
        questions = paginator.page(paginator.num_pages)

    return render(request, 'qa/new.html', {'questions': questions})


def popular(request):
    popular_questions = Question.objects.popular()
    paginator = Paginator(popular_questions, 10)

    page = request.GET.get('page')
    try:
        questions = paginator.page(page)
    except PageNotAnInteger:
        questions = paginator.page(1)
    except EmptyPage:
        questions = paginator.page(paginator.num_pages)

    return render(request, 'qa/popular.html', {'questions': questions})


def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    form = AnswerForm(request.POST or None, initial={'question': question.id})
    if form.is_valid():
        form.save()
        url = question.get_url()
        return HttpResponseRedirect(url)

    return render(request, 'qa/question.html', {'question': question, 'form': form})


def ask(request):
    form = AskForm(request.POST or None)
    if form.is_valid():
        question = form.save()
        url = question.get_url()
        return HttpResponseRedirect(url)

    return render(request, 'qa/ask.html', {'form': form})
