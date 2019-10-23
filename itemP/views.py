from django.shortcuts import render, redirect, get_object_or_404
from django.forms import ModelForm

from itemp.models import Item_plan

class Item_planForm(ModelForm):
    class meta:
        model = Item_plan
        fields = ['plana','content','proced','recursos']

def itemP_list(request,pk, templa te_name='itemP/itemp_list.html'):