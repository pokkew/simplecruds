from django.shortcuts import render, redirect, get_object_or_404
from django.forms import ModelForm

from Plan_aula.models import PlanA

class PlanAForm(ModelForm):
    class Meta:
        model = PlanA
        fields = '__all__'

def PlanA_list(request, template_name='Plan_aula/plana_list.html'):
    plana = PlanA.objects.all()
    data = {}
    data['object_list'] = plana
    return render(request, template_name, data)

def PlanA_create(request, template_name='Plan_aula/plana_form.html'):
    form = PlanAForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('Plan_aula:plana_list')
    return render(request, template_name, {'form':form})

def PlanA_update(request, pk, template_name='Plan_aula/plana_form.html'):
    plana = get_object_or_404(PlanA, pk=pk)
    form = PlanAForm(request.POST or None, instance=plana)
    if form.is_valid():
        form.save()
        return redirect('Plan_aula:plana_list')
    return render(request, template_name, {'form':form})

def PlanA_delete(request, pk, template_name='Plan_aula/plana_confirm_delete.html'):
    plana = get_object_or_404(PlanA, pk=pk)    
    if request.method=='POST':
        plana.delete()
        return redirect('Plan_aula:plana_list')
    return render(request, template_name, {'object':plana})
