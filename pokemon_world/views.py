from django.shortcuts import render
from django.views.generic.base import TemplateView
from . import models

def base(request):
    return render(request, 'base.html')


class TrainersView(TemplateView):
    template_name = 'trainers.html'
    def get(self,request, *args, **kwargs):
        return super().get(request, *args, **kwargs)
    def post(self,request):
        name = request.POST['trainer_name']
        sex = request.POST['trainer_sex']
        age = request.POST['trainer_age']
        gym = request.POST['trainer_gym']        
        query = models.Trainer.objects.filter(citizen__name=name, citizen__sex=sex, citizen__age= int(age), gym__id=gym)
        return render(request, 'trainers.html',{'data':query})

class RegionView(TemplateView):
    template_name = 'region.html'
    def get(self,request, *args, **kwargs):
        return super().get(request, *args, **kwargs)
    def post(self,request):
        code = request.POST['region_code']
        name = request.POST['region_name']
            
        query = models.Region.objects.filter(code=code, name=name)
        return render(request, 'region.html',{'data':query})
    
class DuelView(TemplateView):
    template_name = 'duel.html'
    def get(self,request, *args, **kwargs):
        return super().get(request, *args, **kwargs)
    def post(self,request):
        id = request.POST['duel_id']
        settlemen_name = request.POST['settlemen_name']
        winner = request.POST['winner']
        losser = request.POST['losser']
        
        query = models.Duel.objects.filter(id=id, settlemen=settlemen_name, trainer_win=winner, trainer_loss=losser)
        return render(request, 'duel.html',{'data':query})
    
class SpecieView(TemplateView):
    template_name = 'specie.html'
    def get(self,request, *args, **kwargs):
        return super().get(request, *args, **kwargs)
    def post(self,request):
        name = request.POST['name']
        
        query = models.Specie.objects.filter(name=name)
        return render(request, 'specie.html',{'data':query})