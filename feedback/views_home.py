from django.shortcuts import render
from .models import Feedback

def home(request):
    feedbacks = Feedback.objects.select_related('user').all()
    return render(request, 'home.html', {'feedbacks': feedbacks})