from django.shortcuts import render
from.forms import FormTarea
from .models import Tarea

# Create your views here.
def main(request):
    if request.method == 'POST':
        form = FormTarea(request.POST)
        if form.is_valid():
            form.save()
    form = FormTarea()
    tarea = Tarea.objects.all()
    context = {'form':form, 'tareas':tarea}
    return render(request, 'main.html', context)