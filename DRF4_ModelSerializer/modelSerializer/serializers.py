from rest_framework import serializers
from .models import Student


# Model Serializer
class StudentSerializer(serializers.ModelSerializer):
    # Validators
    def start_with_r(value):
     if value[0].lower() != 'r':
        raise serializers.ValidationError('Name should starts with R !')
    
    name = serializers.CharField(validators= [start_with_r])
    
    class Meta:
        model = Student
        fields = ['name', 'roll', 'city']
        
      # Field Level Validation
    def validate_roll(self, value):
        if value >= 200:
            raise serializers.ValidationError('Seat Full!!')
        return value
    
    # Object Level Validation
    def validate(self, data):
        nm = data.get('name')
        ct = data.get('city')
        if nm.lower() == 'afid' and ct.lower() != 'dhaka':
            raise serializers.ValidationError('City must be Dhaka !')
        return data
