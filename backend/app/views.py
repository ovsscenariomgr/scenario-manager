from rest_framework import generics, permissions
from rest_framework.decorators import renderer_classes, parser_classes, permission_classes
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from rest_framework_xml.renderers import XMLRenderer
from rest_framework_xml.parsers import XMLParser
from rest_framework.response import Response
from app.models import Scenario
from app.serializers import ScenarioSerializer

@permission_classes([permissions.IsAuthenticated])
@renderer_classes([XMLRenderer, JSONRenderer])
@parser_classes([XMLParser, JSONParser])
class ScenarioList(generics.ListCreateAPIView):
    queryset = Scenario.objects.all()
    serializer_class = ScenarioSerializer


@permission_classes([permissions.IsAuthenticated])
@renderer_classes([XMLRenderer, JSONRenderer])
@parser_classes([XMLParser, JSONParser])
class ScenarioDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Scenario.objects.all()
    serializer_class = ScenarioSerializer