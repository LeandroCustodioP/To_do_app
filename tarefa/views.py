from django.shortcuts import render,redirect
from .models import TarefaBd
from .forms import ConteudoForm

# Create your views here.
def index(request):
    conteudo=TarefaBd.objects.all()
    form=ConteudoForm()
    if request.method=='POST':
        form=ConteudoForm(request.POST)
        if form.is_valid():
            form=form.save()
            return redirect('/')
    context={
        'conteudos':conteudo,
        'form':form
    }
    return render(request,'lista.html',context)


def delete_tarefa(request,id):
    deleteTarefa=TarefaBd.objects.get(id=id)
    deleteTarefa.delete()
    return redirect('/')
