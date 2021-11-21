from django.shortcuts import render
import json

# Create your views here.

def animal(request, animal_id):
    with open('data.json') as f:
        data = json.load(f)
    selected_animal = None
    for animal in data['animals']:
        if animal['id'] == animal_id:
            selected_animal = animal
    return render(request, 'animal.html', {'animal':selected_animal})


