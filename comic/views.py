from django.shortcuts import render,redirect,render_to_response,get_list_or_404,get_object_or_404
from django.http.response import HttpResponse
from django.contrib.auth.decorators import login_required
from django.http import QueryDict
from django.forms.formsets import formset_factory
from . import forms#,models
import re,glob,random

def index(request):
    use_form=forms.UseForm(request.GET or None)
    utter_form=forms.UtterForm(request.GET or None)
    speaker_form=forms.SpeakerForm(request.GET or None)
    posi_form=forms.PositiveForm(request.GET or None)
    d={
        'use_form' : use_form,
        'utter_form' : utter_form,
        'speaker_form' : speaker_form,
        'posi_form' : posi_form,
    }
    return render(request, 'index.html', d)
