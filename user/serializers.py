from django.contrib.auth.models import User
from rest_framework import serializers


class RegistrationSerializer(serializers.ModelSerializer):
    repeated_password = serializers.CharField(style={'input_type': 'password'}, write_only=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password', 'repeated_password']
        # Add extra arguments on the specified fields (add write_only for password, password is defined on User model)
        extra_kwargs = {
            'password': {'write_only': True}
        }

    def save(self):
        # Compare passwords
        password = self.validated_data['password']
        repeated_password = self.validated_data['repeated_password']
        if password != repeated_password:
            raise serializers.ValidationError({'error': 'Passwords do not match!'})
        # Check if mail is unique
        if User.objects.filter(email=self.validated_data['email']).exists():
            raise serializers.ValidationError({'error': 'Email already exists!'})

        account = User(username=self.validated_data['username'], email=self.validated_data['email'])
        account.set_password(password)
        account.save()

        return account
