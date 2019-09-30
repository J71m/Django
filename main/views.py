from django.shortcuts import *
from main.models import Asutus
from main.models import Tootaja

# Create your views here.
def home(request):
    return render(request, 'main/index.html')
    

def vaatatootaja(request):
    tootajad = Tootaja.objects.all()
    args = {'tootajad': tootajad}
    return render(request, 'main/vaatatootaja.html', args)
    

def lisatootaja(request):
    if request.method == "POST":
      asutus = request.POST.get('asutus', '')
      eesNimi = request.POST.get('eesNimi', '')
      perekonnaNimi = request.POST.get('perekonnaNimi', '')
      asutus = Asutus.objects.only('id').get(pk=asutus)
      Tootaja.objects.create(asutus=asutus, eesNimi=eesNimi, perekonnaNimi=perekonnaNimi)
    
    args = {'asutused' : Asutus.objects.all()}
    return render(request, 'main/lisatootaja.html', args)

def lisaasutus(request):
    if request.method == "POST":
      nimi = request.POST.get('nimi', '')
      Asutus.objects.create(nimi=nimi)
    
    return render(request, 'main/lisaasutus.html')

def kustutatootaja(request):
  tootaja_id = request.GET.get('id', '')
  tootaja = Tootaja.objects.get(id=tootaja_id)
  tootaja.delete()

  return HttpResponseRedirect('/vaatatootaja')