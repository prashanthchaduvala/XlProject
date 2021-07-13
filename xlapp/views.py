from django.shortcuts import render,redirect
from django.shortcuts import render
import xml.etree.ElementTree as ET

# local imports
from xlapp.models import *



def showmain(request):
    im = File.objects.all()
    return render(request,"index.html",{"data":im})



def showindex(request):
    file = request.FILES['xlfile']
    # tree = ET.parse(file)
    try:
        data = File(file=file)
        data.save()
        message = ('file uploaded sucessfully')
        return redirect('/show/')
    except:
        message = ('not uploaded')
        return render(request, 'error.html', {"message": message})


def showdata(request):
    data = File.objects.all()
    return render(request,'show.html',{'data1':data})


def showindex(request):
    file = request.FILES['xlfile']
    if not file.name.endswith('xlsx'):
        messag = ('wrong format')
        return render(request,'index.html',{'message':messag})
    else:
        if file.name.endswith('xlsx'):
            data = File(file=file)
            data.save()
            return redirect('/show/')
        else:
            return render(request,'index.html')
    return redirect('/')






from xlapp.resources import  FileResource
from django.contrib import messages
from tablib import Dataset

from django.http import HttpResponse

# def simple_upload(request):
#     if request.method == 'POST':
#         file_resource = FileResource()
#         dataset = Dataset()
#         new_file = request.FILES['xlfile']
#
#         if not new_file.name.endswith('xlsx'):
#             message=(request,'wrong format')
#             return render(request,'index.html',{"messag":message})
#         else:
#             if new_file.name.endswith('xlsx'):
#                 # File.objects.create(file=new_file)
#                 data = File(file=new_file)
#                 data.save()
#                 datas= File.objects.all()
#                 return render(request, 'show1.html', {'data1': datas})
#         return render(request,'show.html')
#     return render(request,'index.html')







# from xlapp.forms import *
#
# def showindex(request):
#     form = Profile_Form()
#     if request.method == 'POST':
#         form = Profile_Form(request.POST, request.FILES)
#         if form.is_valid():
#             user_pr = form.save(commit=False)
#             user_pr.file = request.FILES['file']
#             file_type = user_pr.file.url.split('.')[-1]
#             file_type = file_type.lower()
#             if file_type not in IMAGE_FILE_TYPES:
#                 return render(request, 'profile_maker/error.html')
#         user_pr.save()
#         return render(request, 'profile_maker/details.html', {'user_pr': user_pr})
#     context = {"form": form,}
#     return render(request, 'profile_maker/create.html', context)