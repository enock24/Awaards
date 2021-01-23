from django.shortcuts import render,redirect,get_object_or_404
from django.http  import HttpResponse,Http404,HttpResponseRedirect
import datetime as dt
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from .models import *
from .forms import *


#rest 

# Create your views here.
