from django.shortcuts import render

# Create your views here.
def docente_list(request, template_name='Plan_aula/plana_list.html'):
    plana = PlanA.objects.all()
    data = {}
    data['object_list'] = plana
    return render(request, template_name, data)
