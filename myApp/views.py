from django.shortcuts import render
from myApp.forms import student

# Create your views here.
def view1(request):
    f = student()
    if request.method == 'POST':
        f = student(request.POST)
        if f.is_valid():
            mark1 = f.cleaned_data['sem1']
            mark2 = f.cleaned_data['sem2']
            mark3 = f.cleaned_data['sem3']
            mark4 = f.cleaned_data['sem4']
            mark5 = f.cleaned_data['sem5']
            mark6 = f.cleaned_data['sem6']
            mark7 = f.cleaned_data['sem7']
            mark8 = f.cleaned_data['sem8']
            sum = mark1 + mark2 + mark3 + mark4 + mark5 + mark6 + mark7 + mark8
            cgpa = sum / 8
            d = {'cgpa1': cgpa}
            return render(request,'myApp/output.html',d)
    d = { 'forms' : f }
    return render(request,'myApp/input.html',d)
    