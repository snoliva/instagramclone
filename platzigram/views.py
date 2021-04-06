from django.http import HttpResponse
from datetime import datetime
import json

def hello_world(request):
    now = datetime.now().strftime('%b, %dth, %Y, %H:%M')
    return HttpResponse('Hello World! Current time is {now}'.format(now=str(now)))

def sorted_list(request):
    #import pdb; pdb.set_trace() #DEBUGGER
    #numbers = request.GET['numbers']
    data = {
        'status': 'ok',
        'numbers': '10',
        'message': 'Integers sorted successfully'
    }
    return HttpResponse(json.dumps(data), content_type='aplication/json')

def say_hi(request, name, age):
    """Return a greeting"""

    if age < 12:
        message = ' Sorry {}, you are not allowed here'.format(name)
    else:
        message = 'Hello, {}! Welcome to Platzigram'.format(name)

    return HttpResponse(message)
