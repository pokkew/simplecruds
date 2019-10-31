from django.shortcuts import render, redirect, get_object_or_404
from django.forms import ModelForm, HiddenInput
from Plan_aula.models import PlanA
from django.contrib.auth.decorators import login_required


class PlanAForm(ModelForm):
    class Meta:
        model = PlanA
        fields = ['uc', 'evento', 'ch', 'obj', 'docente', 'user']
        widgets = {'user': HiddenInput()}


def PlanA_list(request, template_name='Plan_aula/plana_list.html'):
    if request.user.id==1:
        plana = PlanA.objects.all()
    else:
        plana = PlanA.objects.filter(user = request.user)
    data = {}
    data['object_list'] = plana
    return render(request, template_name, data)

def PlanA_create(request, template_name='Plan_aula/plana_form.html'):
    form = PlanAForm(request.POST or None)
    form.fields['user'].initial = request.user.id
    if form.is_valid():
        form.save()
        return redirect('Plan_aula:plan_list')
    return render(request, template_name, {'form':form})

def PlanA_update(request, pk, template_name='Plan_aula/plana_form.html'):
    plana = get_object_or_404(PlanA, pk=pk)
    form = PlanAForm(request.POST or None, instance=plana)
    if form.is_valid():
        form.save()
        return redirect('Plan_aula:plan_list')
    return render(request, template_name, {'form':form})

def PlanA_delete(request, pk, template_name='Plan_aula/plana_confirm_delete.html'):
    plana = get_object_or_404(PlanA, pk=pk)
    if request.method=='POST':
        plana.delete()
        return redirect('Plan_aula:plan_list')
    return render(request, template_name, {'object':plana})
