from django.db import models


class Element(models.Model):
    name = models.CharField(max_length=200,  primary_key=True)
    
class Movement(models.Model):
    name = models.CharField(max_length=200,  primary_key=True)
    element = models.ForeignKey(Element, on_delete=models.CASCADE)
   
class Date(models.Model):
    id = models.CharField(max_length=200, primary_key=True)
    
    
class Region(models.Model):
    code = models.CharField(max_length=200,  primary_key=True)
    name = models.CharField(max_length=200)

class Citizen(models.Model):
    id = models.CharField(max_length=200, primary_key=True)
    name = models.CharField(max_length=200)
    sex = models.CharField(max_length=1)
    Age = models.IntegerField(default=1)
    region = models.ForeignKey(Region, on_delete=models.CASCADE)
    #l_code = models.ForeignKey(Region, on_delete=models.CASCADE)
       
class City(models.Model): 
       name = models.CharField(max_length=200)
       id = models.CharField(max_length=200, primary_key=True)
       region = models.ForeignKey(Region, on_delete=models.CASCADE)
class Gym(models.Model):
    id =  models.CharField(max_length=200, primary_key=True)
    element = models.ForeignKey(Element, on_delete=models.CASCADE)
    city = models.ForeignKey(City, on_delete=models.CASCADE)

class Trainer(models.Model):
    id = models.CharField(max_length=200, primary_key=True)
    trainer = models.ForeignKey(Citizen, on_delete=models.CASCADE)
    gym = models.ForeignKey(Gym, on_delete=models.CASCADE)
    
class Pokemon(models.Model):
    id = models.CharField(max_length=200, primary_key=True)
    height = models.IntegerField(default=1)
    weight = models.IntegerField(default=1)
    sex = models.CharField(max_length=1)
    nature = models.CharField(max_length=200)
    trainer = models.ForeignKey(Trainer, on_delete=models.CASCADE)

class Knows(models.Model):
    pokemon = models.ForeignKey(Pokemon, on_delete=models.CASCADE)
    movement = models.ForeignKey(Movement, on_delete=models.CASCADE)
    
class Leads(models.Model):
    citizen = models.ForeignKey(Citizen, on_delete=models.CASCADE)
    trainer = models.ForeignKey(Trainer, on_delete=models.CASCADE)
    gym = models.ForeignKey(Gym, on_delete=models.CASCADE)
    
class Got_Medals(models.Model):
    citizen = models.ForeignKey(Citizen, on_delete=models.CASCADE)
    trainer = models.ForeignKey(Trainer, on_delete=models.CASCADE)
    Gym = models.ForeignKey(Gym, on_delete=models.CASCADE)
    
class Specie(models.Model):
    name = models.CharField(max_length=200, primary_key=True)
    legendary = models.BooleanField(default=False)

class Belongs(models.Model):
    pokemon = models.ForeignKey(Pokemon, on_delete=models.CASCADE)
    specie = models.ForeignKey(Specie, on_delete=models.CASCADE)
    
class Inhabited(models.Model): 
    specie = models.ForeignKey(Specie, on_delete=models.CASCADE)
    region = models.ForeignKey(Region, on_delete=models.CASCADE)
    
class Own(models.Model):
    movement = models.ForeignKey(Movement, on_delete=models.CASCADE)

class Teach(models.Model):
    movement = models.ForeignKey(Movement, on_delete=models.CASCADE)
    
class Settlemen(models.Model):
    id = models.CharField(max_length=200, primary_key=True)
    region = models.ForeignKey(Region, on_delete=models.CASCADE)

class Town(models.Model):
    name = models.CharField(max_length=200, primary_key=True)
    settlemen = models.ForeignKey(Settlemen, on_delete=models.CASCADE)
    region = models.ForeignKey(Region, on_delete=models.CASCADE)

class Effective_Against(models.Model):
    elemnt_1 = models.ForeignKey(Element, on_delete=models.CASCADE)
    element_2 = models.ForeignKey(Element, on_delete=models.CASCADE, related_name='element2')

class BelongsE(models.Model):
    element = models.ForeignKey(Element, on_delete=models.CASCADE)
    specie = models.ForeignKey(Specie, on_delete=models.CASCADE)
    
class KnowsM(models.Model):
    specie = models.ForeignKey(Specie, on_delete=models.CASCADE)
    movement = models.ForeignKey(Movement, on_delete=models.CASCADE)
    
class Duel(models.Model):
    id = models.CharField(max_length=200, primary_key=True)
    settlemen = models.ForeignKey(Settlemen, on_delete=models.CASCADE)
    trainer_win = models.ForeignKey(Trainer, on_delete=models.CASCADE)
    trainer_loss = models.ForeignKey(Trainer, on_delete=models.CASCADE, related_name='trainer_loss')
    date = models.ForeignKey(Date, on_delete=models.CASCADE)

class Captured_Pokemon(models.Model):
    trainer = models.ForeignKey(Trainer, on_delete=models.CASCADE)
    pokemon = models.ForeignKey(Pokemon, on_delete=models.CASCADE)
    level = models.IntegerField(default=1)
    a_level = models.IntegerField(default=1)
    nick = models.CharField(max_length=200)
    pockeball =  models.IntegerField(default=1)
    
class Plays(models.Model): 
    duel = models.ForeignKey(Duel, on_delete=models.CASCADE)
    t_id = models.ForeignKey(Captured_Pokemon, on_delete=models.CASCADE)
    #pk_id = models.ForeignKey(Captured_Pokemon, on_delete=models.CASCADE)
    
