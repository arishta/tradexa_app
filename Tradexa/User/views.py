from django.shortcuts import render
from .forms import CreatePost
from .forms import UserRegistration
from .models import User

def showformdata(request):
	if request.method == 'POST':
		form = UserRegistration(request.POST)
		if form.is_valid():
			username = form.cleaned_data['username']
			first_name = form.cleaned_data['first_name']
			last_name = form.cleaned_data['last_name']
			email = form.cleaned_data['email']
			password = form.cleaned_data['password']
			reg = User(username = username, first_name = first_name, last_name = last_name, email = email, password = password)
			reg.save()
	else:
		form = UserRegistration()
	return render(request, 'User/user_registration.html',{'form':form})