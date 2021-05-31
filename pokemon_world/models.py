from django.db import models


class Element(models.Model):
    name = models.CharField(max_length=200,  primary_key=True)
    effective_agains = models.ManyToManyField('self' ,related_name='affected_by', null=True, blank=True)
class Movement(models.Model):
    name = models.CharField(max_length=200,  primary_key=True)
    element = models.ForeignKey('Element', on_delete=models.CASCADE, related_name='element')

class Region(models.Model):
    code = models.CharField(max_length=200,  primary_key=True)
    name = models.CharField(max_length=200)
    species = models.ManyToManyField('Specie', blank=True)
class Citizen(models.Model):
    id = models.CharField(max_length=200, primary_key=True)
    name = models.CharField(max_length=200)
    sex = models.CharField(max_length=1)
    age = models.IntegerField(default=1)
    born_region = models.ForeignKey('Region', on_delete=models.CASCADE, related_name='born_region')
    live_region = models.ForeignKey('Region', on_delete=models.CASCADE, related_name='live_region')
       
class City(models.Model): 
    name = models.CharField(max_length=200)
    id = models.CharField(max_length=200, primary_key=True)
    region = models.ForeignKey('Region', on_delete=models.CASCADE)
class Gym(models.Model):
    id =  models.CharField(max_length=200, primary_key=True)
    element = models.ForeignKey('Element', on_delete=models.CASCADE, related_name='gym_element')
    city = models.ForeignKey('City', on_delete=models.CASCADE, related_name='city')
    boss = models.OneToOneField('Trainer', on_delete=models.CASCADE, related_name='my_gym')
    

class Trainer(models.Model):
    citizen = models.OneToOneField('Citizen', on_delete=models.CASCADE, related_name='citizen')
    medals = models.ManyToManyField(Gym, blank=True)
    gym = models.ForeignKey('Gym', on_delete=models.SET_NULL, related_name='gym_member', null=True, blank=True)
    username = models.CharField(max_length=200, blank=True)
    
class Pokemon(models.Model):
    id = models.CharField(max_length=200, primary_key=True)
    height = models.IntegerField(default=1)
    weight = models.IntegerField(default=1)
    sex = models.CharField(max_length=1)
    chainy = models.BooleanField(default=False)
    nature = models.CharField(max_length=200)
    element = models.ForeignKey('Element', on_delete=models.CASCADE )
    movements = models.ManyToManyField('Movement', blank=True)
    specie = models.ForeignKey('Specie', on_delete=models.CASCADE, related_name='specie')
    captured_by = models.ForeignKey('Trainer', on_delete=models.SET_NULL, related_name='captured_by', null=True, blank=True)
class Specie(models.Model):
    name = models.CharField(max_length=200, primary_key=True)
    legendary = models.BooleanField(default=False)
    movements = models.ManyToManyField('Movement', blank=True)
class Own(models.Model):
    movement = models.ForeignKey('Movement', on_delete=models.CASCADE)

class Teach(models.Model):
    movement = models.ForeignKey('Movement', on_delete=models.CASCADE)
    
class Settlemen(models.Model):
    id = models.CharField(max_length=200, primary_key=True, default='')
    region = models.ForeignKey('Region', on_delete=models.CASCADE, related_name='region')

class Town(models.Model):
    name = models.CharField(max_length=200, primary_key=True)
    settlemen = models.ForeignKey('Settlemen', on_delete=models.CASCADE, related_name='settlemen')

class Duel(models.Model):
    id = models.CharField(max_length=200, primary_key=True)
    settlemen = models.ForeignKey('Settlemen', on_delete=models.CASCADE, related_name='duel_settlemen')
    trainer_win = models.ForeignKey('Trainer', on_delete=models.CASCADE, related_name='trainer_win')
    trainer_loss = models.ForeignKey('Trainer', on_delete=models.CASCADE, related_name='trainer_loss')
    date = models.DateTimeField(auto_now=False, auto_now_add=False)
    participants = models.ManyToManyField('Captured_Pokemon')

class Captured_Pokemon(models.Model):
    trainer = models.ForeignKey(Trainer, on_delete=models.CASCADE, related_name='captor')
    pokemon = models.ForeignKey(Pokemon, on_delete=models.CASCADE, related_name='captured')
    level = models.IntegerField(default=1)
    a_level = models.IntegerField(default=1)
    nick = models.CharField(max_length=200)
    pockeball =  models.IntegerField(default=1)
    