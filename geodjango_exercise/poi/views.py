from django.http import Http404
from django.shortcuts import render
from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import PointOfInterest
from .serializers import PointOfInterestSerializer

# Create your views here.
'''
class PointOfInterestListCreate(generics.ListCreateAPIView):
    queryset = PointOfInterest.objects.all()
    serializer_class = PointOfInterestSerializer

class PointOfInterestDetail(generics.RetrieveDestroyAPIView):
    queryset = PointOfInterest.objects.all()
    serializer_class = PointOfInterestSerializer
'''
#versione senza generics
class PointOfInterestListCreate(APIView):
    #get di tutti i punti di interesse
    def get(self, request):
        pois = PointOfInterest.objects.all()
        serializer = PointOfInterestSerializer(pois, many=True)
        return Response(serializer.data)

    #post per mettere un punto in db
    def post(self, request):
        serializer = PointOfInterestSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class PointOfInterestDetail(APIView):

    #funzione helper, poi capisci il perché
    def get_record(self, key):
        try:
            return PointOfInterest.objects.get(pk=key)
        except PointOfInterest.DoesNotExist:
            raise Http404

    #get singolo elemento
    def get(self, request, pk):
        poi = self.get_record(pk)
        serializer = PointOfInterestSerializer(poi)
        return Response(serializer.data)

    #put per aggiornare
    def put(self, request, pk):
        poi = self.get_record(pk)
        serializer = PointOfInterestSerializer(poi, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request, pk):
        poi = self.get_record(pk)
        serializer = PointOfInterestSerializer(poi, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    #delete singolo elemento
    def delete(self, request, pk):
        poi = self.get_record(pk)
        poi.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

def index(request):
    return render(request, 'index.html')

