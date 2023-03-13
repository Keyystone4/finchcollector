from django.shortcuts import render

# Create your views here.

finches = [
  {'name': 'Wings', 'breed': 'House finch', 'description': 'small-bodied finches with fairly large beaks', 'age': 4},
  {'name': 'Tweet', 'breed': 'Pyrrhula', 'description': 'distinctive black cap, rose-red underparts, and white rump.', 'age': 6},
]

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def finches_index(request):
    return render(request, 'finches/index.html', {
    'finches': finches

    })