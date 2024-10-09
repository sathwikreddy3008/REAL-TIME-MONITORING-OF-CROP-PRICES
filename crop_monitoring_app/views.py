from multiprocessing import context
from django.contrib.auth.views import LogoutView
from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login
import pandas as pd   
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from .models import Crop,Price

import os


os.chdir(os.path.dirname(__file__))






def signup_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
    else:
        form = UserCreationForm()
    return render(request, 'signup.html', {'form': form})


def logout_view(request):
    response = LogoutView.as_view()(request)

    return redirect('home')







def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('home')
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})


def home(request):
    return render(request, 'home.html')

def crop_prediction(request):



    return render(request, 'crop_prediction.html')



def dashboard(request):
    return render(request, 'dashboard.html')


def analyze(request):
    import os

    crop = pd.read_csv("dataset/Crop_recommendation.csv")


    # remove duplicate values
    crop = crop.drop_duplicates()


    # handle null values in dataset
    attr=["N","P","K","temperature","humidity","rainfall","label"]
    if crop.isna().any().sum() !=0:
        for i in range(len(attr)):
            crop[attr[i]].fillna(0.0, inplace = True)

    #Remove unwanted parts from strings in a column 
    crop.columns = crop.columns.str.replace(' ', '') 

    # we have given 7 features to the algorithm
    features = crop[['N', 'P','K','temperature', 'humidity', 'ph', 'rainfall']]

    # dependent variable is crop
    target = crop['label'] 
    x_train, x_test, y_train, y_test = train_test_split(features,target,test_size = 0.2,random_state =2)
    

    # here n_estimators is The number of trees in the forest.
    # random_state is for controlling  the randomness of the bootstrapping
    RF = RandomForestClassifier(n_estimators=20, random_state=0)

    # we'll use rf.fit to build a forest of trees from the training set (X, y).
    RF.fit(x_train,y_train)
    # at this stage our algorithm is trained and ready to use
    
    # take values from user
    N = request.POST.get('nitrogen', 'default')
    P = request.POST.get('phosphorous', 'default')
    K = request.POST.get('potassium', 'default')
    temp = request.POST.get('temperature', 'default')
    humidity = request.POST.get('humidity', 'default')
    ph =request.POST.get('ph', 'default')
    rainfall = request.POST.get('rainfall', 'default')

    # make a list of user input
    userInput = [N, P, K, temp, humidity, ph, rainfall]
    
    # use trained model to predict the data based on user input
    result = RF.predict([userInput])[0]

    # display  result to the user
    params = {'purpose':'Predicted Crop: ', 'analyzed_text': result.upper()}
    return render(request, 'analyze.html', params)    
   

def prices(request):
    crops = Crop.objects.all()
    prices = Price.objects.filter(date__lte='2024-03-05')[:10]
    return render(request, 'prices.html', {'crops': crops, 'prices': prices})

def crop_prices_prices(request):
    return render(request, 'prices/prices.html')

