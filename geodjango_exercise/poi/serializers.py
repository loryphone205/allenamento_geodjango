from rest_framework_gis.serializers import GeoFeatureModelSerializer
from .models import PointOfInterest

#dobbiamo creare il serializzatore per trasforamre in json
class PointOfInterestSerializer(GeoFeatureModelSerializer):
    class Meta:
        model = PointOfInterest
        geo_field = 'location'
        fields = ('id', 'name', 'description')