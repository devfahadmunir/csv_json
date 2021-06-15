from django.shortcuts import render, HttpResponse
from .forms import *
from django.contrib import messages
from .models import *
import pandas as pd


# Create your views here.


class task():

    def index(request):
        if request.method == 'POST':
            form = csvForm(request.POST, files=request.FILES)
            if form.is_valid():
                name = form.cleaned_data['name']
                csv_file = form.cleaned_data['csv_file']
                print(name, csv_file)
                df = pd.read_csv(csv_file)
                dx = df.to_json()
                cdata = csvdata(name=name, csv_file=csv_file,
                                json_data=dx)
                cdata.save()
                messages.success(
                    request, "Your CSV file has been uploaded and sccfullay converted into Json!")
                #df.to_json (r'Path where the new JSON file will be stored\New File Name.json')

        cform = csvForm()
        params = {'form': cform}

        return render(request, "index.html", params)
