from django.shortcuts import render, redirect
from django.http import JsonResponse
from json import dumps
import random


def index(request):
    request.session['guess_result'] = ""
    request.session['random'] = random.randint(1, 100)
    print(request.session['random'])
    context = {
        "guess_result": ""
    }
    js_data = dumps(context)
    return render(request, 'index.html', {"data": js_data})


def submit_guess(request):
    if request.POST['guess']:
        request.session['guess'] = request.POST['guess']
    else:
        request.session['guess'] = 0
    return redirect("/result")


def result(request):
    if int(request.session['guess']) < request.session['random']:
        request.session['guess_result'] = "<div id='result' class='bg-danger'>" + \
            "Too Low!</div>"
    elif int(request.session['guess']) > request.session['random']:
        request.session['guess_result'] = "<div id='result' class='bg-danger'>" + \
            "Too High!</div>"
    else:
        button = "<button onclick=\"window.location.href='/'\">Play Again!</button>"
        request.session['guess_result'] = "<div id='result' class='bg-success'>" + \
            request.session['guess']+" Was the Number!"+button+"</div>"
    return render(request, 'index.html')


def api(request):
    return JsonResponse({"response": request.session['guess_result']})
