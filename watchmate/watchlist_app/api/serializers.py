from rest_framework import serializers
from watchlist_app.models import Movie

def name_length(self, value):
    if len(value) < 2:
             raise serializers.ValidationError("Name is too short!")
         


class MovieSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(validators=[name_length])
    description = serializers.CharField()
    active = serializers.BooleanField()

    def create(self,validation_data):
        return Movie.objects.create(**validation_data)
    
    def update(self,instance ,validation_data):
        instance.name = validation_data.get('name',instance.name)
        instance.description = validation_data.get('description',instance.description)
        instance.active = validation_data.get('active',instance.active)
        instance.save()
        return instance
    
    def validate(self, data):
        if data['title'] == data['description']:
            raise serializers.ValidationError("Title and Description should be different!")
        else:
            return data
    
    #def validate_name(self, value):
         
     #    if len(value) < 2:
     #        raise serializers.ValidationError("Name is too short!")
     #    else:
      #       return value