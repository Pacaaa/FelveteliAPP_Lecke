
from django.http import HttpRequest, HttpResponse
from django.shortcuts import redirect, render
from APP.models import DIAK

def megnezes(request):

    if request.method=="POST" and 'kuldes' in request.POST:
       
       diak = DIAK.objects.filter(diakigazolvanyszam=request.POST['adat']).first()
       if diak != None:

           context={
               'diakigazolvanyszam':diak.diakigazolvanyszam,
               'diakneve':diak.diakneve,
               'elertpontszam':diak.elertpontszam,
               'felvetteke':diak.felvetteke,
               }
            
            
           return render(request,'bennevan.html',context)
       else:
            context={'szam':request.POST['adat']}        
            return render(request,'nincs.html',context)


    return render(request,'index.html')


def felvitel(request):

    if request.method=="POST" and 'mentes' in request.POST:

        ujdiak=request.POST['bevitel']
        
        for diak in ujdiak.splitlines():

            elem=diak.split('\t')
            DIAK.objects.create(
                diakigazolvanyszam=elem[0],
                diakneve=elem[1],
                elertpontszam=elem[2],
                felvetteke=elem[3],
            )
     
           

        

    return render(request,'felvitel.html')
   