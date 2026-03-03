from django.shortcuts import render
from . import final

def sentiment(request):
    res = ""

    if request.method == 'POST':
        name = request.POST.get('text data')  # safer

        if name:
            try:
                res = final.pre(str(name))
            except Exception as e:
                print(e)
                res = "Prediction Error"

    return render(request, "first.html", {'result': res})