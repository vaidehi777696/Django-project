from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.views.decorators.csrf import csrf_exempt
from .models import Member
from .forms import MemberForm
# Create your views here.

def members(request):
  member_list = Member.objects.all().values()
  context = {
    'member_list':member_list
  }
  template = loader.get_template('members.html')
  return HttpResponse(template.render(context, request))


def detail(request,id):
  mymember = Member.objects.get(id=id)
  context = {
    
    'mymember':mymember
  }
  template = loader.get_template('detail.html')
  return HttpResponse(template.render(context, request))

def contact(request):
  template = loader.get_template('contact.html')
  return HttpResponse(template.render())

def hello(request):
  template = loader.get_template('hello.html')
  return HttpResponse(template.render())

@csrf_exempt
def add_newmember(request):
  if request.method=='POST':
    firstname= request.POST.get('firstname',)
    lastname= request.POST.get('lastname',)
    rollno= request.POST.get('rollno',)
    phoneno= request.POST.get('phoneno',)
    image=request.FILES['image']
    member=Member(firstname=firstname,lastname=lastname,rollno=rollno,phoneno=phoneno,image=image)
    member.save()
  template = loader.get_template('add_newmember.html')
  return HttpResponse(template.render())

def update(request,id):
  member=Member.objects.get(id=id)
  form=MemberForm(request.POST,instance=member)
  if form.is_valid():
     form.save()
     t1=loader.get_template('add_newmember.html')
     return HttpResponse(t1.render())
  return render(request,'update.html',{'form':form,'member':member})

@csrf_exempt
def delete(request,id):
  if request.method == 'POST':
    member=Member.objects.get(id=id)
    member.delete()
    t1=loader.get_template('members.html')
    return HttpResponse(t1.render())
  return render(request,'delete.html')
