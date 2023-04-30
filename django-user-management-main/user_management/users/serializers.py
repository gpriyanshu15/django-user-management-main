from rest_framework import serializers
from django.contrib.auth.password_validation import validate_password
from django.core.validators import RegexValidator, validate_email
from .models import User

class UserSerializer(serializers.ModelSerializer):
    name = serializers.CharField(max_length=100)
    email = serializers.EmailField(validators=[validate_email])
    mobile = serializers.CharField(validators=[RegexValidator(regex='^[0-9]{10}$', message='Mobile number must be 10 digits long.')])
    password = serializers.CharField(write_only=True, validators=[validate_password, RegexValidator(regex='^(?=.*[A-Za-z])(?=.*\d)(?=.*[@$!%*#?&])[A-Za-z\d@$!%*#?&]{8,}$', message='Password must contain at least 8 characters, one letter, one number and one special character.')])
    
    class Meta:
        model = User
        fields = ('id', 'name', 'email', 'mobile', 'address', 'username', 'password')
        
    def create(self, validated_data):
        user = User.objects.create(
            name=validated_data['name'],
            email=validated_data['email'],
            mobile=validated_data['mobile'],
            address=validated_data['address'],
            username=validated_data['username'],
        )
        user.set_password(validated_data['password'])
        user.save()
        return user
