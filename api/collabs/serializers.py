
from rest_framework import serializers
from django.contrib.auth.hashers import make_password
from rest_framework.decorators import authentication_classes , permission_classes 
from .models import CustomUser , Collaboration

class CollaborationSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Collaboration
        fields = '__all__'


        extra_kwargs = {
            'business': {'view_name': 'user-detail', 'lookup_field': 'pk'},
            'influencer': {'view_name': 'user-detail', 'lookup_field': 'pk'},
        }

    
    def update(self, instance, validated_data):
        instance.reviewed = True
        instance.review_positive = validated_data.get('review_positive')
        instance.save()
        
        # Update influencer profile
        instance.influencer.influencer_profile.review(instance.review_positive)
        return instance