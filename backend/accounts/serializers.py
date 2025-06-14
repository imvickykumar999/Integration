from rest_framework import serializers
from django.contrib.auth import get_user_model
from django.contrib.auth.password_validation import validate_password

User = get_user_model()

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'email', 'first_name', 'last_name', 'role', 'phone', 'is_active', 'company')
        read_only_fields = ('id', 'is_active')

class UserRegistrationSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, required=True, validators=[validate_password])
    confirm_password = serializers.CharField(write_only=True, required=True)

    class Meta:
        model = User
        fields = ('email', 'password', 'confirm_password', 'first_name', 'last_name', 'role', 'phone',
                  'company_name', 'registration_number', 'industry', 'website', 'address', 'city', 'state', 'postal_code', 'country')

    def validate(self, attrs):
        if attrs['password'] != attrs['confirm_password']:
            raise serializers.ValidationError({"password": "Password fields didn't match."})
        return attrs

    def create(self, validated_data):
        # Extract company data
        company_data = {
            'name': validated_data.pop('company_name'),
            'registration_number': validated_data.pop('registration_number'),
            'industry': validated_data.pop('industry'),
            'website': validated_data.pop('website', ''), # website can be blank
            'phone': validated_data.pop('phone', ''), # phone can be blank for user, but required for company
            'address': validated_data.pop('address'),
            'city': validated_data.pop('city'),
            'state': validated_data.pop('state'),
            'postal_code': validated_data.pop('postal_code'),
            'country': validated_data.pop('country'),
        }

        validated_data.pop('confirm_password')
        user = User.objects.create_user(**validated_data)

        # Create company and link to user if role is PARENT
        if user.role == User.UserRole.PARENT:
            from companies.models import Company # Import here to avoid circular dependency
            company = Company.objects.create(owner=user, **company_data)
            user.company = company
            user.save()

        return user

class LoginSerializer(serializers.Serializer):
    email = serializers.EmailField(required=True)
    password = serializers.CharField(required=True, write_only=True) 