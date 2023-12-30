from django.shortcuts import render
from django.shortcuts import HttpResponse
from .models import Movies
from .forms import movieform


# Create your views here.

def viewlist(request):
    m = Movies.objects.all()
    return render(request, 'Card.html', {'movie': m})


def addform(request):
    form = movieform()
    if (request.method == "POST" ):
        form = movieform(request.POST,request.FILES)
        if (form.is_valid()):
            form.save()
            return viewlist(request)
    return render(request, 'Form.html', {'form': form})


# def viewtable(request):
#     m = Movies.objects.all()
#     return render(request, 'viewtable.html', {'movie': m})
def viewone(request, p):
    m = Movies.objects.get(id=p)
    return render(request, 'viewone.html', {'movie': m})


def deleteM(request, p):
    m = Movies.objects.get(id=p)
    m.delete()
    return render(request, 'Card.html')


def editM(request, p):
    m = Movies.objects.get(id=p)
    form = movieform(instance=m)
    if (request.method == "POST"):
        form = movieform(request.POST, request.FILES, instance=m)
        if (form.is_valid()):
            form.save()
            return viewlist(request)
        return render(request, 'Form.html', {"form": form})
    else:  # Add this else block for GET requests
        form = movieform(instance=m)
        return render(request, 'Form.html', {"form": form})
