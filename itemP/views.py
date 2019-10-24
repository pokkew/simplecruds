from django.shortcuts import render, redirect, get_object_or_404
from django.forms import ModelForm

from itemP.models import Item_plan
from Plan_aula.models import PlanA

class Item_planForm(ModelForm):
    class Meta:
        model = Item_plan
        fields = ['plana','content','proced','recursos']


def itemP_list(request,pk, template_name='itemP/itemp_list.html'):
    itemplan = Item_plan.objects.filter(plana_id = pk)
    data = {}
    data['object_list'] = itemplan
    return render(request,template_name,data)

def itemP_create(request,pk, template_name='itemP/itemp_form.html'):
    plano = PlanA.objects.get(id = pk)
    form = Item_planForm(request.POST or None)
    form.fields['plana'].initial = plano.id
    form.fields['plana'].disabled = True
    if form.is_valid():
        form.save()
        return redirect('Plan_aula:itemP:itemp_list',pk=plano.id)
    return render(request, template_name, {'form':form})
