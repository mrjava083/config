from django.shortcuts import render
from random import choice
from .models import Roman3
# Create your views here.

def _tmpGeneration():
	tmp_session = ""
	choices = [*"abcdefghijklmnopqrstuvwxyz"]
	for i in range(32): tmp_session += choice(choices)
	return tmp_session

def home(request):
	context = {
		"roman":Roman3.objects.all().order_by('-view')
	}
	return render(request, 'gorbayhub/home.html', context)

def add(request):
	return render(request, 'gorbayhub/add.html')


def save(request):
	name = request.POST['name']
	titel = request.POST['titel']
	body = request.POST['body']
	slug = _tmpGeneration()
	view = 0
	admin = "N"
	res = Roman3(name=name, titel=titel, slug=slug, body=body, view=view, admin=admin)
	res.save()
	return render(request, 'gorbayhub/save.html')

def post(request, slug):
	post = Roman3.objects.get(slug=slug)
	post.view += 1
	post.save()
	context = {
		"post":Roman3.objects.get(slug=slug)
	}
	return render(request, 'gorbayhub/post.html', context)	

def page_not_found_view(request,exception):
	return render(request, 'gorbayhub/404.html', status=404)