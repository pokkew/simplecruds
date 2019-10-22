from django.shortcuts import render, redirect, get_object_or_404
from django.forms import ModelForm

from Plan_aula.models import PlanA

class PlanAForm(ModelForm):
    class Meta:
        model = PlanA
        fields = '__all__'

def PlanA_list(request, template_name='books_fbv/book_list.html'):
    plana = PlanA.objects.all()
    data = {}
    data['object_list'] = plana
    return render(request, template_name, data)

def PlanA_create(request, template_name='books_fbv/book_form.html'):
    form = PlanAForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('books_fbv:book_list')
    return render(request, template_name, {'form':form})

def PlanA_update(request, pk, template_name='books_fbv/book_form.html'):
    plana = get_object_or_404(Book, pk=pk)
    form = PlanAForm(request.POST or None, instance=book)
    if form.is_valid():
        form.save()
        return redirect('books_fbv:book_list')
    return render(request, template_name, {'form':form})

def PlanA_delete(request, pk, template_name='books_fbv/book_confirm_delete.html'):
    plana = get_object_or_404(Book, pk=pk)    
    if request.method=='POST':
        plana.delete()
        return redirect('books_fbv:book_list')
    return render(request, template_name, {'object':plana})
