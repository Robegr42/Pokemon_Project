from django.shortcuts import render
from django.views.generic.base import TemplateView
from . import models
from django.db.models import Count 
from django.db.models import Q

def base(request):
    return render(request, 'base.html')


class TrainersView(TemplateView):
    template_name = 'trainers.html'
    def get(self,request, *args, **kwargs):
        return super().get(request, *args, **kwargs)
    def post(self,request):
        id = request.POST['trainer_id']
        name = request.POST['trainer_name']
        query = models.Trainer.objects.filter(id__startswith=id, citizen__name__startswith=name)
        return render(request, 'trainers.html',{'data':query})

class RegionView(TemplateView):
    template_name = 'region.html'
    def get(self,request, *args, **kwargs):
        return super().get(request, *args, **kwargs)
    def post(self,request):
        if 'region_search' in request.POST:
            button = 'region_search'
            code = request.POST['region_code']
            name = request.POST['region_name']
            regions = models.Region.objects.filter(code__startswith=code, name__startswith=name)
            data = []
            for region in regions:
                duels = models.Trainer.objects.all().annotate(win_duels=Count('trainer_win',filter = Q(trainer_win__settlemen__region__pk=region.code),distinct=True))
                duels = duels.filter(win_duels__gt=2)
                citizens = models.Citizen.objects.filter(live_region__code=region.code).count()
                trainers = models.Trainer.objects.filter(citizen__live_region__code=region.code).count()
                if citizens >0:
                    trainers_porcent = trainers/citizens*100
                else:
                    trainers_porcent = 0
                    
                win_medals = models.Trainer.objects.all().annotate(got_medals=Count('medals',filter = Q(medals__city__region__pk=region.code),distinct=True))
                win_medals = win_medals.filter(got_medals__gt=7)    
                
                data.append({'region' : region, 'duels':duels, 'percent': trainers_porcent, 'medals': win_medals} )
            
        
        
        return render(request, 'region.html',{'data': data})

class DuelView(TemplateView):
    template_name = 'duel.html'
    def get(self,request, *args, **kwargs):
        return super().get(request, *args, **kwargs)
    def post(self,request):
        id = request.POST['duel_id']
        settlemen_id = request.POST['settlemen_id']
        winner = request.POST['winner']
        losser = request.POST['losser']

        query = models.Duel.objects.filter(id__startswith=id, settlemen__id__startswith=settlemen_id, trainer_win__pk__startswith=winner, trainer_loss__pk__startswith=losser)
        return render(request, 'duel.html',{'data':query})

class SpecieView(TemplateView):
    template_name = 'specie.html'
    def get(self,request, *args, **kwargs):
        return super().get(request, *args, **kwargs)
    def post(self,request):
        name = request.POST['name']

        query = models.Specie.objects.filter(name__startswith=name)
        return render(request, 'specie.html',{'data':query})

class SettlemenView(TemplateView):
    template_name = 'settlemen.html'
    def get(self,request, *args, **kwargs):
        return super().get(request, *args, **kwargs)
    def post(self,request):
        id = request.POST['id']
        region = request.POST['region']
        query = models.Settlemen.objects.filter(id__startswith=id, region__code__startswith=region)
        return render(request, 'settlemen.html',{'data':query})
class MovementView(TemplateView):
    template_name = 'movement.html'
    def get(self,request, *args, **kwargs):
        return super().get(request, *args, **kwargs)
    def post(self,request):
        name = request.POST['name']
        element = request.POST['element_name']
        query = models.Movement.objects.filter(name__startswith=name, element__name__startswith=element)
        return render(request, 'movement.html',{'data':query})
class ElementView(TemplateView):
    template_name = 'element.html'
    def get(self,request, *args, **kwargs):
        return super().get(request, *args, **kwargs)
    def post(self,request):
        name = request.POST['name']
        if  'elements_search' in request.POST:
            if name == '':
                query = models.Element.objects.all()
            else:
                query = models.Element.objects.filter(name__startswith=name)


        return render(request, 'element.html',{'data': query})

class GymView(TemplateView):
    template_name = 'gym.html'
    def get(self,request, *args, **kwargs):
        return super().get(request, *args, **kwargs)
    def post(self,request):
        id = request.POST['id']
        element = request.POST['element']
        city = request.POST['city']

        query = models.Gym.objects.filter(id=id, element__name=element, city__id=city)
        return render(request, 'gym.html',{'data':query})