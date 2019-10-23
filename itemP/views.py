from django.shortcuts import render, redirect, get_object_or_404
from django.forms import ModelForm

from itemP.models import Item_plan

class Item_planForm(ModelForm):
    class meta:
        model = Item_plan
        fields = ['plana','content','proced','recursos']

def itemP_list(request,pk, template_name='itemP/itemp_list.html'):
    itemplan = Item_plan.objects.filter(plana_id = pk)
    data = {}
    data['object_list'] = itemplan
    return render(request,template_name,data)
   