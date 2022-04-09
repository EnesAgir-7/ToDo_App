from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import NoteSerializer
from .models import Note


@api_view(['GET', ])
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
            'description': 'Creates an existing note with data sent in put request '
        },
        {
            'Endpoint':'/backend/id/delete/',
            'method':'DELETE',
            'body':None,
            'description': 'Deletes and exiting note'
        }
    ]
    return Response(routes)

@api_view(['GET'])  #! This is only going to tale in a get request
def getNotes(request):
    notes = Note.objects.all  #! going to get all the notes 
    serializer = NoteSerializer(notes, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def getNote(request, pk):
    note = Note.objects.get(id= pk)  #! going to get all the note
    serializer = NoteSerializer(note, many=False)
    return Response(serializer.data)


@api_view(['POST'])
def createNotes(request):
    data = request.data
    
    note= Note.objects.create(
        body=data['body']
    )
    serializer = NoteSerializer(note, many=False)
    return Response(serializer.data)


@api_view(['PUT'])
def updateNotes(request, pk):
    data = request.data
    
    note = Note.objects.get(id=pk)
    serializer = NoteSerializer(note, data=request.data)
    if serializer.is_valid():
        serializer.save()
    
    return Response(serializer.data)