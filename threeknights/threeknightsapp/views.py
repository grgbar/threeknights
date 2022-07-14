from django.shortcuts import render
from django.http  import HttpResponse
from .models import Exercise

# Create your views here.
def index(request):
    return HttpResponse("Request:" + request.get_host()) 

def exercise_by_id (request, exercise_id):
    exercise = Exercise.objects.get(pk=exercise_id)
    #return HttpResponse(f"Exercise: {exercise.name}, points: {exercise.points}")
    return render (request, 'exercise_details.html', {'exercise': exercise})