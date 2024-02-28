from rest_framework import generics, permissions
from rest_framework.decorators import renderer_classes, parser_classes, permission_classes
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from app.models import Scenario
from app.serializers import ScenarioSerializer
from app.renderers import ScenarioXMLRenderer
from app.parsers import ScenarioXMLParser

@permission_classes([permissions.IsAuthenticatedOrReadOnly])
@renderer_classes([ScenarioXMLRenderer, JSONRenderer])
@parser_classes([ScenarioXMLParser, JSONParser])
class ScenarioList(generics.ListCreateAPIView):
    queryset = Scenario.objects.all()
    serializer_class = ScenarioSerializer


@permission_classes([permissions.IsAuthenticatedOrReadOnly])
@renderer_classes([ScenarioXMLRenderer, JSONRenderer])
@parser_classes([ScenarioXMLParser, JSONParser])
class ScenarioDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Scenario.objects.all()
    serializer_class = ScenarioSerializer