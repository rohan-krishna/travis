from django.shortcuts import render
from django.utils import timezone
from django.http import HttpResponse,HttpResponseRedirect
from django.urls import reverse

from .models import Notebook,Note
# Create your views here.
def index(request):
	notebooks = Notebook.objects.all()
	return render(request, 'notes/index.html',  { 'notebooks' : notebooks })

def create(request):
	note = Note(title=request.POST['title'],body=request.POST['body'],notebook_id=1)
	note.save()

	return HttpResponseRedirect(reverse('notes:index'))

def notes(request):
	return render(request, 'notes/list_notes.html', {})