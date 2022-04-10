
from tkinter import CASCADE
from django.db import models


       


# class Iskola(models.Model):
    
#     # TODO: Define fields here

#     class Meta:
       
#         verbose_name = 'Iskola'
#         verbose_name_plural = 'Iskolas'

#     iskola_diakigazolvanyszam=models.IntegerField()
#     iskola=models.TextField()


#     def __str__(self):
#         return f"{self.iskola}"
    
class DIAK(models.Model):
    
    class Meta:
       

         verbose_name = 'DIAK'
         verbose_name_plural = 'DIAKs'

    
    diakigazolvanyszam=models.IntegerField()
    diakneve=models.TextField()
    elertpontszam=models.FloatField()
    felvetteke=models.BooleanField()
    # iskola=models.ForeignKey(Iskola, on_delete=models.CASCADE)

    def __str__(self):
        
        return f"{self.diakneve}"