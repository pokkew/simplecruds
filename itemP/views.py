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
    data['iden'] = pk
    return render(request,template_name,data)


def itemP_create(request,pk, template_name='itemP/itemp_form.html'):
    plano = PlanA.objects.get(id=pk)
    form = Item_planForm(request.POST or None)
    form.fields['plana'].initial = plano.id
    form.fields['plana'].disabled = True
    if form.is_valid():
        form.save()
        return redirect('Plan_aula:itemP:itemp_list', pk=plano.id)
    return render(request, template_name, {'form': form, 'plano': plano})


def itemP_update(request, pkI, template_name='itemP/itemp_form.html'):
    itemplan = get_object_or_404(Item_plan, pk=pkI)
    plano = PlanA.objects.get(id=itemplan.plana_id)
    form = Item_planForm(request.POST or None, instance=itemplan)
    form.fields['plana'].disabled = True
    if form.is_valid():
        form.save()
        return redirect('Plan_aula:itemP:itemp_list', pk=plano.id)
    return render(request, template_name, {'form': form, 'plano': plano})

def itemP_delete(request, pkI, template_name='itemP/itemp_confirm_delete.html'):
    itemplan = get_object_or_404(Item_plan, pk=pkI)
    plano = PlanA.objects.get(id = itemplan.plana_id)
    if request.method=='POST':
        itemplan.delete()
        return redirect('Plan_aula:itemP:itemp_list', pk=plano.id)
    return render(request, template_name, {'object':itemplan})
