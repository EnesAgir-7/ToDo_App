from rest_framework.serializers import ModelSerializer
from .models import Note


class NoteSerializer(ModelSerializer):
    class Meta:
        model = Note   #! add in the model that want to serialize 
        fields = '__all__'
