from django.shortcuts import render,redirect
from numpy import number
from . models import *
from django.core.files.storage import FileSystemStorage
from django.utils.datastructures import MultiValueDictKeyError
# Create your views here.
def indexC(request):
	return render(request,'indexchatbot.html')

def logC(request):
    return render(request,'loginC.html')    

def logintheC(request):
	uname = request.POST.get('uname')
	password = request.POST.get('password')
	if Thereg.objects.filter(uname=uname,password=password).exists():
		data = Thereg.objects.filter(uname=uname,password=password).values('email','img','location','id').first()
		request.session['email']=data['email']
		request.session['img']=data['img']
		request.session['location']=data['location']
		request.session['id']=data['id']
		request.session['uname']=uname  
		request.session['password']=password
		return redirect('indexC') 
	else:
		return render(request,'loginC.html',{'msg':"Sorry... Invalid username or password"})    

def regC(request):
    return render(request,'registerC.html')  

def registertheC(request):
	if request.method=='POST':
		uname = request.POST.get('uname')
		password = request.POST.get('password')
		location = request.POST.get('location')
		email = request.POST.get('email')
		img = request.FILES['img']
		data = Thereg(uname=uname,location=location,password=password,email=email,img=img)
		data.save()
		return redirect('logC')

def thelogoutC(request):
	del request.session['uname']
	del request.session['location']
	del request.session['img']
	del request.session['email']
	del request.session['password']
	del request.session['id']
	return redirect('logC')

def about_the(request):
	return render(request,'aboutCthe.html')    


def contact_the(request):
	return render(request,'contactCthe.html')  


def therapist_the(request):
	return render(request,'therapistCthe.html')   

def doctor_the(request):
	return render(request,'doctorCthe.html')   

def concellr_the(request):
	return render(request,'concellrCthe.html')   		

def indexUser1(request):
	return render(request,'user/indexuserC.html')  

def contact_user(request):
	return render(request,'user/user_contact.html')	

def reg_user(request):
	return render(request,'user/register_user.html')

def registertheC(request):
	if request.method=='POST':
		uname = request.POST.get('uname')
		password = request.POST.get('password')
		age = request.POST.get('your_age')
		gname = request.POST.get('your_gname')
		location = request.POST.get('your_location')
		email = request.POST.get('your_email')
		number = request.POST.get('your_number')
		data = Userreg(uname=uname,gname=gname,age=age,location=location,password=password,email=email,number=number)
		data.save()
		return redirect('reg_user')	

def RegUser(request):
	uname = request.POST.get('uname')
	password = request.POST.get('password')
	if Userreg.objects.filter(uname=uname,password=password).exists():
		data = Userreg.objects.filter(uname=uname,password=password).values('email','number','age','gname','location','id').first()
		request.session['email']=data['email']
		request.session['number']=data['number']
		request.session['age']=data['age']
		request.session['gname']=data['gname']
		request.session['location']=data['location']
		request.session['id']=data['id']
		request.session['uname']=uname  
		request.session['password']=password
		return redirect('indexUser1') 
	else:
		return render(request,'user/register_user.html',{'msg':"Sorry... Invalid username or password"})   		


def userlogout(request):
	del request.session['uname']
	del request.session['gname']
	del request.session['age']
	del request.session['location']
	del request.session['number']
	del request.session['email']
	del request.session['password']
	del request.session['id']
	return redirect('RegUser')

def add_lab(request):
	return render(request,'addlabdetails.html')
    

def lablist(request):
    if request.method=='POST':
        Name= request.POST.get('Name')
        drname = request.POST.get('dr_name')
        age = request.POST.get('age')
        number = request.POST.get('number')
        gender = request.POST.get('gender')
        bgroup = request.POST.get('gender')
        img = request.FILES['img']
        data = labsaddreport(Name=Name,drname=drname,age=age,number=number,gender=gender,bgroup=bgroup,img=img)
        data.save()
    return redirect('indexC')   

def labtable(request):
    data3 = labsaddreport.objects.all()
    return render(request,'labtable.html',{'data3':data3})        


def labdelete(request,labdid):
    data = labsaddreport.objects.filter(id=labdid)
    data.delete()
    return render(request,'labtable.html')


def reg_doctor(request):
	return render(request,'doctor/doc_reg.html') 	

def registerdoc(request):
	if request.method=='POST':
		uname = request.POST.get('uname')
		password = request.POST.get('password')
		qua = request.POST.get('your_qua')
		experience = request.POST.get('your_experience')
		location = request.POST.get('your_location')
		email = request.POST.get('your_email')
		number = request.POST.get('your_number')
		data = Docreg(uname=uname,experience=experience,qua=qua,location=location,password=password,email=email,number=number)
		data.save()
		return redirect('reg_doctor')	

def RegDoc(request):
	uname = request.POST.get('uname')
	password = request.POST.get('password')
	if Docreg.objects.filter(uname=uname,password=password).exists():
		data = Docreg.objects.filter(uname=uname,password=password).values('email','number','qua','experience','location','id').first()
		request.session['email']=data['email']
		request.session['number']=data['number']
		request.session['qua']=data['qua']
		request.session['experience']=data['experience']
		request.session['location']=data['location']
		request.session['id']=data['id']
		request.session['uname']=uname  
		request.session['password']=password
		return redirect('indexC') 
	else:
		return render(request,'doctor/doc_reg.html',{'msg':"Sorry... Invalid username or password"})   		

def doclogout(request):
	del request.session['uname']
	del request.session['qua']
	del request.session['experience']
	del request.session['location']
	del request.session['number']
	del request.session['email']
	del request.session['password']
	del request.session['id']
	return redirect('RegDoc')
