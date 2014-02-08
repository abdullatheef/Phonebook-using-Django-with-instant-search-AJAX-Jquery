from django.http import HttpResponse
import json
from django.shortcuts import render
from django.shortcuts import render_to_response
from django.views.decorators.csrf import csrf_exempt
from phonebook.models import *
from django.template import RequestContext
from django.template import Context
# Create your views here.

def home(request):
    return render_to_response('home.html')
@csrf_exempt
def check(request):
	for i in Persons.objects.all():
		if i.name==request.POST.get("name"):
			if i.passw==request.POST.get("pass"):
				request.session['member_id']=True
				a=i.name
				info=[dict(id=i.id,name=i.bname,number=i.number) for i in Book.objects.filter(idname=a)]
				return render(request,'details.html',{'b':a,'info':info})

	return render_to_response('err.html')
def signup(request):
	
	return render_to_response('signup.html')
@csrf_exempt
def add(request):
	if request.POST.get('name') =="" or request.POST.get('pass')=="":
		return render_to_response('home.html')
	else:	
		pname=request.POST.get('name')
		ppass=request.POST.get('pass')
		p=Persons(name=pname,passw=ppass)
		p.save()
		return render_to_response('afreg.html')
@csrf_exempt
def addc(request):
	try:
		if request.session['member_id']==True:
			cname=request.POST.get('name')
			cnum=request.POST.get('num')
			p=Book(bname=cname,number=cnum,idname=request.POST.get('c'))
			p.save()
			a=request.POST.get('c')
			info=[dict(id=i.id,name=i.bname,number=i.number) for i in Book.objects.filter(idname=a)]	
			return render(request,'details.html',{'b':a,'info':info})

	except KeyError:
	        pass
	return render_to_response('home.html')
def logout(request):
	try:
        	del request.session['member_id']
	except KeyError:
	        pass
	return render_to_response('home.html')
@csrf_exempt
def instant(request):
	d=request.POST['d']
	a=request.POST['c']
	info=[dict(id=i.id,name=i.bname,number=i.number) for i in Book.objects.filter(idname=a) if d.lower() in i.bname.lower()]
	data={'b':a,'info':info,'d':d}
	info=data['info']
	html=""
	for i in info:
		htm="<div><p></p><b>Name:</b>"+i['name']+"  &nbsp;&nbsp;<b>No:</b>"+i['number']+" </br></div></n>"	
		html=html+htm
	return HttpResponse(html)
'''
def save(request):
	alert("dfsdfdsfsd")
	return render_to_response('home.html')


	alert("sd")
	inst=request.POST.get('d')
	a=request.POST.get('c')
	alert(inst)
	info=[dict(id=i.id,name=i.bname,number=i.number) for i in Book.objects.filter(idname=a) if inst in i]
	return render(request,'details.html',{'info':info})
'''
	
	
