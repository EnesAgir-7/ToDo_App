from types import NoneType
from django.http import JsonResponse

def getRoutes(request):
    routes = [
        {
            'Endpoint':'/backend/',
            'method':'GET',
            'body':None,
            'description': 'Returns an array of notes'
        },
        {
            'Endpoint':'/backend/id',
            'method':'GET',
            'body':None,
            'description': 'Returns a single note object'
        },
        {
            'Endpoint':'/backend/create/',
            'method':'POST',
            'body':{'body':""},
            'description': 'Creates new note with data sent in post request '
        },
        {
            'Endpoint':'/backend/id/update/',
            'method':'PUT',
            'body':{'body':""},
            'description': 'Creates new note with data sent in put request '
        },
        {
            'Endpoint':'/backend/id/delete/',
            'method':'DELETE',
            'body':None,
            'description': 'Deletes and exiting note'
        }
    ]
    return JsonResponse(routes, safe=False)