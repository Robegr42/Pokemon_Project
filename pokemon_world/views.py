from django.shortcuts import render
from django.views.generic.base import TemplateView


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
        region = request.POST['trainer_region_code']        
        
        return render(request, 'trainers.html')