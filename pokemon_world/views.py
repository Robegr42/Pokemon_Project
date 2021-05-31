from django.shortcuts import render,redirect
from django.contrib.auth import login
from django.urls import reverse
from django.views.generic.base import TemplateView
from . import models
from django.db.models import Count, Q
from django.contrib.auth.forms import UserCreationForm
from django import forms



class MyTrainerForm(forms.Form):
    id = forms.CharField(label='ID', max_length=200, required=True)
    name = forms.CharField(label='Nombre', max_length=200, required=True)
    sex = forms.CharField(label='Sexo', max_length=1, required=True)
    age = forms.IntegerField(label='Edad', required=True)
    born_region = forms.CharField(label='Region de Nacimiento', required=True)
    live_region = forms.CharField(label='Region de Residencia', required=True)

def base(request):
    return render(request, 'base.html')

def register(request):
    if request.method == "GET":
        return render(
            request, 'register.html',
            {"form": UserCreationForm}
        )
    elif request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect(reverse('base'))
        else:
            return render(
            request, 'register.html',
            {"form": UserCreationForm}
        )
class ProfileView(TemplateView):
    template_name = 'trainerprofile.html'
    def get(self,request, *args, **kwargs):
        profile = models.Trainer.objects.filter(username=request.user.username)
        if profile.count() == 1:
            profile = profile[0]
            data = {'profile' : profile}
            profile.my_gym.pk
        else:
            profile = None
            data = {'form' : MyTrainerForm}
        return render(request, 'trainerprofile.html', data)
    def post(self,request):
        if 'add' in request.POST:
            t = models.Trainer.objects.filter(id=request.POST['trainer_id'])
            boss = models.Trainer.objects.filter(username=request.user.username)[0]
            if t.count():
                temp=t[0]
                temp.gym = boss.my_gym
                temp.save()
            return render(request, 'trainerprofile.html')
        citizen = MyTrainerForm(request.POST)
        if citizen.is_valid():
            born_region = models.Region.objects.filter(code=citizen.cleaned_data['born_region'])[0]
            live_region = models.Region.objects.filter(code=citizen.cleaned_data['live_region'])[0]
            temp = models.Citizen(id=citizen.cleaned_data['id'], name=citizen.cleaned_data['name'], sex=citizen.cleaned_data['sex'], age=citizen.cleaned_data['age'], live_region=live_region, born_region=born_region)
            temp.save()
            models.Trainer.objects.create(citizen=temp, username=request.user.username)
        else: render(request, 'trainerprofile.html', {'form':MyTrainerForm})
        return render(request, 'trainerprofile.html')
        
class TrainersView(TemplateView):
    template_name = 'trainers.html'
    def get(self,request, *args, **kwargs):
        return super().get(request, *args, **kwargs)
    def post(self,request):
        if 'trainers_query' in request.POST:
            button = 'trainers_query' 
            id = request.POST['trainer_id']
            name = request.POST['trainer_name']
            query = models.Trainer.objects.filter(citizen__pk__startswith=id, citizen__name__startswith=name)
        elif 'specie_search' in request.POST:
            button = 'specie_search'
            id = request.POST['specie_trainer_id']
            specie = request.POST['specie']
            query = models.Captured_Pokemon.objects.filter(trainer__citizen__pk=id, pokemon__specie__name=specie)
            
            
        return render(request, 'trainers.html',{'data':query, 'button': button})

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

        query = models.Duel.objects.filter(id__startswith=id, settlemen__id__startswith=settlemen_id, trainer_win__citizen__pk__startswith=winner, trainer_loss__citizen__pk__startswith=losser)
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
        query = models.Gym.objects.filter(id__startswith=id, element__name__startswith=element, city__id__startswith=city)
        return render(request, 'gym.html',{'data':query})