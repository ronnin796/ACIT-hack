from rest_framework import serializers
from django.contrib.auth.hashers import make_password
from rest_framework.decorators import authentication_classes , permission_classes 
from .models import CustomUser , InfluencerProfile, BusinessProfile

class UserSerializer(serializers.HyperlinkedModelSerializer):  # Use ModelSerializer unless you need HyperlinkedModelSerializer
    def create(self, validated_data):
        password = validated_data.pop('password', None)
        instance = self.Meta.model(**validated_data)
        if password is not None:
            instance.set_password(password)  # Hashes the password
        instance.save()
        return instance

    def update(self, instance, validated_data):
        for attr, value in validated_data.items():
            if attr == 'password':
                instance.set_password(value)
            else:
                setattr(instance, attr, value)
        instance.save()
        return instance
    class Meta:
        model = CustomUser
        fields = (
            'id', 'name', 'email', 'role' , 'password', 'phone',
            'session_token', 'created_at', 'updated_at',
            'is_active', 'is_staff', 'is_superuser'
        )
        extra_kwargs = {
            'password': {'write_only': True}
        }



class InfluencerProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = InfluencerProfile
        fields = '__all__'


from .models import BusinessProfile

class BusinessProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = BusinessProfile
        fields = '__all__'
        read_only_fields = ('user',)

    def to_internal_value(self, data):
        data = data.copy()  # make mutable

        # Convert multipart list into actual Python list
        tp = data.getlist('target_platforms') if hasattr(data, 'getlist') else data.get('target_platforms')
        if tp:
            data['target_platforms'] = list(tp) if isinstance(tp, (list, tuple)) else [tp]

        ta = data.getlist('target_age') if hasattr(data, 'getlist') else data.get('target_age')
        if ta:
            data['target_age'] = [int(x) for x in ta] if isinstance(ta, (list, tuple)) else [int(ta)]

        return super().to_internal_value(data)




