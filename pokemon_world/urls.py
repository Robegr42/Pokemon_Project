from django.urls import path
from . import views


urlpatterns = [
    path('base/', views.base, name='base'),
    path('trainers/', views.TrainersView.as_view(), name='trainers'),
    path('region/', views.RegionView.as_view(), name='region'),
    path('duel/', views.DuelView.as_view(), name='duel'),
    path('specie/', views.SpecieView.as_view(), name='specie'),
    path('settlemen/', views.SettlemenView.as_view(), name='settlemen'),
    path('movement/', views.MovementView.as_view(), name='movement'),
    path('element/', views.ElementView.as_view(), name='element'),
    path('gym/', views.GymView.as_view(), name='gym'),
    
    
    
]

