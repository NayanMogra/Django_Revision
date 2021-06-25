from django.core.checks.messages import Error
from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import *


    
def string_installation_manupluation(result , ind):
    for i in range(result.index('"')+3 , len(result)):
        if(result[i] == '"' and result[i+1] == '"' and result[i+2] == '"'):
                title = result[result.index('"')+3:i]
                break
    desc = result[i+3:]
    replace_char = ['\n' , '"' , "'" ]
    for chr in replace_char:
        desc = desc.replace(chr,'')
    
    obj = show_code(
        category = ind,
        title = title,
        code = desc
    )
    try:
        obj.save()
        return obj
    except:
        return False


def home_page(request,pk=1):
    print(pk)
    category_choosen = indicator.objects.filter(id = pk).first()  
    obj = show_code.objects.filter(
                category=category_choosen)
    
    all_category_list = indicator.objects.all()
    print(all_category_list)
    return render(request , 'home.html' , {'obj' : obj , 'all_category_list':all_category_list})
