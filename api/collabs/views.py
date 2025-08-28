# views.py
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Collaboration
from .serializers import CollaborationSerializer
from api.user.models import BusinessProfile
from .recommendations import recommend_influencers
from api.user.serializers import InfluencerProfileSerializer  # you need this

class CollaborationViewSet(viewsets.ModelViewSet):
    queryset = Collaboration.objects.all()
    serializer_class = CollaborationSerializer
    permission_classes = [IsAuthenticated]

    # Optional: restrict updates only to the owning business
    def get_queryset(self):
        return Collaboration.objects.filter(business=self.request.user)


# views.py in collaboration/recommendation or api app




class RecommendationView(APIView):
    permission_classes = [IsAuthenticated]  # optional

    def get(self, request, business_id):
        try:
            business = BusinessProfile.objects.get(id=business_id)
        except BusinessProfile.DoesNotExist:
            return Response({"error": "Business not found"}, status=404)

        influencers = recommend_influencers(business, top_n=5)

        serializer = InfluencerProfileSerializer(influencers, many=True)
        return Response(serializer.data)
