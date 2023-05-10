from django.shortcuts import render,redirect
from django.http import JsonResponse
from .models import attendance
# Create your views here.

def home(request):
    entries = attendance.objects.all()
    return render(request, 'home.html', {'entries':entries})

def attendpost(request):
    print(request.GET.get('personid'))
    if attendance.objects.filter(personid=request.GET.get('personid')):
        return JsonResponse({"success":"yes","added":"no", "already punched":"yes"})
    punch = attendance(personid=request.GET.get('personid'))
    punch.save()
    return JsonResponse({"success":"yes","added":"yes"})

def delete(request):
    attendance.objects.all().delete()
    return redirect ('home')
