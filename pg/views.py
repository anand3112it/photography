from django.shortcuts import render, redirect
from django.http import HttpResponse
from pg.models import Banner, Category, Portfolio, Blog
from pg.services.ser import mainService
from django.views import generic

# Create your views here.

def home(request):
	return render(request, 'home.html', {
		'banner' : Banner.objects.filter(status = 1),
		'category' : Category.objects.filter(status = 1),
		'random' : Portfolio.objects.only('image').filter(status = 1).order_by('-created_date')[:10]
	})

class PortfolioView(generic.ListView):
	template_name = 'portfolio.html'
	context_object_name = 'portfolio'

	def get_queryset(self):
		return mainService(1).getPortfolio()

def resume(request):
	return render(request, 'resume.html')

def blog(request):
	return render(request, 'blog.html', {
		'blog' : Blog.objects.filter(status = 1).order_by('-created_date') 
	})

def contact(request):
	if request.method == "GET":
		return render(request, 'contact.html', {'err':'', 'postdata':''})

	form_data_dict = dict();
	form_data_dict["name"] = request.POST.get("name")
	form_data_dict["email"] = request.POST.get("email")
	form_data_dict["phone"] = request.POST.get("phone")
	form_data_dict["message"] = request.POST.get("message")

	data = dict()
	data['err'] = mainService(1).storeMessage(request)

	if bool(data['err'].get('success')) == False:
		data['postdata'] = form_data_dict

	return render(request, 'contact.html', data)