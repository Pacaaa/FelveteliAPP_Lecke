

from django.db import models


       
    
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