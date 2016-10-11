from django.shortcuts import render,redirect,render_to_response,get_list_or_404,get_object_or_404
from django.http.response import HttpResponse
from django.contrib.auth.decorators import login_required
from django.http import QueryDict
from django.forms.formsets import formset_factory
from . import forms#,models
import re,glob,random

def index(request):
    utter_form=forms.UtterForm(request.GET or None)
    speaker_form=forms.SpeakerForm(request.GET or None)
    d={
        'utter_form' : utter_form,
        'speaker_form' : speaker_form,
    }
    return render(request, 'index.html', d)
