from django.shortcuts import render

# Create your views here.
def MSD(request):
    d={'a':10,'b':1000,'c':50}
    return render(request,'MSD.html',d)