from django.shortcuts import render, HttpResponseRedirect
from .forms import RegisterForm
from .models import Join

import uuid

def get_ref_id():
    ref_id = str(uuid.uuid4())[:11].replace('-', '').upper()
    try:
        id_exists = Join.objects.get(ref_id=ref_id)
        get_ref_id()
    except:
        return ref_id

# Create your views here.
def home(request):

    # Model form:
    print "test"
    form = RegisterForm(request.POST or None)
    if form.is_valid():
        print "testing"
        new_registered = form.save(commit=False)
        # -----Ikke testet enda-----
        new_registered.ref_id = get_ref_id()
        # we might do something here
        new_registered.save()

    context = {"form": form}
    template = "home.html"
    return render(request, template, context)

def headset(request):
    context = {}
    template = "headset.html"
    return render(request, template, context)